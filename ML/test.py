import tensorflow as tf
sess = tf.Session()
a = tf.constant(10)
b = tf.constant(22)
print(sess.run(a + b))
32

>>> import tensorflow as tf
>>> sess = tf.Session()
>>> a = tf.constant(10)
>>> b = tf.constant(22)
>>> print(sess.run(a + b))
32


import tensorflow as tf
sess = tf.Session()
a = tf.constant(10)
b = tf.constant(22)
print(sess.run(a + b))
c = u'\u9e21\u5e74\u5927\u5409\uff0c\u65b0\u5e74\u5feb\u4e50\uff01'
print(c)


>>> import tensorflow as tf
>>> sess = tf.Session()
>>> a = tf.constant(10)
>>> b = tf.constant(22)
>>> print(sess.run(a + b))
32
>>> c = u'\u9e21\u5e74\u5927\u5409\uff0c\u65b0\u5e74\u5feb\u4e50\uff01'
>>> print(c)
����󼪣�������֣�
>>> 



import tensorflow as tf

# ����һ������ op, ����һ�� 1x2 ����. ��� op ����Ϊһ���ڵ�
# �ӵ�Ĭ��ͼ��.
#
# �������ķ���ֵ����ó��� op �ķ���ֵ.
matrix1 = tf.constant([[3., 3.]])

# ��������һ������ op, ����һ�� 2x1 ����.
matrix2 = tf.constant([[2.],[2.]])

# ����һ������˷� matmul op , �� 'matrix1' �� 'matrix2' ��Ϊ����.
# ����ֵ 'product' �������˷��Ľ��.
product = tf.matmul(matrix1, matrix2)

# ����Ĭ��ͼ.
sess = tf.Session()

# ���� sess �� 'run()' ������ִ�о���˷� op, ���� 'product' ��Ϊ�÷����Ĳ���. 
# �����ᵽ, 'product' �����˾���˷� op �����, ���������򷽷�����, ����ϣ��ȡ��
# ����˷� op �����.
#
# ����ִ�й������Զ�����, �Ự���𴫵� op �����ȫ������. op ͨ���ǲ���ִ�е�.
# 
# �������� 'run(product)' ������ͼ������ op (�������� op ��һ������˷� op) ��ִ��.
#
# ����ֵ 'result' ��һ�� numpy `ndarray` ����.
result = sess.run(product)
print result
# ==> [[ 12.]]

# �������, �رջỰ.
sess.close()