"""
时间复杂度nlogn【十分详细的题解】https://www.cnblogs.com/0zcl/p/6737944.html
n是外层数组长度
logn是树内元素的时间复杂度（树的高度是logk）
"""
# 请特别特别注意: 初始化大顶堆时 是从最后一个有子节点『(非叶子节点)开始往上』调整最大堆。
# 而堆顶元素(最大数)与堆最后一个数交换后，需再次调整成大顶堆，此时是『从上往下』调整的。
# 不管是初始大顶堆的从下往上调整，还是堆顶堆尾元素交换，
# 每次调整都是从父节点、左孩子节点、右孩子节点三者中选择最大者跟父节点进行交换，交换之后都可能造成被交换的孩子节点不满足堆的性质，
# 因此每次交换之后要重新对被交换的孩子节点进行调整。我在算法中是用一个while循环来解决的
class Solution:
    def sortArray(self, nums):  # List[int]) -> List[int]:
        return self.heapSort(nums)
    # 堆排序
    def heapSort(self, nums):
        n = len(nums)-1
        # 将数组整理成堆（堆有序）
        # 从第一个非叶子节点开始构建初始堆
        # 只需要从 i=(len-1)/2 这个位置开始逐层下移
        for i in range(n//2, -1, -1): # 从下往上（start，建堆的起始点缩小）
            self.build_heap(nums, i, n)

        # 进行n-1次循环完成堆排序
        # 循环不变量：区间 [0, i] 堆有序
        for i in range(n, 0, -1): # 从上往下(high增大)
            # 换出根节点，将其放在最终位置（根节点和最后一个元素交换）
            nums[0], nums[i] = nums[i], nums[0]
            # 在减少了1个元素的无序序列中进行调整（剩余部分调整堆）
            # i-1:逐步减少堆有序的部分
            # 下标 0 位置下沉操作，使得区间 [0, i] 堆有序
            self.build_heap(nums, 0, i-1) # start=0每次都从根节点开始建堆
        return nums

    def build_heap(self, nums, start, high):
        """
        堆排序--建堆（大顶堆，升序）
        :param nums:
        :param start: 【建堆的起点】当前下沉元素的下标
        :param high: [0, high] 是 nums 的有效部分
        :return:
        """
        i = start
        j = 2 * i + 1
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
                j = 2 * i + 1
            else:
                break

nums=[9,2,1,2,3,10,4]
print(Solution().sortArray(nums))