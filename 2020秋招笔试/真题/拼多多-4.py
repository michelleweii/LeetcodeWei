def isLegal(x,y):
    NUM = 1e9+7
    sumx = [] # x的辅助栈，x中左括号比右括号多了几个
    sumy = [] # y的辅助栈
    n = len(x)
    m = len(y)
    # 只要左括号数量>=右括号数量，即为合法的圆括号
    # 初始化sumx
    sumx.append(0)
    for i in range(1,n+1):
        sumx.append(sumx[i-1] + (1 if x[i-1]=='(' else -1))

    # 初始化sumy
    sumy.append(0)
    for i in range(1,n+1):
        sumy.append(sumy[i-1] + (1 if y[i-1]=='(' else -1))


    if sumx[-1] + sumy[-1] != 0:
        #说明x,y中的左右括号个数不相等
        return 0

    # 构建dp
    # 这样构建会浅拷贝，造成！
    # row = [0]*(n+1)
    # dp = [row]*(m+1) # 从x中选0个，选1个，选2个，选3个。共有4种可能
    # print(dp)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)] # 这样不会浅拷贝
    for j in range(1,m+1):
        if sumx[j]<0: break
        dp[j][0] = 1

    for i in range(1,n+1):
        if sumy[i]>=0:
            dp[0][i] = 1

    # print(dp)
    for i in range(1,n+1):
        for j in range(1,m+1):
            # if (sumy[i]+sumy[j])<0:continue # 我有这句话为什么是错的呢？
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%NUM
    print(dp)
    # [[0, 1, 1, 0], [1, 2, 3, 3], [1, 3, 6, 9], [1, 4, 10, 19]]
    print(dp[n][m])

if __name__ == '__main__':
    str1 = '(()'
    str2 = '())'
    isLegal(str1,str2)
