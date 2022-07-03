

# 快速排序
def quick_sort(nums, left, right):
    # 当只传来一个元素
    if left>=right:return
    pivot = nums[left]
    i,j = left, right
    while i<j:
        while i<j and nums[j]>=pivot:j-=1 # #从后往前查找，直到找到一个比pivot更小的数
        nums[i] = nums[j] # #将更小的数放入左边
        while i<j and nums[i]<=pivot:i+=1 # #从前往后找，直到找到一个比pivot更大的数
        nums[j] = nums[i] # #将更大的数放入右边
    # 循环结束，i与j相等
    nums[i] = pivot # 待比较数据放入最终位置
    # return i # 回待比较数据最终位置
    quick_sort(nums, left, i-1)
    quick_sort(nums, i+1, right)
    # print(nums)

if __name__ == '__main__':
    nums = [2,3,1]
    quick_sort(nums, 0, len(nums)-1)
    print("nums ", nums)