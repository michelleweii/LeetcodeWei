# 题目意思：将二进制转为十进制相加后转为二进制
class Solution:
    def addBinary(self, a, b):
        print(int(a, 2))  # 将二进制转为十进制输出
        return bin(int(a, 2)+int(b, 2))[2:]


if __name__ == '__main__':
    a = "11"
    b = "1"
    res = Solution()
    print(res.addBinary(a, b))
