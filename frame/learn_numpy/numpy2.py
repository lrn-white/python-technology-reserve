import numpy as np

a = np.array([["Sam", 12], ["Tom", 15], ["Jetty", 18]])
print("形状：" + str(a.shape))
print("维度：" + str(a.ndim))
print("元素：" + str(a.size))
# 类型,整数默认为int(64),浮点数默认为float(64)
print("类型：" + str(a.dtype))

"""
形状：(3, 2)
维度：2
元素：6
类型：<U5
"""
