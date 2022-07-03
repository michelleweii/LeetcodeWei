# 排序文章 https://mp.csdn.net/mp_blog/creation/editor/88017405

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
    quick_sort(nums, left, i-1) # 每次递归结束，右边都比pivot小
    quick_sort(nums, i+1, right) # 左边都比pivot大
    # print(nums) 原地更改

nums=[9,2,1,2,3,10,4]
quick_sort(nums,0,len(nums)-1)
print(nums)