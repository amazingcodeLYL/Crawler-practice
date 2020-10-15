#Pandas处理丢失数据
import numpy as np
import pandas as pd
dates=pd.date_range('20190101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)
#              A     B     C   D
# 2019-01-01   0   NaN   2.0   3
# 2019-01-02   4   5.0   NaN   7
# 2019-01-03   8   9.0  10.0  11
# 2019-01-04  12  13.0  14.0  15
# 2019-01-05  16  17.0  18.0  19
# 2019-01-06  20  21.0  22.0  23

#去掉NaN的行或列，可以使用dropna
df=df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='any'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
    )
print(df)

#将NaN的值用其他值替换
df=df.fillna(value=0)
print(df)
#              A     B     C   D
# 2019-01-01   0   0.0   2.0   3
# 2019-01-02   4   5.0   0.0   7
# 2019-01-03   8   9.0  10.0  11
# 2019-01-04  12  13.0  14.0  15
# 2019-01-05  16  17.0  18.0  19
# 2019-01-06  20  21.0  22.0  23

#判断是否有缺失数据NaN，为True表示确实数据
print(df.isnull())
#                 A      B      C      D
# 2019-01-01  False   True  False  False
# 2019-01-02  False  False   True  False
# 2019-01-03  False  False  False  False
# 2019-01-04  False  False  False  False
# 2019-01-05  False  False  False  False
# 2019-01-06  False  False  False  False

#检测数据中是否存在NaN，存在就返回True
print(np.any(df.isnull())==True)
#True