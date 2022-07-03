"""
easy 模拟题
https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
"""

def printNumbers(n: int):
    return [i for i in range(1, 10 ** n)]


if __name__ == '__main__':
    n = 1
    print(printNumbers(n))