"""
hard 模拟题/数学题
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/python3si-lu-dai-ma-10fen-zhong-jiang-qi-9btr/
2021-07-26

递归
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/jian-zhi-offersi-lu-de-pythonshi-xian-by-xiao-shi-/
"""
"""
总共有3种情况

"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        base = 1
        res = 0
        while base<=n:# 392, base=10
            b = n%base
            a = n//base
            cur = a%base
            a //=10
            if cur>1: res += (a+1) * base
            elif cur == 1: res += (a*base+1*(b+1))
            else:res += a*base
            base *= 10
        return res

if __name__ == '__main__':
    n = 12
    print(Solution().countDigitOne(n))