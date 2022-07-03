"""
easy 2021-12-12 哈希
https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/solution/li-yong-tong-pai-xu-de-si-lu-ni-huan-ke-e3t4w/
相关题lc41
"""
class Solution:
    def findDisappearedNumbers(self, nums): #List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            # 要过去的下标 num[i]-1
            # nums[下标]=下标+1
            while nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                # 交换
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] # 左边的会比右边的先赋值

        res = []
        # print(nums)
        for i in range(n):
            # print(i)
            if i+1!=nums[i]:
               res.append(i+1)
        return res

if __name__ == '__main__':
    # nums = [4, 3, 2, 7, 8, 2, 3, 1]
    nums = [1,1]
    print(Solution().findDisappearedNumbers(nums))