import tensorflow as tf
# g1=tf.Graph()
# with g1.as_default():
#     v=tf.get_variable("v",initializer=tf.zeros_initializer()(shape=[1]))
# g2=tf.Graph()
# with g2.as_default():
#     v=tf.get_variable("v",initializer=tf.ones_initializer()(shape=[1]))
#
# with tf.Session(graph=g1) as sess:
#     tf.global_variables_initializer().run()
#     with tf.variable_scope("",reuse=True):
#         print(sess.run(tf.get_variable("v")))
#
# with tf.Session(graph=g2) as sess:
#     tf.global_variables_initializer().run()
#     with tf.variable_scope("",reuse=True):
#         print(sess.run(tf.get_variable("v")))

# a=tf.constant([1.0,2.0],name="a")
a=tf.constant([1,2],name="a",dtype=tf.float32)
b=tf.constant([2.0,3.0],name="b")
result=a+b
g=tf.Graph()
# result=a+b
result=tf.add(a,b,name="add")
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(result))


config=tf.ConfigProto(allow_aoft_placement=True,log_device_placement=True)
#ConfigProto可以配置类似并行的线程数、GPU分配策略等参数
#当第一个参数为True时，当某些运算无法被当前
#GPU支持时，可以自动调整到CPU上，而不是报错。第二个参数为True时，日志将会记录每个节点被安排在了哪个设备上以方便调试
sess1=tf.InteractiveSession(config=config) #InteractiveSession可以将产生的会话注册为默认的会话
sess2=tf.Session(config=config)


#使用神经网络解决分类主要分为4 个步骤：
#1.提取问题中实体的特征向量作为伸进网络的输入
#2.定义神经网络结构，并定义如何从神经网络的输入得出输出。这个过程就是前向传播算法。
#3.通过训练数据来调整神经网络中的参数取值。
#4.使用训练好的神经网络来预测未知的数据

#前向传播
#x=tf.matmul(x,w1)
#y=tf.matmul(a,w2) 矩阵乘法


#tensorflow随机生成函数
#tf.random_normal 正态分布  主要参数：平均值、标准差、取值类型
#tf.truncated_normal 正态分布  主要参数：平均值、标准差、取值类型
#tf.random_uniform 平均分布   主要参数：最大值、最小值、取值类型


#tensorflow常数生成函数
#tf.zeros([2,3],int32) 产生全为1的
# tf.ones([2,3],int32) 产生全为0的
# tf.fill([2,3],9) 填充全为9

#w2=tf.Variable(weights.initialized_value()) w2初始为与weights变量相同
#w3=tf.Variable(weights.initialized_value()*2.0) w3初始为weights初始值的两倍


#placeholder
# x=tf.placeholder(tf.float32,shape=(1,2),name="input")
# print(sess.run(y,feed_dict={x:[[0.7,0.9]]}))

#损失函数
#cross_entropy=-tf.reduce_mean(y_*tf.log(tf.clip_by_value(y,le-10,1.0)))
#learning_rate=0.001
#train_step=tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy) 定义了反向传播的优化方法
#优化方法有三种:ttf.train.AdamOptimizer   tf.train.GradientDesentOptimizer  tf.train.MomentumOptimizer


#如何判断一个输出向量和期望的向量有多接近?交叉熵是常用的评判方法之一.交叉熵刻画了两个概率分布之间的距离,他是分类问题
#使用比较广的一种损失函数

#cross_entropy=tf.nn.softmax_cross_entropy_with_logits(y,y_) #可以得到使用了softmax后的交叉熵

#分类问题中,常用均方误差,通过Tensorflow实现均方误差损失函数:
#mse=tf.reduce_mean(tf.square(y_-y))