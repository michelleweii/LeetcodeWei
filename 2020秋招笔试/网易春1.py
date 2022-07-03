def poka(n,nums):
    if n<5:
        return 0
    dictc = {'A':0,'J':11,'Q':12,'K':13}

    for i in range(len(nums)):
        if nums[i] in dictc:
            nums[i] = dictc[nums[i]]
        nums[i]= int(nums[i])

    nums = sorted(nums)
    flag1,flag2=0,0
    if nums[0]==nums[1]:
        flag1 +=1
    if nums[-1]==nums[-2]:
        flag2 +=1
    # print(nums)
    diffnums = list(set(nums))
    if len(diffnums)<5:
        return 0
    print(diffnums)
    cnt = 0
    for i in range(0,len(diffnums)):
        tmp = diffnums[i:i+5]
        print(tmp)
        for i in range(len(tmp)-1):
            if tmp[i+1]-1!=tmp[i]:
                break
        cnt+=1
    print(cnt+flag1+flag2)


if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        nums = input().split()
        print(nums)
        # poka(n,nums)
        t -= 1
    # 输入t表示有t个测试用例，对每个测试用例调用一遍poka函数
    # n表示nums中有多少个数字，nums为列表


    # n = 7
    # nums = ['7','3','3','4','4','5','6'] # 4
    # # n = 6
    # # nums = ['7','3','4','5','6','3']
    # poka(n, nums)