import pandas as pd

# 读取json
# lines=False：以一行为一个样本
# orient="records":以records格式读取
data = pd.read_json("student1.json", lines=False, orient="records")
print(data)

# 存储json
data.to_json("student2.json")
