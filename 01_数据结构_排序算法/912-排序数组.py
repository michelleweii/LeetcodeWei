"""
middle 2021-12-23 排序算法【基础中的基础！】
十大排序算法
https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
"""
class Solution:
    def sortArray(self, nums): #List[int]) -> List[int]:
        return self.heapSort(nums)

    # 堆排序
    def heapSort(self, nums):
        n = len(nums)-1

        # 将数组整理成堆（堆有序）
        # 从第一个非叶子节点开始构建初始堆
        # 只需要从 i=(len-1)/2 这个位置开始逐层下移
        for i in range(n//2, -1, -1):
            self.Sift(nums, i, n)

        # 进行n-1次循环完成堆排序
        # 循环不变量：区间 [0, i] 堆有序
        for i in range(n, 0, -1):
            # 换出根节点，将其放在最终位置（根节点和最后一个元素交换）
            nums[0], nums[i] = nums[i], nums[0]
            # 在减少了1个元素的无序序列中进行调整（剩余部分调整堆）
            # i-1:逐步减少堆有序的部分
            # 下标 0 位置下沉操作，使得区间 [0, i] 堆有序
            self.Sift(nums, 0, i-1)
        return nums


    def Sift(self, nums, low, high):
        """
        堆排序--建堆（大顶堆，升序）
        :param nums:
        :param low: 当前下沉元素的下标
        :param high: [0, high] 是 nums 的有效部分
        :return:
        """
        i = low
        j = 2*i + 1
        # temp存储父节点
        # temp = nums[i]
        # 与孩子节点做比较，建堆
        while (j <= high):
            # 找到最大的那个孩子
            if (j < high and nums[j] < nums[j + 1]):
                j += 1
            # 父亲和孩子交换
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                # 继续向下调整
                i = j
                j = 2*i + 1
            else:
                break
        # nums[i]=temp



if __name__ == '__main__':
    # nums =  [5,2,3,1] # [1,2,3,5]
    nums = [5, 1, 1, 2, 0, 0] # [0,0,1,1,2,5]
    print(Solution().sortArray(nums))

    # 升序采用大顶堆，降序采用小顶堆
    # 从最后一个非叶子结点开始，从左至右，从下至上进行调整
