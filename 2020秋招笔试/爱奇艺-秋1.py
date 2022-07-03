def permute(nums):
    n = len(nums)
    rs = []
    perm(nums, 0, n, rs)
    return rs
def perm(nums, p, q, rs):
    if p == q:
        # print(nums)
        rs.append(nums[:])
        # 切片返回新数组，不改变原数组
    for i in range(p, q):
        # for i in range(p, q+1): 这里一直报错
        # 遍历一个数组就是range(0, len(arr))
        # 你第一次调用 传入的q是len(n)，你要遍历数组 就range(0, q)就行，为啥还要+1？
        nums[p], nums[i] = nums[i], nums[p]
        # nums[p]=nums[i]
        perm(nums, p + 1, q, rs)
        nums[p], nums[i] = nums[i], nums[p]
#
def post(n,nums,A):
    index = len(nums)-1
    print("cnt",index)
    for i in range(len(A)):
        while index:
            cur = nums[index]
            print("cur",cur)
            if A[i] == 0:
                for k in range(1,n):
                    if cur[k] <= cur[k-1]:
                        del cur[index]
                        continue

            elif A[i] == 1:
                for k in range(1, n):
                    # print(j)
                    if cur[k] >= cur[k - 1]:

                        del cur[index]
                        continue

            index -= 1
    print("after",len(nums))

# 符合要求的排列为{3 2 1 4}、{4 2 1 3}和{4 3 1 2}。

if __name__ == '__main__':
    # s = input().strip().split('')
    # n = int(s[0])
    # m = int(s[1])
    # matrix = []
    # while n:
    #    tmp = input().strip()
    #    tmp = [int(x) for x in tmp]
    #    matrix.append(tmp)
    #    n-=1
    n = 4
    A = [1,1,0]
    nums = [i for i in range(1,n+1)]
    res = (permute(nums))
    print(post(n,res,A))
