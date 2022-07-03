# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
# 位运算
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # 2^3^3^4^4=2 只出现一次的数，只要异或一遍
        sum = 0 # x^y
        for x in array:
            sum^=x
        k = 0 # x^y只要有一位，第k位是1，不等于0，否则会异或得0
        # 将第k位移到个位，&1，即可看出第k位是0还是1
        while not (sum>>k&1):k+=1
        # k存x^y中是1的那一位
        first = 0
        for x in array:
            if x>>k&1: # x的第k位是1的疑惑和
                first^=x
        return [first,sum^first]




if __name__ == '__main__':
    a = [1,2,3,3,4,4]
    print(Solution().FindNumsAppearOnce(a))