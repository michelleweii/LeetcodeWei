"""
middle 2021-12-25 快速排序【面试高频】
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/jie-jue-kthwen-ti-de-liang-chong-fang-sh-xvjl/
(评论区快排模板一样)https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
思路：
1、每次patition对数组进行一次划分，确定枢轴的最终位置。
2、若本次划分的结果恰好使枢轴出现在第k个位置上，即所求的第k小的元素(第k大元素也可以使用
## 时间复杂度 O(n) 分治思想!!!
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        n = len(nums)
        if not nums or k>n:return -1
        # 转求index=n-k
        return self.quick_sort(nums, 0, n-1, n-k)

    # 快速排序，逆序
    def quick_sort(self, nums, left, right, index):
        # 递归出口，仅剩一个元素
        if left>=right:return nums[left]# 如果原地更改的话，就return
        i,j = left, right
        pviot = nums[i] # 基准点
        while i<j:
            # 逆序<=，正序>=
            while i<j and nums[j]>=pviot:
                j-=1
            nums[i] = nums[j]
            while i<j and nums[i]<=pviot:
                i+=1
            nums[j] = nums[i]
        nums[i] = pviot
        # i是分割点
        # 直接快速排序会超过时间限制
        # 若位置小于index，则在左边找
        if index<i: return self.quick_sort(nums,left,i-1,index)
        # 若位置大于index，则在右边找
        elif index>i: return self.quick_sort(nums,i+1,right,index)
        # 若刚好相同，则直接返回即可
        else: return nums[i]

if __name__ == '__main__':
    # nums = [3,2,1,5,6,4]
    # k = 2 # 5
    # nums = [1]
    # k = 1
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4 #4
    myResult = Solution()
    print(myResult.findKthLargest(nums, k))
