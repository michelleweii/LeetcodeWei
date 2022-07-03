"""
easy
首先将nums化成二进制数，然后再化成补数的形式，再化成十进制数。
https://leetcode-cn.com/problems/number-complement/solution/476-shu-zi-de-bu-shu-jian-dan-si-lu-xian-y4rq/
"""
class Solution(object):
    def findComplement(self, num):
        res = []
        result = 0
        # 十进制转二进制的方法：除2取余，逆序排
        res.append(str(num%2))
        while (num//2 != 0):
            num = num//2
            res.append(str(num%2))
        res.reverse() # 逆序
        print(res)
        # 按位取反
        for i,val_i in enumerate(res):
            if (val_i=='0'):
                res[i] = '1'
            else:
                res[i] = '0'
        print(res)
        # 2进制转为10进制
        for j,val_j in enumerate(res):
            if (val_j == '1'):
                result += pow(2, len(res)-1-j)
        return result

if __name__ == "__main__":
    num = 5
    myresult = Solution()
    print(myresult.findComplement(num))
