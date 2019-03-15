import random
import time
import numpy as np

"""
ndarray和python原生list性能对比:
Numpy针对ndarray的操作和进行了优化，数组越大，numpy的优势越明显
原因：
1.ndarray需要相同类型存储，可以进行连续存储；list支持不同类型存储，通用性较强
2.ndarray支持向量化运算
3.ndarray底层由C语言实现
"""
a = []
for i in range(10000000):
    a.append(random.random())
t1 = time.time()
sum1 = sum(a)
t2 = time.time()

b = np.array(a)
t4 = time.time()
sum2 = np.sum(b)
t5 = time.time()

print("原生list：" + str(t2 - t1))
print("ndarray：" + str(t5 - t4))

"""
原生list：0.04097104072570801
ndarray：0.0110015869140625
"""
