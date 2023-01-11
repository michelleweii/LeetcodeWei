# 20230111 ali本地生活

# 问题：对 values 中的元素排序，打印出它们在原数组 values 中的序号。
"""
# 注意
tuple的特点
1、不支持添加元素【增】
2、不支持删除元素【删】
3、不支持修改元素（修改操作的步骤是：先删除、再添加）【改】
4、支持2种查找元素【查】
第一、根据下标查找元素，称为【访问】元素，时间复杂度为O（1）
第二、根据元素值获取下标，称为【查找】元素，时间复杂度为O（n）
# https://haicoder.net/python/python-tuple-add.html
"""
# keymap: {6: 0, 4: 1, 1: 2, 7: 3}
# dict_keys([6, 4, 1, 7])
# nums: [1, 4, 6, 7]
# [2, 1, 0, 3]
def quick(nums, left, right):
    if left >= right: return
    i, j = left, right
    pivot = nums[left]  # 数值
    while i < j:
        while i < j and nums[j] >= pivot: j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot: i += 1
        nums[j] = nums[i]
    nums[i] = pivot

    quick(nums, left, i - 1)
    quick(nums, i + 1, right)

if __name__ == '__main__':
    nums = [6, 4, 1, 7]
    keymap = {}
    n = len(nums)
    for i in range(n):
        keymap[nums[i]] = i
    print('keymap:', keymap)
    print(keymap.keys())

    nums = list(keymap.keys())
    quick(nums, 0, n-1)
    print('nums:', nums)


    res = []
    for num in nums:
        res.append(keymap[num])

    print(res)


