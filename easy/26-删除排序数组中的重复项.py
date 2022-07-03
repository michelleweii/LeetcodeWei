# 此题gg，用while！！！！！！！！
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for i in range(1,len(nums)):
#             # for的机制是一开始就定下i到len(nums)
#             # 之后每次循环不会去重新计算len。
#             """
#             所以我这里为什么越界了呢？
#             因为一开始拿个length去接收固定的数组长度，
#             然后设置i从0到length的遍历，但是这个数组长度是会变的，
#             但我不该固定length的长度，因为删除元素的时候数组长度
#             是会改变的。
#             """
#             print(i)
#             if nums[i-1]==nums[i]:
#                 nums.remove(nums[i-1])
#             else:
#                 continue
#         print(nums)
#         return len(nums)

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        i = 0
        while i < len(A)-1:
            if A[i] == A[i+1]:
                A.remove(A[i])
            else:
                i += 1
        return len(A)

def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    myResult = Solution()
    print(myResult.removeDuplicates(nums))

if __name__ == '__main__':
    main()


"""
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        return n - len([nums.pop(i) for i in range(n -1, 0, -1) if nums[i] == nums[i - 1]])
"""


"""
class Solution:
    def removeDuplicates(self, nums):

        k = 0
        for i, num in enumerate(nums):
            if k < 1 or num != nums[k - 1]:
                if i != k:
                    nums[k] = num 
                    k += 1
                else:
                    k += 1

        return k
"""