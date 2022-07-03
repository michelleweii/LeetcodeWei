def bank(coordinate,money):
    dp = [0 for _ in range(len(coordinate))]
    # print(dp)
    dp[0] = money[0]
    # dp[i]表示坐标为i的店铺获取最大的收益
    # print(dp)
    for i in range(1,len(coordinate)):
        # 选这家
        index = find(coordinate,coordinate[i]-d-1)
        # print(i,index)
        A = money[i] + dp[index]
        # 不选这家
        B = dp[i-1]# 不选这家
        # print(B)
        dp[i] = max(A,B)
    print(dp)

def find(coordinate,val): # val=3
    for i in range(len(coordinate)):
        if val==coordinate[i]:
            return i
    for i in range(len(coordinate)):
        if val<coordinate[i]:
            return i-1


if __name__ == '__main__':
    n = 6  # 银行数量
    d = 3  # 约定距离
    coordinate = [1, 3, 4, 6, 10]
    money = [1, 5, 8, 4, 3]
    bank(coordinate,money)