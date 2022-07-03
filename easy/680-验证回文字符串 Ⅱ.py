# 解法：还是从首尾两边开始比较，如果匹配就移动指针继续比较。
# 当遇到不匹配的时候，删除左边的字符或者右边的字符，只要有一种能匹配就继续。
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def myValidPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return myValidPalindrome(s, left, right - 1) or myValidPalindrome(s, left + 1, right)
            left, right = left + 1, right - 1
        return True


def main():
    s = "abc"
    myResult = Solution()
    print(myResult.validPalindrome(s))

if __name__ == '__main__':
    main()