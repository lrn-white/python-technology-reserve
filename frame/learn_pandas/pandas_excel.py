import pandas as pd
import numpy as np

# 读取excel文件
data = pd.read_excel('pandas1.xlsx')

# 保存到excel中
data.to_excel('pandas2.xlsx')
