"""
easy 2021-12-07
模拟题 26进制转换(与171相反)
对于一般性的进制转换题目，只需要不断地对 columnNumber进行 % 运算取得最后一位，
然后对 columnNumber 进行 / 运算，将已经取得的位数去掉，记得顺序要reverse
直到 columnNumber为 0 即可。
https://leetcode-cn.com/problems/excel-sheet-column-title/solution/gong-shui-san-xie-cong-1-kai-shi-de-26-j-g2ur/
"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber>0:
            columnNumber -= 1
            # ASCII码转大写字符 并且左加
            # python字符串左加需要创建新字符串，时间复杂度是O（n）
            s = chr(65+columnNumber%26) + s
            columnNumber //= 26
        return s

#     public String convertToTitle(int cn) {
#         StringBuilder sb = new StringBuilder();
#         while (cn > 0) {
#             cn--;
#             sb.append((char)(cn % 26 + 'A'));
#             cn /= 26;
#         }
#         sb.reverse(); # 左加等价于str倒序，回顾进制转换
#         return sb.toString();
#     }

if __name__ == '__main__':
    columnNumber = 28
    print(Solution().convertToTitle(columnNumber))