# 梯度下降求x方最小值

# https://gitee.com/wanduoz/gradient_descent/tree/master
# https://zhuanlan.zhihu.com/p/397069608


# 一般性
# https://blog.csdn.net/qq_45572853/article/details/122289995
# https://blog.csdn.net/le000426/article/details/120761460
# 梯度下降算法求解f(x)=x^2-4x-5的最小值
def gradient(x):  # 计算x位置的梯度
    # 求导
    return 2.0*x-4  # 函数f(x)=x^2-4x-5的梯度

def gradient_descent():  # 梯度下降的过程中，函数返回迭代完成后，f(x)取得最小值时，x的值
    x = 1.0  # 从位置0开始迭代
    iteration_num = 8000  # 迭代次数
    alpha = 0.001  # 迭代速率
    for i in range(0, iteration_num):
        print("%d iteration x=%1f gradient(x)=%1f" % (i, x, gradient(x)))
        x = x-alpha*gradient(x)
    return x


# https://blog.csdn.net/m0_63794226/article/details/125289189

#  8 # 函数 f(x)=x^2
#  9 def f(x): return x ** 2
# 10
# 11
# 12 # 一阶导数:dy/dx=2*x
# 13 def fd(x): return 2 * x
# 14
# 15
# 16 def GD(x_start, df, epochs, lr):
# 17     xs = np.zeros(epochs+1)
# 18     w = x_start
# 19     xs[0] = w
# 20     for i in range(epochs):
# 21         dx = df(w)
# 22         # 权重的更新
# 23         # W_NEW = W — 学习率(learning rate) x 梯度(gradient)
# 24         w += - lr * dx
# 25         xs[i+1] = w
# 26     return xs
# 27
# 28
# 29 # 超参数(Hyperparameters)
# 30 x_start = 5    # 起始权重
# 31 epochs = 25    # 执行周期数
# 32 lr = 0.1       # 学习率
# 33
# 34 # 梯度下降法, 函数 fd 直接当参数传递
# 35 w = GD(x_start, fd, epochs, lr=lr)

if __name__ == '__main__':
    gradient_descent()

