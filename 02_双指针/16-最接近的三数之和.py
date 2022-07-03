"""
middle 2021-12-30 反向双指针 o(n^2)
重点理解i,left,right的位置
1、在数组 nums 中，进行遍历，每遍历一个值利用其下标i，形成一个固定值 nums[i], 枚举剩余部分left&right。
2、根据 sum = nums[i] + nums[start] + nums[end] 的结果，判断 sum 与目标 target 的距离，如果更近则更新结果 ans
3、同时判断 sum 与 target 的大小关系，因为数组有序，如果 sum > target 则 end--，
如果 sum < target 则 start++，如果 sum == target 则说明距离为 0 直接返回结果

题解：https://leetcode-cn.com/problems/3sum-closest/solution/hua-jie-suan-fa-16-zui-jie-jin-de-san-shu-zhi-he-b/
"""
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort() # [-4, -1, 1, 2]
        # 有3个变量
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            # 剪枝, 重复的数字不需要再计算
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 每次固定一个数nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                cur = nums[i]+nums[left]+nums[right]
                if cur == target:return target
                # 这一句是重点不明白的
                # 当前的三个数cur更接近target
                if abs(res-target)>abs(cur-target):
                    res = cur

                # 如果当前值>target,说明值大了，right左移
                if cur>target:
                    right-=1

                # else，left右移动
                elif cur<target:
                    left+=1

        return res

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))