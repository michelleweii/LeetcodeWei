

# 简单选择排序
def SelectSort(nums):
    n = len(nums)
    for i in range(0,n,1):
        k = i
        # 从无序序列中挑出一个最小的元素
        for j in range(i+1,n,1):
            if nums[k]>nums[j]:
                k = j
        # 最小元素与无序序列第一个元素交换
        nums[k],nums[i]=nums[i],nums[k]
    return nums

if __name__ == '__main__':
    nums = [49,38,65,200,97,76,13,27,49,100,-1]
    print("简单选择：",SelectSort(nums))