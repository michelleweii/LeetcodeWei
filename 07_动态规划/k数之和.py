# https://blog.csdn.net/RincolF/article/details/123834328
# https://harrytsz.blog.csdn.net/article/details/101273628?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-1-101273628-blog-87901537.pc_relevant_aa&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-1-101273628-blog-87901537.pc_relevant_aa&utm_relevant_index=1
# https://blog.csdn.net/JiuZhang_ninechapter/article/details/109672109

# 状态定义：dp[i][k][t]，表示从0遍历到A[i]后找到的k个元素之和为t的情况的总数。
def func(nums,k,target):
    n=len(nums)
    # int[][][] f = new int[n + 1][k + 1][target + 1];
    dp=[[[0]*(target+1) for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0][0]=1
    # print(dp)
    for i in range(1,n+1):
        for j in range(k+1): # 只走到i，所以pick的数字个数j<i
            for t in range(target+1):
                if nums[i-1]>t:
                    # print(nums[i-1])
                    dp[i][j][t]=dp[i-1][j][t] # 都>t了，所以和不可能为t
                else:
                    dp[i][j][t]+=dp[i-1][j-1][t-nums[i-1]]
    # print(dp)
    return dp[n][k][target]

if __name__ == '__main__':
    nums=[1, 2, 3, 4]
    k = 2
    target = 5
    print(func(nums,k,target))