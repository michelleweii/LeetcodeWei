"""
middle 2021-12-15 dfs递归
# 给定一个整数 n, 返回从 1 到 n 的字典顺序。
# 给定 n = 13，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9]
【看看树长什么样】https://leetcode-cn.com/problems/lexicographical-numbers/solution/386-zi-dian-xu-pai-shu-o1-kong-jian-fu-z-aea2/

思路：
1、将 h 位的所有整数看做 h 层的 k 叉树（k≤10,0~9）;
2、[1,n] 范围内的所有整数的字典序实际上就是这棵 k 叉树的先序遍历顺序;
"""
class Solution:
    # 方法一：dfs
    # 空间复杂度：O(n)，为递归栈占用的空间
    def lexicalOrder(self, n):
        self.res = []
        self.n = n
        for i in range(1, 10):
            self.dfs(i) # 开始第一层，第1棵树、第2棵树、、、第9棵树
        return self.res

    # 递归, i为以i开头, n为不大于n, res为保存结果的数组
    def dfs(self, num):
        if num>self.n:return
        self.res.append(num) # 1
        # 开始第二层，第二层可以从0开始
        for next_level in range(num*10, num*10+10):
            # 以1为开始node，下面接0-9，那么取值范围就是10~19
            self.dfs(next_level)

    # 方法二：迭代
    # 将DFS改为迭代需要额外的栈空间。注意到当前搜索的数 num 本身就能反映出每一层递归的状态，例如当前搜索至 123，
    # 我们知道当前层遍历至 3，上一层遍历至 2，再上一层遍历至 1。
    # 如果我们需要返回上一层，只需要令 num //= 10 即可。
    # 空间复杂度：O(1)，答案数组所占空间不计入
    def lexicalOrder_2(self, n):
        cur = 1
        ans = []
        for i in range(n):
            ans.append(cur)
            if cur*10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur%10 == 0:
                    cur //= 10
        return ans

    """
    1、如果一个数乘以十以后没有超过n，那它后面紧挨着的应该是它的十倍，比如1,10,100。
    2、如果不满足1，那就应该是直接加一，比如n为13的时候，前一个数为12，120超过了n，
    那接着的应该是13。但是这里要注意如果前一个数的个位已经是9或者是它就是n了，那就不能加一了，
    比如 n = 25，前一个数为19，下一个数应该为2而不是19+1=20。25的下一个也没有26了。
    3、如果不满足2，比如19后面应该接2而不是20，这时候应该将19除以10再加一，比如n=500，
    399的下一个应该是4，那就是除以十，个位还是9，继续除以10，得到3，加一得到4。

    将上面的过程整理成代码就可以了，循环的次数就是n，也就是总个数。
    """

if __name__ == '__main__':
    n = 13
    print(Solution().lexicalOrder(n))