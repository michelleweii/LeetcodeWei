"""
middle 哈希表
"""
class Solution(object):
    def threeSum(self, nums):
        rs = []
        for i in range(len(nums)):
            temp = 0-nums[i]
            hash_map = {}
            # 现在是两数之和
            for j in range(i+1,len(nums)):
                if nums[j] not in hash_map:
                    hash_map[temp-nums[j]]=j
                else:
                    ans = []
                    ans.append(nums[i])
                    ans.append(nums[hash_map[nums[j]]])
                    ans.append(nums[j])
                    if sorted(ans) not in rs:
                        rs.append(sorted(ans[:]))
        return rs

if __name__ == '__main__':
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print(Solution().threeSum(nums))
    # print([-4, 4, 0] == [-4, 4, 0])