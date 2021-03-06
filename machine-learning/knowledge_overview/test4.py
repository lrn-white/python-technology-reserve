import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder, Normalizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split


# 判断什么类型的人容易离职

# 对HR表进行数据预处理
# sl:satisfaction_level-- False:MinMaxScaler,True:StandardScaler,False:归一化，True:标准化
# le:last_evaluation-- False:MinMaxScaler,True:StandardScaler
# npr:number_project-- False:MinMaxScaler,True:StandardScaler
# amh:average_montly_hours-- False:MinMaxScaler,True:StandardScaler
# tsc:time_spend_company-- False:MinMaxScaler,True:StandardScaler
# wa:Work_accident-- False:MinMaxScaler,True:StandardScaler
# pl5:promotion_last_5years-- False:MinMaxScaler,True:StandardScaler
# dp:Department-- False:LabelEncoder,True:OneHotEncoder
# slr:salary-- False:LabelEncoder,True:OneHotEncoder
# lower_d:不降维
# ld_n:降维时的参数
def hr_preprocessing(sl=False, le=False, npr=False, amh=False, tsc=False, wa=False, pl5=False, dp=False, slr=False,
                     lower_d=False, ld_n=1):
    df = pd.read_csv("HR.csv")

    # 1.清洗数据
    # 删除空值
    df = df.dropna(subset=["satisfaction_level", "last_evaluation"])
    df = df[df["satisfaction_level"] <= 1][df["salary"] != "nme"]

    # 2.得到标注
    label = df["left"]
    # 删除left这列
    df = df.drop("left", axis=1)

    # 3.特征选择

    # 4.特征处理
    scaler_list = [sl, le, npr, amh, tsc, wa, pl5]
    colume_list = ["satisfaction_level", "last_evaluation", "number_project", "average_montly_hours",
                   "time_spend_company", "Work_accident", "promotion_last_5years"]
    for i in range(len(scaler_list)):
        if not scaler_list[i]:
            df[colume_list[i]] = \
                MinMaxScaler().fit_transform(df[colume_list[i]].astype(float).values.reshape(-1, 1)).reshape(1, -1)[
                    0]
        else:
            df[colume_list[i]] = \
                StandardScaler().fit_transform(df[colume_list[i]].astype(float).values.reshape(-1, 1)).reshape(1, -1)[
                    0]

    scaler_list2 = [dp, slr]
    colume_list2 = ["Department", "salary"]
    for i in range(len(scaler_list2)):
        if not scaler_list2[i]:
            if colume_list[i] == "salary":
                df[colume_list2[i]] = [map_salary(s) for s in df["salary"].values]
            else:
                df[colume_list2[i]] = LabelEncoder().fit_transform(df[colume_list2[i]])
            df[colume_list2[i]] = \
                MinMaxScaler().fit_transform(df[colume_list2[i]].astype(float).values.reshape(-1, 1)).reshape(1, -1)[
                    0]
        else:
            df = pd.get_dummies(df, colume_list2[i])
    if lower_d:
        return PCA(n_components=ld_n).fit_transform(df.values), label
    return df, label


def map_salary(s):
    d = dict([("low", 0), ("medium", 1), ("high", 2)])
    return d.get(s, 0)


# 训练模型
def hr_modeling(features, label):
    # 划分训练集，测试集，验证集，按占比6:2:2分配
    f_v = features.values
    l_v = label.values
    X_tt, X_validation, Y_tt, Y_validation = train_test_split(f_v, l_v, test_size=0.2)
    X_train, X_test, Y_train, Y_test = train_test_split(X_tt, Y_tt, test_size=0.25)

    from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
    from sklearn.metrics import accuracy_score, recall_score, f1_score
    from sklearn.naive_bayes import GaussianNB, BernoulliNB
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.linear_model import LogisticRegression
    from keras.layers.core import Dense, Activation
    from keras.optimizers import SGD
    from keras.models import Sequential
    from sklearn.ensemble import GradientBoostingClassifier

    # 人工神经网络
    # mdl = Sequential()
    # mdl.add(Dense(50, input_dim=len(f_v[0])))
    # mdl.add(Activation("sigmoid"))
    # mdl.add(Dense(2))
    # mdl.add(Activation("softmax"))
    # sgd = SGD(lr=0.1)
    # mdl.compile(loss="mean_squared_error", optimizer="adam")
    # mdl.fit(X_train, np.array([[0, 1] if i == 1 else [1, 0] for i in Y_train]), nb_epoch=20000, batch_size=8999)
    # xy_lst = [(X_train, Y_train), (X_validation, Y_validation), (X_test, Y_test)]
    # for i in range(len(xy_lst)):
    #     X_part = xy_lst[i][0]
    #     Y_part = xy_lst[i][1]
    #     Y_pred = mdl.predict_classes(X_part)
    #     print(i)
    #     # 衡量指标,验证集对比
    #     print("NN", "-ACC:", accuracy_score(Y_part, Y_pred))
    #     print("NN", "-REC:", recall_score(Y_part, Y_pred))
    #     print("NN", "-F-Score:", f1_score(Y_part, Y_pred))

    models = []

    # KNN 模型
    models.append(("KNN", KNeighborsClassifier(n_neighbors=3)))
    # 朴素贝叶斯模型
    models.append(("GaussianNB", GaussianNB()))
    models.append(("BernoulliNB", BernoulliNB()))
    # 决策树
    models.append(("DecisionTree", DecisionTreeClassifier()))
    # 支持向量机
    models.append(("SVM", SVC(C=1000)))
    # 随机森林
    models.append(("RandomForest", RandomForestClassifier(n_estimators=11, max_features=None)))
    # 提升法
    models.append(("AdaBoost", AdaBoostClassifier(n_estimators=100)))
    # 逻辑斯特回归
    models.append(("LogisticRegression", LogisticRegression(C=1000, tol=1e-10, solver="sag", max_iter=10000)))
    # 回归树
    models.append(("GBDT", GradientBoostingClassifier(max_depth=6, n_estimators=100)))
    for clf_name, clf in models:
        clf.fit(X_train, Y_train)
        xy_lst = [(X_train, Y_train), (X_validation, Y_validation), (X_test, Y_test)]
        for i in range(len(xy_lst)):
            X_part = xy_lst[i][0]
            Y_part = xy_lst[i][1]
            Y_pred = clf.predict(X_part)
            print(i)
            # 衡量指标,验证集对比
            print(clf_name, "-ACC:", accuracy_score(Y_part, Y_pred))
            print(clf_name, "-REC:", recall_score(Y_part, Y_pred))
            print(clf_name, "-F-Score:", f1_score(Y_part, Y_pred))

    # 存储模型
    # from sklearn.externals import joblib
    # joblib.dump(knn_clf, "knn_clf")
    # # 加载模型
    # joblib.load("knn_clf")


# 回归模型
def regr_test(features, label):
    print("X", features)
    print("Y", label)
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    # 线性回归
    # regr = LinearRegression()
    # regr = Ridge(alpha=0.1)
    regr = Lasso(alpha=0.1)

    regr.fit(features.values, label.values)
    Y_pred = regr.predict(features.values)
    print("Coef:", regr.coef_)
    from sklearn.metrics import mean_squared_error
    print("MSE:", mean_squared_error(Y_pred, label.values))


def main():
    features, label = hr_preprocessing()
    hr_modeling(features, label)
    # regr_test(features[["number_project", "average_montly_hours"]], features["last_evaluation"])#


if __name__ == '__main__':
    main()
