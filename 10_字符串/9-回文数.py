"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

class Solution(object):
    def isPalindrome(self,x):
        str1 = str(x)  #数字转为字符串
        length = len(str1)
        tepstr = str1[::-1] #反转字符串
        if(length==1):
            return True
        else:
            for i,val_i in enumerate(str1):
                if(i>(length/2-1)):
                    return True
                if(val_i != tepstr[i]):
                    return False
                return True



def main():
    x = 101
    myresult = Solution()
    print(myresult.isPalindrome(x))

if __name__ == "__main__":
    main()
