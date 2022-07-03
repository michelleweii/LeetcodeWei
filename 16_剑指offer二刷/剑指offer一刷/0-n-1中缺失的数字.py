def fn(nums):
    n = len(nums)+1
    s = (0+n-1)*n//2
    # print(s)
    for x in nums:
        s-=x
    # print(s)
    return s


nums = [0,2,3,4]
print(fn(nums))