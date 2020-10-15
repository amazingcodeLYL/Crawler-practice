import numpy as np
A=np.array([1,1,1])
B=np.array([2,2,2])
print(np.vstack((A,B)))
#vstack按行按列等多种方式合并
#[[1 1 1]
 # [2 2 2]]

print(np.hstack((A,B))) #左右合并
#[1 1 1 2 2 2]

