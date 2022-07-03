"""
middle 2021-12-22 贪心
https://programmercarl.com/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.html#%E6%9A%B4%E5%8A%9B%E8%A7%A3%E6%B3%95
题目：找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
分析：
例如：98，一旦出现strNum[i-1] > strNum[i]的情况（非单调递增），
首先想让strNum[i-1]--，然后strNum[i]给为9，这样这个整数就是89，即小于98的最大的单调递增整数。
"""
class Solution:
    # 从后向前遍历332的数值变化为：332 -> 329 -> 299
    def monotoneIncreasingDigits(self, n: int) -> int:
        a = list(str(n)) # ['3', '3', '2']
        for i in range(len(a)-1,0,-1):
            # 98->99->89
            if int(a[i])<int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                # python不需要设置flag值，直接按长度给9就好了
                # a[i] = '9', 不能这个简单的设置
                # print('9'* (len(a) - i), a)
                a[i:] = '9'* (len(a) - i)
                # print(a)
        return int(''.join(a))


if __name__ == '__main__':
    # n = 10 # 9
    n = 332 # 299
    print(Solution().monotoneIncreasingDigits(n))