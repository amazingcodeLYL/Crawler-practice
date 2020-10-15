import numpy as np
A=np.arange(2,14).reshape((3,4))
print(A)
# [[ 2  3  4  5]
#  [ 6  7  8  9]
#  [10 11 12 13]]
print(np.argmin(A)) #索引0
print(np.argmax(A)) #11

print(np.mean(A)) #计算均值 7.5
print(A.mean()) #等同于上面一种方法
print(np.average(A)) #7.5

print(np.cumsum(A)) #累加函数
#[ 2  5  9 14 20 27 35 44 54 65 77 90]


print(np.diff(A)) #前一项和后一项之差
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

B=np.arange(14,2,-1).reshape((3,4))
print(B)
# [[14 13 12 11]
#  [10  9  8  7]
#  [ 6  5  4  3]]
print("B[2]=",B[2])
#B[2]= [6 5 4 3]
print("B[1][1]=",B[1][1])
#B[1][1]= 9
print("B[1,1:3]",B[1,1:3])
#B[1,1:3] [9 8]
print(np.sort(B)) #对每一行从小打大排序
# [[11 12 13 14]
#  [ 7  8  9 10]
#  [ 3  4  5  6]]

#矩阵的转置
print(np.transpose(B))
print(B.T)
# [[14 10  6]
#  [13  9  5]
#  [12  8  4]
#  [11  7  3]]

print(np.clip(B,5,9))
# [[9 9 9 9]
#  [9 9 8 7]
#  [6 5 5 5]]
#clip(array,min,max)是将比最小值小或者比最大值大的值转换为最小值或最大值

X=np.arange(3,15).reshape((3,4))
print(X.flatten()) #展开成一行
#[ 3  4  5  6  7  8  9 10 11 12 13 14]