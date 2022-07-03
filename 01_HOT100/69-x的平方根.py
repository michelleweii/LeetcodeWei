"""
easy 2022-02-27 二分
# 二分法、梯度下降法、牛顿法求解根号（Python）
# (这个@!) https://blog.csdn.net/weixin_41744192/article/details/123543067
# 【牛顿迭代法】https://leetcode-cn.com/problems/sqrtx/solution/niu-dun-die-dai-fa-by-loafer/
# 【二分法】https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
"""
class Solution:
    # 梯度下降，定义损失函数!!必会！！
    # 求根号2，即求 x^2-2=0 的根，即求 f(x)=(x^2-n)^2 取极小值时x的取值。求导后另其导数=0，所求的x即为极值点。
    # 当n=2时，求根号2
    def gradient_descent(self, n):
        # 随机初始化
        x = n # x = float(random.randint(1, 100))
        lr = 0.00001 # 学习率
        # loss = [] # 记录损失
        # 损失阈值
        while (abs(x ** 2 - n) > 0.0000000001): # 损失函数，误差
            # x(n+1) = x(n) - lr * g(x(n))
            x = x - lr * 4*x*(x**2-n)
            # 记录损失  loss.append((x ** 2 - n) ** 2)
        return x

    # 牛顿法，方法使用函数的泰勒级数的前2项来寻找方程的根。
    # 把 f(x) 在 点x_0 的某邻域内展开成泰勒级数，
    # 得到牛顿迭代法的一个迭代关系式：x_(n+1)=x_n - f(x_n)/f`(x_n)
    # 假设方程f(x)=x^2-n，得到
    # x_(n+1)=(x_n+a/x_n)/2
    def newton(self, n):
        x = n  # 随便猜一个近似值x
        while x * x > n:
            x = (x + n / x) / 2  # 牛顿迭代法, 不断令 x 等于 x 和 a/x 的平均数
        return x  # 迭代个六七次后 x 的值就已经相当精确了
        # 所得x即为根号n的值

    # 二分
    def sqrt_bi(self, x: int) -> int:
        if not x:return x
        if x==1:return x
        l,r = 1, x//2
        while l<r:
            mid = (l+r+1)//2
            if mid*mid<=x:
                l=mid
            else:
                r=mid-1
        return r

if __name__ == '__main__':
    x = 9 # 8,return 2容易理解
    print("二分法：", Solution().sqrt_bi(x)) # 二分
    print("梯度下降：", Solution().gradient_descent(x))
    print("牛顿法：", Solution().newton(x))
