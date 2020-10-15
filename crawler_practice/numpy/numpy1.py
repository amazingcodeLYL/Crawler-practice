import numpy as np
array = np.array([[1,2,3],[2,3,4]])
print(array)
print('number of dim:',array.ndim)#维度

print('shape:',array.shape) #行数和列数

print('size:',array.size) #元素个数

a=np.array([2,23,4])
print(a)

a=np.array([2,23,4],dtype=np.int)
print(a.dtype)

a=np.array([2,23,4],dtype=np.int32)
print(a.dtype)


a=np.array([2,23,4],dtype=np.float)
print(a.dtype)
#float64

a=np.array([[2,23,4],[2,32,4]])
print(a)
#[[ 2 23  4]
# [ 2 32  4]]


a=np.zeros((3,4))
print(a)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

a=np.ones((3,4),dtype=np.int)
print(a)

# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

a=np.empty((3,4))
print(a)

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

#创建连续数组
a=np.arange(10,20,2)
print(a)
#[10 12 14 16 18]

