import pandas as pd
import numbers as np

# 对比分析
df = pd.read_csv("HR.csv")

# 按部门分组并求各组的均值
df.groupby("Department").mean()
# 只取两列值并分组
df.loc[:, ["Department", "satisfaction_level"]].groupby("Department").mean()
