"""
middle 2022-05-30 贪心
子序列不要求连续
[图解很容易明白]https://leetcode.cn/problems/increasing-triplet-subsequence/solution/java-tan-xin-by-feilue-usn7/
"""
class Solution:
    def increasingTriplet(self, nums): #List[int]) -> bool:
        if len(nums)<3:return False
        minvalue=float('inf') # 记录的是值
        midvalue=float('inf')
        for x in nums:
            if x>midvalue:return True
            if x<=minvalue:minvalue=x
            else: # x>minvalue
                midvalue=x
        return False

if __name__ == '__main__':
    nums = [2, 1, 5, 0, 4, 6]
    print(Solution().increasingTriplet(nums))
# 三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6