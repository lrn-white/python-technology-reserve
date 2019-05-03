import pandas as pd
import numpy as np
# 处理异常值

# 判断异常数据：空值，特大或特小值，类别之外的字
df = pd.read_csv("HR.csv")

sl_s = df['satisfaction_level']

# 判断每一行是否有空值
sl_s.isnull()
# 找出空值所在的行
sl_s[sl_s.isnull()]
# 丢弃空值数据
sl_s = sl_s.dropna()
# 均值
sl_s.mean()
# 标准差
sl_s.std()
# 最大值
sl_s.max()
# 最小值
sl_s.min()
# 中位数
sl_s.median()
# 下四分位数
sl_s.quantile(q=0.25)
# 偏度(为负则表示均值偏小）
sl_s.skew()
# 分布
sl_s.kurt()

np_s = df['number_project']
# 每个值出现的次数
np_s.value_counts()
# 每个值的构成比例
np_s.value_counts(normalize=True)

# 排除异常的汉字
s_s = df['salary']
s_s = s_s.where(s_s != "nme").dropna()
