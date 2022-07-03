"""
easy python切片 once ok
2021-07-18
"""

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # a = s[n:-1]
        # b= s[:n]
        # print(a+b)
        return s[n:]+s[:n]


if __name__ == '__main__':
    s = "lrloseumgh"
    k = 6
    print(Solution().reverseLeftWords(s, k))