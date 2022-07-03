"""
hard
"""
class Solution:
    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1]*n, 0)
        return self.res

    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index+1)

    def valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[n]-nums[i]) == n-i:
                return False
        return True

if __name__ == '__main__':
    n = 4
    print(Solution().totalNQueens(n))