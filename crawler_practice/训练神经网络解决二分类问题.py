import tensorflow as tf
from numpy.random import RandomState
#定义训练数据batch大小
batch_size=8
#定义神经网络参数
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x=tf.placeholder(tf.float32,(None,2),name="x-input")
y_=tf.placeholder(tf.float32,(None,1),name="y-input")

#定义前向传播过程
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

#定义损失函数和反向传播的算法   0.001为学习率
cross_entropy=-tf.reduce_mean(y_*tf.log(tf.clip_by_value(y,1e-10,1.0)))
train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

#随机生成一个模拟数据集
rdm=RandomState(1)
dataset_size=128
X=rdm.rand(dataset_size,2)
Y=[[int(x1+x2<1)] for (x1,x2) in X]
with  tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(w1))
    print(sess.run(w2))

    STEPS=5000
    for i in range(STEPS):
        #每次选取batch_size个样本训练
        start=(i*batch_size)%dataset_size
        end=min(start+batch_size,dataset_size)
        #通过选取的样本训练神经网络并更新参数
        sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
        if i%1000==0:
            #每隔一段时间计算在所有数据上的交叉熵并输出
            total_cross_entropy=sess.run(cross_entropy,feed_dict={x:X,y_:Y})
            print("After %d training step(s),cross_entropy on all data is %g"%(i,total_cross_entropy))
    print(sess.run(w1))
    print(sess.run(w2))


#定义神经网络的过程分为3个步骤:
#1.定义神经网络结构和前向传播的输出结果
#2.定义损失函数以及选择反向传播优化的算法
#3.生成会话并在训练数据上反复运行反向传播优化算法