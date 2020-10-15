import numpy as np
import pandas as pd
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])
#按照join_axes指定的索引合并
print(res)
#axis=1按列进行合并
#      a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0

res=pd.concat([df1,df2],axis=1)
#与上面不同的是去掉按df1设定的索引，根据各自的索引添加元素
print(res)
#      a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0

#append添加数据
#append只能添加纵向合并，没有横向合并
df3=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df4=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df5=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
lyl=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(lyl)
# a    1
# b    2
# c    3
# d    4
res=df1.append(lyl,ignore_index=True)
print(res)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  2.0  3.0  4.0
res=df1.append(df2,ignore_index=True)
print(res)
#      a    b    c    d    e
# 0  0.0  0.0  0.0  0.0  NaN
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0
# 5  NaN  1.0  1.0  1.0  1.0
res=df1.append([df2,df3],ignore_index=True)
print(res)
#   a    b    c    d    e
# 0  0.0  0.0  0.0  0.0  NaN
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0
# 5  NaN  1.0  1.0  1.0  1.0
# 6  0.0  0.0  0.0  0.0  NaN
# 7  0.0  0.0  0.0  0.0  NaN
# 8  0.0  0.0  0.0  0.0  NaN


#合并merge
left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3']})
right=pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#     A   B key
# 0  A0  B0  K0
# 1  A1  B1  K1
# 2  A2  B2  K2
# 3  A3  B3  K3
print(right)
#     C   D key
# 0  C0  D0  K0
# 1  C1  D1  K1
# 2  C2  D2  K2
# 3  C3  D3  K3
res=pd.merge(left,right,on='key')
print(res)
#     A   B key   C   D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K2  C2  D2
# 3  A3  B3  K3  C3  D3
