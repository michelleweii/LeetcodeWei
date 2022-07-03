class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        split_s = s.split()
        # print(split_s)
        length = len(split_s)
        if length==0:
            return 0
        rs = len(split_s[length-1])
        # print(rs)
        return rs

def main():
    s = " "
    myResult = Solution()
    print(myResult.lengthOfLastWord(s))

if __name__ == '__main__':
    main()