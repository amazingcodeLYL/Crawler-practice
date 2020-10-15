import pandas as pd
import numpy as np
s=pd.Series([1,3,6,np.nan,44,1])
print(s)
# 这里我们没有给数据指定索引
# 会自动创建一个0到N-1的整数型索引
# 0     1.0
# 1     3.0
# 2     6.0
# 3     NaN
# 4    44.0
# 5     1.0
# dtype: float64

datas=pd.date_range('20160101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=datas,columns=['a','b','c','d'])
#DataFrame是一个表格型的数据结构，包含一组有序的列
#既有行索引又有列索引
print(df)
#                    a         b         c         d
# 2016-01-01  1.585208 -0.990413  1.236099 -0.388732
# 2016-01-02  0.495724  0.059505  0.416845 -0.181266
# 2016-01-03 -1.859331  0.071485 -0.665165  0.110948
# 2016-01-04  2.665616 -0.974616  0.047750 -0.623723
# 2016-01-05 -0.618240 -0.770843  0.779370 -1.378176
# 2016-01-06 -0.101552  1.311490 -0.665657  0.854078
print(df['b'])
# 2016-01-01   -2.038565
# 2016-01-02    0.378850
# 2016-01-03    0.354676
# 2016-01-04    0.096856
# 2016-01-05    2.455016
# 2016-01-06    0.702862
# Freq: D, Name: b, dtype: float64

df1=pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo
print(df2.dtypes)
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object
print(df2.index)
# Int64Index([0, 1, 2, 3], dtype='int64')
print(df2.columns)
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
print(df2.values)
# [[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]
print(df2.describe())
#          A    C    D
# count  4.0  4.0  4.0
# mean   1.0  1.0  3.0
# std    0.0  0.0  0.0
# min    1.0  1.0  3.0
# 25%    1.0  1.0  3.0
# 50%    1.0  1.0  3.0
# 75%    1.0  1.0  3.0
# max    1.0  1.0  3.0
print(df2.T)#转置

#对index进行排序
print(df2.sort_index(axis=1,ascending=False))
#      F      E  D    C          B    A
# 0  foo   test  3  1.0 2013-01-02  1.0
# 1  foo  train  3  1.0 2013-01-02  1.0
# 2  foo   test  3  1.0 2013-01-02  1.0
# 3  foo  train  3  1.0 2013-01-02  1.0

#对数据值进行排序
print(df2.sort_values(by='B'))
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo


