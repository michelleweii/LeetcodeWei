"""
easy 2021-12-07
模拟题 26进制转换(与168相反)
如果题目是 10 进制转换，那么转换过程：
从高位向低位处理，起始让 ans 为 0，每次使用当前位数值更新 ans，
更新规则为 ans = ans * 10 + vali
ans = 0
ans = ans * 10 + 1
ans = ans * 10 + 2
ans = ans * 10 + 3
ans = ans * 10 + 4
https://leetcode-cn.com/problems/excel-sheet-column-number/solution/gong-shui-san-xie-tong-yong-jin-zhi-zhua-y5fm/
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for i in range(n):
            res = res*26+(ord(columnTitle[i])-65+1)
        return res

if __name__ == '__main__':
    columnTitle = "AB"
    print(Solution().titleToNumber(columnTitle))