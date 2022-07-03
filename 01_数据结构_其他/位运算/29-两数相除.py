"""
middle
位运算
"""

class Solution(object):
    def divide(self, dividend, divisor):
        a = abs(dividend)
        b = abs(divisor)
        if a < b: return 0
        num = 0
        while b<=a:
            sum = b
            cnt = 1
            while(sum + sum <= a):
                cnt += cnt
                sum += sum
            a = a - sum
            num = num + cnt
        if divisor<0 and dividend>0 or divisor>0 and dividend<0:
            return -num
        else:
            return num

    def divide_gg(self, dividend, divisor):
        a = abs(dividend)
        b = abs(divisor)
        if a<b:return 0
        # for i in range(b,a,b):
        #     print(i)
        # 这样会内存溢出
        cnt = len(range(b,a+1,b)) # 构建生成器
        if divisor<0 and dividend>0 or divisor>0 and dividend<0:
            return -cnt
        else:
            return cnt

    def div(self, dividend, divisor):
        # 取巧了
        i = abs(dividend)//abs(divisor)
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            i *= -1
        max_limit = 2**31 - 1
        if i < -2**31 or i > max_limit:
            return max_limit
        return i



if __name__ == '__main__':
    dividend = 7
    divisor = -3
    print(Solution().divide(dividend,divisor))