def generate(i, nums, item, result):
    if i >= len(nums):
        return
    item.append(nums[i])
    # print(item)
    result.append(item[:])
    # print(result)
    generate(i + 1, nums, item, result)
    print("item-before:{}".format(item))
    item.pop()
    # print(item)
    print("item-after:{}".format(item))
    print("i:{}".format(i))
    generate(i + 1, nums, item, result)


if __name__ == '__main__':
    nums = [1, 2, 3]
    item = []
    result = []
    generate(0, nums, item, result)


