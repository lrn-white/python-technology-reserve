import pandas as pd

"""
操作excel文件
"""

# 读取文件
data = pd.read_excel("student1.xlsx")
print(data)

# 读取文件中的某几列
data1 = pd.read_excel("student1.xlsx", usecols=["name", "age"])
print(data1)

# 重命名列名
data2 = pd.read_excel("student1.xlsx", names=["1", "2", "3"])
print(data2)

# 存储excel文件
# 保存第一行数据，保存name列数据,不保存行索引
data[:1].to_excel("student2.xlsx", columns=["name"], index=False)
