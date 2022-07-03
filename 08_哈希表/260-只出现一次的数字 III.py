"""
middle
哈希表
"""
# 1.先将数组排序，从后往前遍历，先删除最后面一个，数组长度减一，如果数组中还有这个数就再减一，
# 这样就删除掉两个相同的数，如果数组中这个数唯一添加到sum列表里，最后返回这个列表。
class Solution(object):
    def singleNumber(self, nums):
        nums = sorted(nums)
        i = len(nums)
        sum = []
        while i > 0:
            a = nums[i - 1]
            nums.remove(a)
            i -= 1
            if a in nums:
                nums.remove(a)
                i -= 1
            else:
                sum.append(a)
        return sum

def main():
    nums = [1,2,1,3,2,5]
    myResult = Solution()
    print(myResult.singleNumber(nums))

if __name__ == '__main__':
    main()
