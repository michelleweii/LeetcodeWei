"""
easy
哈希表
"""
import collections
class Solution(object):
    def findLHS(self, nums):
        ans = 0
        dict_nums = collections.Counter(nums)
        print(dict_nums) # Counter({2: 3, 3: 2, 1: 1, 5: 1, 7: 1})
        for num in nums:
            if num+1 in dict_nums:
                # print(dict_nums[num])
                # print(dict_nums[num+1])
                ans = max(ans, dict_nums[num]+dict_nums[num+1])
                # print(ans)
        return ans


if __name__ == '__main__':
    nums = [1,3,2,2,5,2,3,7]
    myResult = Solution()
    print(myResult.findLHS(nums))