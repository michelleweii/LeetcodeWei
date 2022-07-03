"""
2022-03-01 hard 回溯
全排列，返回第k个排列
https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
https://leetcode-cn.com/problems/permutation-sequence/solution/shou-hua-tu-jie-jing-dian-de-dfshui-su-shu-xue-gui/
"""
#### 核心思想 ####
# 所求排列 一定在叶子结点处得到，进入每一个分支，可以根据已经选定的数的个数，进而计算还未选定的数的个数，然后计算阶乘，就知道这一个分支的 叶子结点 的个数：
# 如果 k 大于这一个分支将要产生的叶子结点数，直接跳过这个分支，这个操作叫「剪枝」；
# 如果 k 小于等于这一个分支将要产生的叶子结点数，那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解。
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #     // 方法1：使用回溯法的思路思考，则每当选择一个数加入排列时，可以计算出剩下的数还有多少种排列的可能，
        #     // 即可以计算出当前被选择的数的排列总数，设用 remain_fac 表示， remain_fac = 剩下的待选择的数的阶乘。
        #     // 然后将 remain_fac 与 k 进行大小比较，若小于 k ，则说明所要求的第 k 个排列不在以 当前选定的数 为开头的所有排列中，直接跳过
        #     // 一次递归到底就能找到 第 k 个排列

        def dfs(n, k, index, path):
            if index == n:
                return

            cnt = factorial[n-1-index] # 剩下的数的全排列的个数（树枝层面剩下的数）
            print(index,"阶乘", factorial, n-1-index) # 选1的时候，剩余2个数
            # 比如1,2,3
            # 选1的话，下一层2,3，剩余2种全排列（12,13）
            # 下一层选2，只剩1种全排列（123）
            # cnt记录的是剩余的数量
            print('cnt', cnt)

            for i in range(1, n + 1):
                if used[i]: # 跳过已使用的数
                    continue
                if cnt < k: # 剩下的数的全排列个数小于当前 k ，说明第 k 个排列肯定不在当前的递归子树中，直接跳过该递归
                    # print(cnt, k) # 2,3
                    k -= cnt # 剪枝
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, index + 1, path)
                # 注意：这里要加 return，后面的数没有必要遍历去尝试了
                # 因为是一次递归直接到叶子，所以不需要还原状态
                return

        if n == 0:
            return ""

        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])

############################################################################################################################
    # # 普通回溯超出时间范围
    # def getPermutation_pure(self, n: int, k: int) -> str:
    #     self.res = ""
    #     self.path = []
    #     nums = [str(i) for i in range(1, n+1)]
    #     used = [0]*n
    #     self.k = k
    #     self.dfs(nums, used)
    #     return self.res
    #
    # def dfs(self, nums, used):
    #     if not self.k:
    #         return
    #
    #     if len(self.path)==len(nums) and self.k:
    #         # self.res.append(''.join(self.path[:]))
    #         # ['123', '132', '213', '231', '312', '321']
    #         self.k-=1
    #         if self.k==0:
    #             self.res = ''.join(self.path[:])
    #             return
    #     # 不会有重复的元素，不需要剪枝
    #     for i in range(len(nums)):
    #         if used[i]==1:continue
    #         self.path.append(nums[i])
    #         used[i]=1
    #         self.dfs(nums,used) # 取过的元素不能再取
    #         used[i]=0
    #         self.path.pop()

if __name__ == '__main__':
    n = 3
    k = 3
    # '213'
    print(Solution().getPermutation(n,k))