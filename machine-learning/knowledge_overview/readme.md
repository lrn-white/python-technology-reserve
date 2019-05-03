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
总结：

优点:
- 速度快: 计算量相对较小, 且容易转化成分类规则. 只要沿着树根向下一直走到叶, 沿途的分裂条件就能够唯一确定一条分类的谓词.
- 准确性高: 挖掘出来的分类规则准确性高, 便于理解, 决策树可以清晰的显示哪些字段比较重要, 即可以生成可以理解的规则.
- 可以处理连续和种类字段
- 不需要任何领域知识和参数假设
- 适合高维数据

缺点:
- 对于各类别样本数量不一致的数据, 信息增益偏向于那些更多数值的特征
- 容易过拟合
- 忽略属性之间的相关性

作者：小贤_xian
链接：https://www.jianshu.com/p/655d8e555494
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

适用数据类型：数值型和标称型
###### 1.4 支持向量机(SVM)
总结：

优点：

- 可以解决高维问题，即大型特征空间；
- 能够处理非线性特征的相互作用；
- 无需依赖整个数据；
- 可以提高泛化能力；
- 需要对数据提前归一化，很多人使用的时候忽略了这一点，毕竟是基于距离的模型，所以LR也需要归一化

缺点:
- 当观测样本很多时，效率并不是很高；
- 一个可行的解决办法是模仿随机森林，对数据分解，训练多个模型，然后求平均，时间复杂度降低p倍，分多少份，降多少倍
- 对非线性问题没有通用解决方案，有时候很难找到一个合适的核函数；
- 对缺失数据敏感；
###### 1.5 集成方法
随机森林

随机森林使用数据的随机样本独立训练每棵树。 这种随机性有助于使模型比单个决策树更稳健，并且不太过拟合训练数据。 RF中通常有两个参数 - 树数量和被选择的每个结点的特征数目（列抽样）。

- RF适用于并行或分布式计算。
- 几乎总是比决策树具有更低的分类错误和更好的f分数。
- 几乎总是表现出与SVM相同或更好的效果，但对于人类来说更容易理解。
- 非常适合具有缺失变量的不均匀数据集。
- 给你一个关于你的数据集中的哪些特征是最重要的免费的好主意。
- 通常训练速度比支持向量机要快（尽管这显然取决于你的实现）。

提升法Adaboost

###### 1.6 各个模型的应用场景

随机森林平均来说最强。数据维度越高，随机森林就比AdaBoost强越多，但是整体不及SVM。
数据量越大，神经网络就越强。

- KNN：需要一个特别容易解释的模型的时候，比如需要向用户解释原因的推荐算法。
- 贝叶斯：需要一个比较容易解释，而且不同维度之间相关性较小的模型的时候。可以高效处理高维数据，虽然结果可能不尽如人意。
- 决策树：它能够生成清晰的基于特征(feature)选择不同预测结果的树状结构，数据分析师希望更好的理解手上的数据的时候往往可以使用决策树（画出图）。
常用于金融领域的期权定价，期权分析。
- 随机森林：随机森林在现实分析中被大量使用，它相对于决策树，在准确性上有了很大的提升，同时一定程度上改善了决策树容易被攻击的特点。
数据维度相对低（几十维），同时对准确性有较高要求时。
因为不需要很多参数调整就可以达到不错的效果，基本上不知道用什么方法的时候都可以先试一下随机森林。
- SVM：相对来说，SVM尽量保持与样本间距离的性质导致它抗攻击的能力更强。
和随机森林一样，这也是一个拿到数据就可以先尝试一下的算法。

##### 2.回归模型
###### 2.1 线性回归 
特点：
- 建模速度快，不需要很复杂的计算，在数据量大的情况下依然运行速度很快。 
- 可以根据系数给出每个变量的理解和解释 
- 对异常值很敏感
###### 2.2 逻辑斯特回归 （LR）
LR是解决工业规模问题最流行的算法。在工业应用上，如果需要分类的数据拥有很多有意义的特征，每个特征都对最后的分类结果有或多或少的影响，那么最简单最有效的办法就是将这些特征线性加权，一起参与到决策过程中。比如预测广告的点击率，从原始数据集中筛选出符合某种要求的有用的子数据集等等。

优点：
- 适合需要得到一个分类概率的场景。
- 计算代价不高，容易理解实现。LR在时间和内存需求上相当高效。它可以应用于分布式数据，并且还有在线算法实现，用较少的资源处理大型数据。
- LR对于数据中小噪声的鲁棒性很好，并且不会受到轻微的多重共线性的特别影响。（严重的多重共线性则可以使用逻辑回归结合L2正则化来解决，但是若要得到一个简约模型，L2正则化并不是最好的选择，因为它建立的模型涵盖了全部的特征。）

缺点：
- 容易欠拟合，分类精度不高。
- 数据特征有缺失或者特征空间很大时表现效果并不好。
###### 2.3 人工神经网络
目前深度神经网络已经应用与计算机视觉，自然语言处理，语音识别等领域并取得很好的效果。

优点：
- 分类准确度高，学习能力极强。
- 对噪声数据鲁棒性和容错性较强。
- 有联想能力，能逼近任意非线性关系。

缺点：
- 神经网络参数较多，权值和阈值。
- 黑盒过程，
###### 1.1 K-means算法
###### 1.2 DBSCAN算法
###### 1.3 层次聚类
不能观察中间结果。
- 学习过程比较长，有可能陷入局部极小值。
###### 2.4 回归树
优点：决策树能学习非线性关系，对异常值也具有很强的鲁棒性。集成学习在实践中表现非常好，其经常赢得许多经典的（非深度学习）机器学习竞赛。

缺点：无约束的，单棵树很容易过拟合，因为单棵树可以保留分支（不剪枝），并直到其记住了训练数据。集成方法可以削弱这一缺点的影响。
#### 二、非监督学习
##### 1.聚类模型
#### 三、选择适用的模型
![image](ml_map.png)