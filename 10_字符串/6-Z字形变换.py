"""
middle
找规律
思路：下标
对于行数n，
1、对于第一行和最后一行，是公差为2(n-1)的等差数列，首项是0和n-1
2、对于第i行（0<i<n-1），是两个公差为2(n-1)的等差数列交替排列，首项分别是i和2n-i-2
"""
class Solution:
    def convert(self, s, numRows):
        if numRows==1:return s
        res = []
        for j in range(numRows):
            # 如果是第一行or最后一行
            if j==0 or j==numRows-1:
                for i in range(j, len(s), 2*(numRows-1)):
                    res.append(s[i])
            else:
                # 注意这里要错位交叉添加
                # for k, i in zip(range(j, len(s), 2*(numRows-1)), range(2*numRows-2-j, len(s), 2*(numRows-1))):
                k = j # 第一个数字
                i = 2*numRows-2-j # 第二个数字
                while k<len(s) or i<len(s):
                    if k<len(s):res.append(s[k])
                    if i<len(s):res.append(s[i])
                    k += 2*(numRows-1)
                    i += 2*(numRows-1)
        return "".join(res)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    myResult = Solution()
    print(myResult.convert(s, numRows))
    # "PAHNAPLSIIGYIR"

    # for i, j in zip(range(0, 5), range(7, 0, -1)):
    #     print(i, j) # zip这种组合，结束条件是and。其中一个结束，另一个也结束了。