"""
hard 2022-05-12 二分
https://leetcode.cn/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-coder233-2/
关于最后的count+1
temp <= mid，相应的，不会执行，也就是说最后一个划分得到的子数组实际没有统计到数量中，故需要 对cnt进行 + 1处理；
temp > mid，相应的，会执行，但是实际划分的部分应该是截止到最后一个数之前（因为加上最后这个数之后就不满足条件了），所以最后一个数做单独划分，也需要对cnt进行 + 1处理
# 与LC287类似
"""
class Solution:
    def splitArray(self, nums,m): #List[int], m: int) -> int:
        # 由于题目的返回要求：返回最小和的值
        # 最小和必然落在 [max(nums), sum(nums)] 之间
        # 我们可以使用二分来进行查找
        l,r=max(nums),sum(nums)
        while l<r:
            mid=(l+r)//2
            # 二分算法
            # 我们由前向后对nums进行划分，使其子数组和 <= mid，然后统计满足条件的数组数量
            # 若我们选的sum值过小，则满足条件的数量 > m，目标值应落在 [mid+1, high]
            # 若我们选的sum值过大，则满足条件的数量 < m，目标值应落在 [low, mid-1]
            sub_sum=0
            count=0
            for i in range(len(nums)):
                sub_sum+=nums[i]
                if sub_sum>mid:
                    count+=1
                    sub_sum=nums[i] # 这里不清楚？分成好几段
            ## 末尾还有一个子数组我们没有统计，这里把它加上
            count += 1 # 这里不清楚？ 假如分成2段，那么如果剩余部分没有满足if sub_sum>nums[mid]:
                    # 但也是要统计的。
            if count>m:
                l=mid+1
            else:
                r=mid
        return l


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(Solution().splitArray(nums,m))