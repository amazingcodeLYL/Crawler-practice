import numpy as np
import pandas as pd
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#     A   B key1 key2
# 0  A0  B0   K0   K0
# 1  A1  B1   K0   K1
# 2  A2  B2   K1   K0
# 3  A3  B3   K2   K1

print(right)
#     C   D key1 key2
# 0  C0  D0   K0   K0
# 1  C1  D1   K1   K0
# 2  C2  D2   K1   K0
# 3  C3  D3   K2   K0

#合并时有四种形式 left,right,inner,outer
res=pd.merge(left,right,on=['key1','key2'],how='inner')
print(res)
#     A   B key1 key2   C   D
# 0  A0  B0   K0   K0  C0  D0
# 1  A2  B2   K1   K0  C1  D1
# 2  A2  B2   K1   K0  C2  D2

res=pd.merge(left,right,on=['key1','key2'],how='outer')
print(res)
#      A    B key1 key2    C    D
# 0   A0   B0   K0   K0   C0   D0
# 1   A1   B1   K0   K1  NaN  NaN
# 2   A2   B2   K1   K0   C1   D1
# 3   A2   B2   K1   K0   C2   D2
# 4   A3   B3   K2   K1  NaN  NaN
# 5  NaN  NaN   K2   K0   C3   D3

res=pd.merge(left,right,on=['key1','key2'],how='left')
print(res)
#     A   B key1 key2    C    D
# 0  A0  B0   K0   K0   C0   D0
# 1  A1  B1   K0   K1  NaN  NaN
# 2  A2  B2   K1   K0   C1   D1
# 3  A2  B2   K1   K0   C2   D2
# 4  A3  B3   K2   K1  NaN  NaN

res=pd.merge(left,right,on=['key1','key2'],how='right')
print(res)
#      A    B key1 key2   C   D
# 0   A0   B0   K0   K0  C0  D0
# 1   A2   B2   K1   K0  C1  D1
# 2   A2   B2   K1   K0  C2  D2
# 3  NaN  NaN   K2   K0  C3  D3

#Indicator会将合并的记录放在新的一列

d1=pd.DataFrame({'cc':[0,1],'cc_left':['a','b']})
d2=pd.DataFrame({'cc':[1,2,3],'cc_right':[2,2,2]})
res=pd.merge(d1,d2,on='cc',how='outer',indicator=True)
print(res)
#    cc cc_left  cc_right      _merge
# 0   0       a       NaN   left_only
# 1   1       b       2.0        both
# 2   2     NaN       2.0  right_only
# 3   3     NaN       2.0  right_only

#自定义indicator名称
res=pd.merge(d1,d2,on='cc',how='outer',indicator='indicator_column')
print(res)
#    cc cc_left  cc_right indicator_column
# 0   0       a       NaN        left_only
# 1   1       b       2.0             both
# 2   2     NaN       2.0       right_only
# 3   3     NaN       2.0       right_only


cat=pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
mouse=pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res=pd.merge(cat,mouse,on='k',suffixes=['_cat','_mouse'],how='inner')
print(res)
#    age_cat   k  age_mouse
# 0        1  K0          4
# 1        1  K0          5