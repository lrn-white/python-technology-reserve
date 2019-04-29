### 机器学习
#### 一、监督学习
##### 1.分类模型
###### 1.1 KNN
将训练集的一条数据按照“闵可夫斯基公式”转换成一个坐标点，传入验证集时，
同样将验证集的数据转换为一个点，获取离这个点最近的训练集的点的分类，即预测结果
```python
 # KNN 模型(邻近算法)
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
knn_clf = KNeighborsClassifier(n_neighbors=3)
knn_clf.fit(X_train, Y_train)
Y_pred = knn_clf.predict(X_validation)

# 衡量指标,验证集对比
from sklearn.metrics import accuracy_score, recall_score, f1_score
print("ACC:", accuracy_score(Y_validation, Y_pred))
print("REC:", recall_score(Y_validation, Y_pred))
print("F-Score:", f1_score(Y_validation, Y_pred))

# 测试集对比
Y_pred = knn_clf.predict(X_test)
print("ACC:", accuracy_score(Y_test, Y_pred))
print("REC:", recall_score(Y_test, Y_pred))
print("F-Score:", f1_score(Y_test, Y_pred))

# 存储模型
from sklearn.externals import joblib
joblib.dump(knn_clf, "knn_clf")
# 加载模型
joblib.load("knn_clf")
```
总结：

优点：
- 简单好用，容易理解，精度高，理论成熟，既可以用来做分类也可以用来做回归；
- 可用于数值型数据和离散型数据；
- 训练时间复杂度为O(n)；无数据输入假定；
- 对异常值不敏感

缺点：
- 计算复杂性高；空间复杂性高；
- 样本不平衡问题（即有些类别的样本数量很多，而其它样本的数量很少）；
- 一般数值很大的时候不用这个，计算量太大。但是单个样本又不能太少 否则容易发生误分。
- 最大的缺点是无法给出数据的内在含义。

###### 1.2 朴素贝叶斯
前提：假设各特征之间相互独立

贝叶斯公式：P(B|A)=P(A|B)P(B)/P(A)

根据训练集算出各个特征的概率，导入验证集后，根据概率算出结果的概率，得出结论

例如：判断某个人是否近视

是否熬夜| 是否关灯看手机| 是否近视
---|---|---
1 | 1 | 1 
0 | 0 | 0 
1 | 0 | 0 

假设近视的人中，熬夜的概率是80%，关灯看手机的概率是70%
不近视的人中，熬夜的概率是60%，关灯看手机的概率是20%
那么如果一个人不熬夜，关灯看手机，那么他近视的概率是 20%*70% = 14%，不近视的概率是40%*20%=8%
14%<8%
结论：他近视


总结：

优点：

- 生成式模型，通过计算概率来进行分类，可以用来处理多分类问题，
- 对小规模的数据表现很好，适合多分类任务，适合增量式训练，算法也比较简单。

缺点：

- 对输入数据的表达形式很敏感，
- 由于朴素贝叶斯的“朴素”特点，所以会带来一些准确率上的损失。需要一个比较容易解释，而且不同维度之间相关性较小的模型的时候。
- 需要计算先验概率，分类决策存在错误率。
###### 1.3 决策树
###### 1.4 支持向量机
###### 1.5 集成方法
###### 1.6 罗吉斯特映射
###### 1.7 人工神经网络
