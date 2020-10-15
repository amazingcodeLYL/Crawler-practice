# from urllib.request import urlopen
# html=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)

import tensorflow as tf
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x=tf.constant([[0.7,0.9]])
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    sess.run(w1.initial_value)
    sess.run(w2.initial_value)
    print(sess.run(y))
