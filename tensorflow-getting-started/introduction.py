import tensorflow as tf

sess = tf.Session()

hello = tf.constant('Hello Sharon Mordechai!')
print(sess.run(hello))

a = tf.constant(20)
b = tf.constant(5)
print('a + b = {0}'.format(sess.run(a + b)))
