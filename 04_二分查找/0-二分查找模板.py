def check(value):
    pass

# <= 目标值的最大位置
def bsearch_1(l, r):
    while (l < r):
        mid = (l+r) // 2
        # 求最大值
        if check(mid): r = mid
        else: l = mid+1
    return l

# >= 目标值的最小位置
def bsearch_2(l, r):
    while(l<r):
        mid = (l+r+1) // 2
        # 求最小值
        if check(mid): l = mid
        else: r = mid-1
    return l

# 如果元素不存在呢？
def bisec(nums,k):
    l,r = 0,len(nums)-1
    while(l<r):
        mid = (l+r)//2
        if nums[mid]>=k: r=mid
        else: l=mid+1
    print(l) # 1 # 停在里>=k值最近的那个index=1处

if __name__ == '__main__':
    sum = (4+2)>>1
    print(sum) # 3
    nums = [1,5,6,7,9]
    k = 3
    bisec(nums,k)
