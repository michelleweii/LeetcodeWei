

def func(x, nums):
    l,r=0,len(nums)
    while l<r:
        mid=(l+r)//2
        count=0
        for num in nums:
            if x<=num:count+=1
        print('count',count)
        # if count==nums[mid]:return count
        if count>mid:
            r=mid
        else: # <=
            l=mid+1
    return l
x=1
nums=[1,2,200] # 1
print(func(x,nums))
