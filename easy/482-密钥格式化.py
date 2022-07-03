class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        rs = ""
        # tmp = ""
        newS = ""
        for ch in S:
            if ch.isalnum():
                newS += ch.upper()
        # print(newS[::-1])
        for index,ch in enumerate(newS[::-1]):
            if (index%K)==0 and index!=0:
                rs += '-'
            rs += ch
        # print(rs[::-1])
        return rs[::-1]



def main():
    S = "2-5g-3-J"
    K = 2
    myResult = Solution()
    print(myResult.licenseKeyFormatting(S,K))

if __name__=="__main__":
    main()