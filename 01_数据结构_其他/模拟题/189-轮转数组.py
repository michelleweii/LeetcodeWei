"""
middle 2021-12-09
将数组中的元素向右轮转 k 个位置——切片
https://leetcode-cn.com/problems/rotate-array/solution/python3-qie-pian-jie-jue-by-westcott-36jh/
"""
class Solution:
    def rotate(self, nums, k):# List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # k需要预先除列表长度取余，因为移动n次相当于没动
        nums[:] = nums[n-k:n]+nums[0:n-k]
        """
        切片的用法：复制列表时，需要用代码中所示的用法（注意左边nums括号中的冒号，创建了一个新的切片）将旧列表的值赋给新列表，
        如果直接 list_1 = list_2，两个变量只是指向同一个列表，并非创建了一个新的。
        """

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # [5,6,7,1,2,3,4]
    print(Solution().rotate(nums, k))