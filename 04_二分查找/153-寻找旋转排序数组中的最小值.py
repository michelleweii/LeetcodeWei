"""
middle 2021-05-13 二分
"""
# mid < right 表面右边有序 否则左边有序
# 那么mid > right 则表明最小数肯定在mid 和 right之间
class Solution(object):
    def minArray(self, numbers) -> int:
        n = len(numbers)-1
        while(n>0 and numbers[n]==numbers[0]): n-=1
        # 最后比第一个值大，则一定递增
        if numbers[n] >= numbers[0]:return numbers[0]
        l, r = 0, n
        while(l<r):
            mid = (l+r)//2
            if numbers[mid]<numbers[0]: r=mid
            else:
                l = mid+1
        return numbers[l]

if __name__ == "__main__":
    numbers = [3, 4, 5, 1, 2]
    print(Solution().minArray(numbers))
