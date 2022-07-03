# 可以总结出以下的要求：
#
# 该数字中不含[3, 4, 7]，否则其倒影不是数字。
# 该数字中必须包含[2, 5, 6, 9]中的至少一个，否则倒影和原数字相同
# 包含[2, 5, 6, 9]中的至少一个==[1,8,0]不构成全部的数字

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        str1 = ''
        rs = 0
        for i in range(1,N+1):
            # print(i)
            str1 = str(i)
            if (str1.count('3')==0 and str1.count('4')==0 and str1.count('7')==0):
                if (str1.count('1')+str1.count('8')+str1.count('0')!=len(str1)):
                    rs += 1
        return rs

def main():
    N = 10
    myResult = Solution()
    print(myResult.rotatedDigits(N))

if __name__ == '__main__':
    main()