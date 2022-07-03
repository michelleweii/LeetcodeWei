"""
middle 2021-09-02 能不能用双指针呢？
"""
# 字典，元组，set的使用

class Solution(object):
    def fourSum(self, nums, target):
        lens = len(nums)
        nums.sort() # 说明：解集不能包含重复的子集
        res = set()
        dicinum = {}
        # 先求数字的两两之和，存到一个list里。
        # 再两次for循环，将4sum转为2sum
        # 2sum时，在list中找是否存在元素。
        for i in range(lens-1):
            for j in range(i+1,lens):
                key = nums[i]+nums[j]
                if key not in dicinum:
                    dicinum[key]= [(i,j)]
                else:
                    dicinum[key].append((i,j))
        # print(dicinum)

        for i in range(2,lens-1):
            # 转为3数之和
            for j in range(i+1,lens-2):
                # 转为2数之和
                diff2 = target - nums[i] - nums[j]
                if diff2 in dicinum:
                    for index in dicinum[diff2]:
                        # print(index) #(4, 5) (2, 5)
                        if index[0]>j: # 不能重复取
                            res.add((nums[i], nums[j], nums[index[0]], nums[index[1]]))
        print(res)
        # {(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)}
        return [list(i) for i in res]
        # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]



if __name__ == '__main__':
    # nums = [0,0,0,0]
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums,target))


