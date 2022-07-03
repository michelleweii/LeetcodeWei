"""
middle 2021-12-14 dp
【一般思路】https://leetcode-cn.com/problems/unique-binary-search-trees/solution/by-trophy-1-0u4f/
题目：给定整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
dp[i] 表示i个元素的二叉搜素树有多少种，以某个节点为根结点的树形态数 = 左子树的形态数量 * 右子树的形态数量
https://leetcode-cn.com/problems/unique-binary-search-trees/solution/dong-tai-gui-hua-python-bu-tong-de-er-ch-jpog/
"""
# 题目就是 卡特兰数 公式
# g(n)是n棵树，f(n)是以i为树根有多少形态的树
"""
假设n个节点存在二叉排序树的个数是G(n)，令f(i)=以i为根的二叉搜索树的个数；
即有: G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
n为根节点，当i为根节点时，其左子树节点个数为[1, 2, 3, ..., i-1]，右子树节点个数为[i+1, i+2, ...n]，
所以当i为根节点时，其左子树节点个数为(i-1)个，右子树节点为(n-i)，即f(i) = G(i-1) * G(n-i),
上面两式可得: G(n) = G(0)*G(n-1) + G(1)*(n-2) + ... + G(n-1)*G(0)

举个例子，dp[5]指的就是5个连续数字可以组成的二叉搜索树的个数
这5个数字不一定是[1,2,3,4,5]，也可以是[7,8,9,10,11]，只要是i个连续的数，就一定可以排列出dp[i]个二叉搜索树
"""
# 为什么是乘而不是加呢？
class Solution:
    def numTrees(self, n):
        dp = [0]*(n+1) # dp[i] 表示i个元素的二叉搜素树有多少种
        dp[0], dp[1] = 1, 1
        # 将1至n分别作为根结点时的数量累加即为结果 dp[n]
        for i in range(2, n+1):
            # 将除去根结点之外的（n-1）个子节点做排列组合
            for j in range(i):
                # G(n) = G(0)*G(n-1) + G(1)*(n-2) + ... + G(n-1)*G(0)
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]

if __name__ == '__main__':
    # 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
    # 二叉搜索树:左边比它大，右边比它小
    n = 3
    print(Solution().numTrees(n))