"""
easy 2022-02-27 二分
# 【牛顿迭代法】https://leetcode-cn.com/problems/sqrtx/solution/niu-dun-die-dai-fa-by-loafer/
# 【二分法】https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:return x
        if x==1:return x
        l,r = 1, x//2
        while l<r:
            mid = (l+r+1)//2
            if mid*mid<=x:
                l=mid
            else:
                r=mid-1
        return r

if __name__ == '__main__':
    x = 9 # 8,return 2容易理解
    print(Solution().mySqrt(x))
