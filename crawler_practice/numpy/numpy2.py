import numpy as np
a=np.array([10,20,30,40]) #[10 20 30 40]
b=np.arange(4) #[0 1 2 3]
c=a-b
print(c) #[10 19 28 37]
c=a+b
print(c) #[10 21 32 43]
c=a*b
print(c) #[  0  20  60 120]
c=b**2
print(c) #[0 1 4 9]
c=10*np.sin(a)
print(c) #[-5.44021111  9.12945251 -9.88031624  7.4511316 ]
print(b<3) #[ True  True  True False]

e=np.array([[1,1],[0,1]])
f=np.arange(4).reshape((2,2))
print(e)
# [[1 1]
#  [0 1]]
print(f)
# [[0 1]
#  [2 3]]

c_dot=np.dot(e,f) #矩阵乘法
print(c_dot)
# [[2 4]
#  [2 3]]

#另一种表示方法
c_dot_2=e.dot(f)
print(c_dot_2)

r_a=np.random.random((2,4)) #随机生成一个矩阵值
print(r_a)
# [[0.42132264 0.22771785 0.44466418 0.11913662]
#  [0.71617876 0.48510079 0.50271546 0.88637848]]

a_sum=np.sum(r_a)
print(a_sum) #2.9857142667039276
a_min=np.min(r_a)
print(a_min) #0.0009651795627688697
a_max=np.max(r_a)
print(a_max) #0.6642412178791747

#对行或者列进行运算，设置参数axis=0时，以列为单位
#axis=1时，以行为单位
print("sum=",np.sum(r_a,axis=1))
#sum= [1.92376688 1.9235414 ]
print("min=",np.min(r_a,axis=0))
#min= [0.50175284 0.56405502 0.04557037 0.295479  ]
print("max=",np.max(r_a,axis=1))
#max= [0.72859575 0.56405502]