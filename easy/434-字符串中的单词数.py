class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s)==0:
        #     return 0
        # n = s.split(" ")
        # count = 0
        # for i in n:
        #     if i!='':
        #         count+=1
        #
        # return count

        return len(s.split())  # 分割包括空格，换行，制表位等，标点符号与单词一起，不影响


def main():
    s = "hi, amy is a clever girl   "
    myresult = Solution()
    print(myresult.countSegments(s))

if __name__ == "__main__":
    main()