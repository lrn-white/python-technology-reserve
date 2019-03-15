import pandas as pd
import numpy as np

"""
DataFrame:既有行索引又有列索引的二维数组
"""
stock_change = np.random.normal(0, 1, (10, 5))

# 初始化数据
stock_date1 = pd.DataFrame(stock_change)
print(stock_date1)

# 添加行索引
stock = ["股票{}".format(i) for i in range(10)]
stock_date2 = pd.DataFrame(stock_change, index=stock)
print(stock_date2)

# 添加列索引
date = pd.date_range(start="20180101", periods=5, freq="B")
stock_date3 = pd.DataFrame(stock_change, index=stock, columns=date)
print(stock_date3)

# 行列索引转置
print(stock_date3.T)

# DateFrame属性
print("状态：" + str(stock_date3.shape))
print("行索引：" + str(stock_date3.index))
print("列索引：" + str(stock_date3.columns))
print("排除行列索引的值：" + str(stock_date3.values))

# DateFrame属性常用方法
print("默认返回前5行：" + str(stock_date3.head()))
print("默认返回后5行：" + str(stock_date3.tail()))

# 修改行列索引值，注意：不能单独修改某一行或某一列
stock_ = ["股票_{}".format(i) for i in range(10)]
stock_date3.index = stock_
print(stock_date3)

# 重设索引，将原先的索引设为列，并重新添加索引
print(stock_date3.reset_index())

# 将某一列设置为新索引
print(stock_date3.set_index("2018-01-01"))
