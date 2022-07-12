"""
easy
"""
class Solution(object):
    def reverse(self, x):
        str1 = str(x).split('-')

        if len(str1)>1:
            temp = '-'+str1[1][::-1]
            if int(temp)>-2**31 and int(temp)<2**31-1:
                return int(temp)
            return 0
        else:
            if int(str1[0][::-1])>-2**31 and int(str1[0][::-1])<2**31-1:
                return int(str1[0][::-1])
            return 0

if __name__ == '__main__':
    x = 1534236469
    myResult = Solution()
    print(myResult.reverse(x))

