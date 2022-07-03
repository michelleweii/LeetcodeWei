"""
hard 2022-05-24 贪心
对于 abcde 来说，最近的回文数值的前三位可能是abc、abc+1和abc-1三者之一，其他位置的数值随着前三位的确定而唯一确定。

"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:



if __name__ == '__main__':
    n="123" # 最近的回文数121
    print(Solution().nearestPalindromic(n))