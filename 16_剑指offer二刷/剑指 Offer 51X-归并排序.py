
# 归并排序
def merge_sort1():
    pass

# 归并排序模板
# # [l, mid] + [mid+1, r]
def merge_sort2(nums, l, r):
    if l>=r: return
    mid = (l+r)//2
    merge_sort2(nums, l, mid)
    merge_sort2(nums, mid+1, r)
    left_p, right_p = l, mid+1
    res = []
    while left_p <= mid and right_p <= r:
        if nums[left_p]<nums[right_p]:
            res.append(nums[left_p])
            left_p += 1
        else:
            res.append(nums[right_p])
            right_p += 1
    res += nums[left_p:mid+1]
    res += nums[right_p:r+1]
    # 把临时数组里的元素再放回去
    print("[l:r]", l, r)
    for k in range(r-l+1):
        nums[l+k] = res[k]
    print("nums", nums)
    print("res", res)
    print('-'*20)
    return nums # nums已经实现原地更改

# def mergesort(nums,l,r):
#     if l>=r: return
#     mid = (l+r)//2
#     mergesort(nums,l,mid)
#     mergesort(nums,mid+1,r)
#     i,j=l,mid+1
#     temp = []
#     while i<=mid and j<=r:
#         if nums[i]<nums[j]:
#             temp.append(nums[i])
#             i+=1
#         else:
#             temp.append(nums[j])
#             j+=1
#     if i<=mid:temp.extend(nums[i:mid+1])
#     if j<=r  :temp.extend(nums[j:r+1])
#     for i in range(r-l+1):
#         nums[l+i] = temp[i]
#     return nums


if __name__ == '__main__':
    nums = [3,2,1,6,4]
    # a = merge_sort(nums, 0, len(nums)-1)
    # print("a", a)
    # b = mergesort(nums, 0, len(nums)-1)
    # print("b", b)
    c = merge_sort2(nums, 0, len(nums)-1)
    print("c", c)

