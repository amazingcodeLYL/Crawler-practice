import numpy as np
import pandas as pd
dates=pd.date_range('20190101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df['A'])
# print(df.A)
# 2019-01-01     0
# 2019-01-02     4
# 2019-01-03     8
# 2019-01-04    12
# 2019-01-05    16
# 2019-01-06    20
# Freq: D, Name: A, dtype: int32
print(df[0:3])
#             A  B   C   D
# 2019-01-01  0  1   2   3
# 2019-01-02  4  5   6   7
# 2019-01-03  8  9  10  11
print(df["20190102":"20190104"])
#              A   B   C   D
# 2019-01-02   4   5   6   7
# 2019-01-03   8   9  10  11
# 2019-01-04  12  13  14  15
#通过标签名字选取某一行数据
print(df.loc['20190101'])
# A    0
# B    1
# C    2
# D    3
# Name: 2019-01-01 00:00:00, dtype: int32

print(df.loc[:,'A':'B'])
#              A   B
# 2019-01-01   0   1
# 2019-01-02   4   5
# 2019-01-03   8   9
# 2019-01-04  12  13
# 2019-01-05  16  17
# 2019-01-06  20  21

print(df.loc['20190102',['A','B']])
# A    4
# B    5

#根据位置选择iloc
print(df.iloc[3,1])#13
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
#混合选择,选择前三行和‘A’和‘C’的两列
print(df.ix[:3,['A','C']])
#通过判断筛选
print(df[df.A>8])
#              A   B   C   D
# 2019-01-04  12  13  14  15
# 2019-01-05  16  17  18  19
# 2019-01-06  20  21  22  23
