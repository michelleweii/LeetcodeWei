"""
middle 2022-05-24 双指针（类似三数之和）
更进一步我们发现，当我们在枚举较大数下标 i，并在 [0,i) 范围内逐步减小下标找次大值下标 j 时，
符合条件的 k'必然是从 0 逐步递增（这是由三角不等式nums[k]+nums[j]>nums[i] 所决定的）。
因此，我们可以枚举较大数下标 i 时，在[0,i) 范围内通过双指针，以逐步减少下标的方式枚举 j，
并在遇到不满足条件的 k 时，增大 k 下标。从而找到所有符合条件三元组的个数。
https://leetcode.cn/problems/valid-triangle-number/solution/gong-shui-san-xie-yi-ti-san-jie-jian-dan-y1we/
"""
class Solution:
    def triangleNumber(self, nums): #List[int]) -> int:
        n=len(nums)
        nums.sort()
        res=0
        # 固定最大边i (k+j<i)
        for i in range(n-1,1,-1):
            k,j=0,i-1
            # 两数之和问题
            while k<j:
            # 两数之和大于最大边，他们之间的所有值作为左端点，均可以和右端点构成答案
                if nums[k] + nums[j] > nums[i]:
                    res+=j-k
                    j-=1
                else:
                    # 小于最大边，构不成答案，之后的右端点都需要更大的左端点才有可能继续构成答案
                    k += 1
        return res

if __name__ == '__main__':
    nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
    print(Solution().triangleNumber(nums))
