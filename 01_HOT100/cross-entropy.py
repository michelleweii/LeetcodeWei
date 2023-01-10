import numpy as np

"""
交叉熵损失函数实现

因此真实分布p(x)和预测分布q(x)的交叉熵就是我们要求的loss损失值.
-( p(x)log(q(x))+ (1-p(x))log(1-q(x))  )
"""
def cross_entropy(a, y):
    """

    :param a: 预测值
    :param y: 真实值
    :return:
    """
    return np.sum(np.nan_to_num(-y*np.log(a)-(1-y)*np.log(1-a)))

# tensorflow version
# loss = tf.reduce_mean(-tf.reduce_sum(y _ *tf.log(y), reduction_indices=[1]))

# numpy version
# loss = np.mean(-np.sum(y_*np.log(y), axis=1))