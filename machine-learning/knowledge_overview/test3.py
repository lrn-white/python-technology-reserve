import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 可视化分析
# 柱状图
df = pd.read_csv("HR.csv")
#
# sns.set_style(style="darkgrid")
# # 标题
# plt.title('SALARY')
# # x轴
# plt.xlabel("salary")
# # y轴
# plt.ylabel("number")
# # x轴标注
# plt.xticks(np.arange(len(df['salary'].value_counts())) + 0.5, df['salary'].value_counts().index)
#
# # 取值范围,x轴0到4，y轴0到10000
# plt.axis([0, 4, 0, 10000])
# # 画出x，y轴，x轴左移0.5，宽度为0.5
# plt.bar(np.arange(len(df['salary'].value_counts())) + 0.5, df['salary'].value_counts(), width=0.5)
#
# # 标明值
# for x, y in zip(np.arange(len(df['salary'].value_counts())) + 0.5, df['salary'].value_counts()):
#     plt.text(x, y, y, ha="center", va="bottom")
# plt.show()


# 直方图
# f = plt.figure()
# f.add_subplot(1, 3, 1)
# sns.distplot(df['satisfaction_level'], bins=10)
# plt.show()

# 箱线图
# sns.boxplot(y=df['time_spend_company'])
# plt.show()

# 折现图
# sub_df = df.groupby("time_spend_company").mean()
# sns.pointplot(sub_df.index,sub_df["left"])
# plt.show()

# 饼图
lbs = df['Department'].value_counts().index
plt.pie(df['Department'].value_counts(normalize=True), labels=lbs, autopct="%1.1f%%")
plt.show()
