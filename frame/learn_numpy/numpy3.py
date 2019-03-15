import numpy as np

"""
生成0或1:
a = np.zeros(shape)
b = np.ones(shape)
"""
a = np.zeros((3, 2))
b = np.ones((2, 3))
print(a)
print(b)

"""
从现有数组中生成
np.array,np.copy是深拷贝,np.asarray是浅拷贝
"""
c = np.array([["Sam", 12], ["Tom", 15], ["Jetty", 18]])
d = np.copy(c)
e = np.asarray(c)
print(c)
print(d)
print(e)

"""
生成给定范围的数组
np.linspace(0, 10, 100):生成0到10之间100个数,注意:[0,10]的等距离的数
np.arange(0, 100, 10):生成0到100之间步长为10的数,注意:[0,100)距离为10
"""
f = np.linspace(0, 10, 100)
g = np.arange(0, 100, 10)
print(f)
print(g)

"""
生成随机数组
均匀分布:np.random.uniform(-1, 1, 10000000)落在每一组的可能性相等,[-1,1)之间取10000000个数
正态分布:np.random.normal(1.75, 0.1, 10000)均值为1.75.标准差为0.1
"""
h = np.random.uniform(-1, 1, 10000000)
j = np.random.normal(1.75, 0.1, 10000)
print(h)
print(j)
