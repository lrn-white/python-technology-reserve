import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder, Normalizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA


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
                MinMaxScaler().fit_transform(df[colume_list[i]].values.reshape(-1, 1)).reshape(1, -1)[
                    0]
        else:
            df[colume_list[i]] = \
                StandardScaler().fit_transform(df[colume_list[i]].values.reshape(-1, 1)).reshape(1, -1)[
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
                MinMaxScaler().fit_transform(df[colume_list2[i]].values.reshape(-1, 1)).reshape(1, -1)[
                    0]
        else:
            df = pd.get_dummies(df, colume_list2[i])
    if lower_d:
        return PCA(n_components=ld_n).fit_transform(df.values), label
    return df, label


def map_salary(s):
    d = dict([("low", 0), ("medium", 1), ("high", 2)])
    return d.get(s, 0)


def main():
    print(hr_preprocessing())


if __name__ == '__main__':
    main()
