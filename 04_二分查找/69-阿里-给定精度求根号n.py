# 输入一个整数N，输出sqrt(N)，精度为0.001
# 二分法
def binarySearch(n,eps):
    if n<0: return -1
    low = 0
    high = n
    mid = (low+high)/2
    while abs(mid*mid-n)>eps:
        if mid*mid>n:
            high = mid
        else:
            low = mid
        mid = (low+high)/2
    return mid

# 牛顿法
# 通项公式：x(n+1)=(x(n)+p/x(n))*0.5
# p为要开根号的数字
def newton(n,eps):
    x = n
    y = 0
    while(abs(x-y)>eps):
        y = x
        x = 0.5*(x+n/x)
    return x

if __name__ == '__main__':
    n = 5
    eps = 0.0001
    print(n**0.5) # 2.23606797749979
    print(binarySearch(n,eps)) # 2.2360610961914062
    print(newton(n,eps)) # 2.236067977499978