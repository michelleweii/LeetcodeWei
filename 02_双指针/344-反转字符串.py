"""
easy 2021-09-09 反向双指针|很简单可以直接过
# 经典的双指针，左右两个指针指向的数字相互交换，并同时向中间行进，直到遇见彼此
"""
class Solution:
    def reverseString(self, s):
        i = 0
        j = len(s)-1
        while i < j: # i<=j也是ok的
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return s


if __name__ == '__main__':
    s = ["h","e","l","l","o"] # ["o","l","l","e","h"]
    myResult = Solution()
    print(myResult.reverseString(s))