
# [l, mid] + [mid+1, r]
def merge_sort2(nums, l, r):
    if l>=r: return
    mid = (l + r) // 2
    merge_sort2(nums, l, mid)
    merge_sort2(nums, mid + 1, r)
    left_p, right_p = l, mid + 1
    res = []  # 临时数组，用于保存局部排序好的结果
    while left_p <= mid and right_p <= r:
        if nums[left_p] < nums[right_p]:
            res.append(nums[left_p])
            left_p += 1
        else:
            res.append(nums[right_p])
            right_p += 1
    res += nums[left_p:mid + 1]
    res += nums[right_p:r + 1]

    # 把临时数组里的元素再放回去，当前归并的区间
    for k in range(r-l+1):
        nums[l+k] = res[k]
    # print("nums", nums)
    # print("res", res)
    # print('-'*20)
    return nums  # nums已经实现原地更改

nums=[9,2,1,2,3,10,4]
print(merge_sort2(nums,0,len(nums)-1))