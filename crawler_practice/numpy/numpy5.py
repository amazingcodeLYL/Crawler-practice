import numpy as np
A=np.arange(12).reshape((3,4))
print(A)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
B=A.copy()
print("B=",B)
# B= [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

#纵向分割
print(np.split(A,2,axis=1))
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]

#横向分割
print(np.split(A,3,axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

