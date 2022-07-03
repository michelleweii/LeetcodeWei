
def insertionSort(nums):
    for i in range(1, len(nums)):
        pos = nums[i]
        j = i-1
        while j >= 0 and pos < nums[j]:
            # print(i, nums[j+1], nums[j])
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = pos

if __name__ == '__main__':
    nums = [12, 11, 13, 5, 6]
    insertionSort(nums)
    print("插入排序后的数组:")
    print(nums)