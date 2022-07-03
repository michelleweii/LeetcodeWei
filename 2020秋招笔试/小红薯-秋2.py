def fn1(n,nums):
    dp = [0] * n
    cnt = [1] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    # dp[i]以第i个字符结尾的最多点赞数

    for i in range(2,len(nums)):
        A = dp[i-2] + nums[i] # 选这家
        B = dp[i-1] # 不选这家
        # dp[i] = max(A,B)
        if A>B:
            dp[i] = A
            cnt[i] = cnt[i-2]+1
        else:
            dp[i] = B
            cnt[i] = cnt[i-1]
    # print(dp)
    # print(cnt)
    res = [dp[len(nums)-1]]
    res.append(cnt[-1])
    res = [str(i) for i in res]
    return " ".join(res)


if __name__ == '__main__':
    n = input().strip()
    n = int(n)
    q = input().strip().split()
    nums = [int(i) for i in q]

    # n = 4
    # nums = [1,2,3,1]
    res = fn1(n,nums)
    print(res)