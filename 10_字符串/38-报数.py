# 我的想法：用递归（脑残）
# 2021-05-26

class Solution(object):
    def countAndSay(self, n):
        s = '1'
        for _ in range(1, n):
            nextS = ''
            countC = 1
            for j in range(1, len(s)+1):
                if j == len(s) or s[j] != s[j-1]:
                    nextS += str(countC) + s[j-1]
                    countC = 1
                else:
                    countC += 1
            s = nextS
        return s

if __name__ == '__main__':
    n = 4
    myResult = Solution()
    print(myResult.countAndSay(n))