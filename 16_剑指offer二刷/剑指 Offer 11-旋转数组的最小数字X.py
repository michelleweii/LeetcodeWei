"""
easy 2021-07-13 二分
做几遍忘几遍！！！
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
"""
class Solution:
    def minArray(self, numbers):
        # numbers是原本是递增的
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


if __name__ == '__main__':
    numbers = [2,2,2,0,1]
    print(Solution().minArray(numbers))