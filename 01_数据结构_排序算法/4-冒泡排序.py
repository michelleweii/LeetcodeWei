


# 冒泡排序
def BubbleSort(nums):
    n = len(nums)-1 # 从最后一个元素开始，然后n-1,n-2,因为此时已经有了最大的冒到最后。
    for i in range(n,-1,-1): # 控制未排序的长短，已经冒上来的（位于最后）不再做处理
        flag = 0
        for j in range(1,i+1,1): # 对未排序的部分，进行两两交换比较
            if(nums[j-1]>nums[j]):
                nums[j-1],nums[j] = nums[j],nums[j-1]
                flag = 1

        if(flag==0): # 没有数据进行交换
            return nums

if __name__ == '__main__':
    nums = [49,38,65,200,97,76,13,27,49,100,-1]
    print("冒泡：",BubbleSort(nums))
