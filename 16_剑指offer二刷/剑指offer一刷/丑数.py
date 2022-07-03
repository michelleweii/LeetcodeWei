# -*- coding:utf-8 -*-
# leetcode264 类似于三路归并
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0: return False
        i,j,k = 0,0,0
        res = [1]
        while len(res)<index: # res在变，len的值也在变
            # 长度可以代表第几个
            tmp = min(res[i]*2,res[j]*3,res[k]*5)
            res.append(tmp)
            if res[i] * 2 == tmp: i += 1
            # i代表2所产生的丑数到第几步了
            if res[j] * 3 == tmp: j += 1
            if res[k] * 5 == tmp: k += 1

        return res[-1]



if __name__ == '__main__':
    idx = 5
    print(Solution().GetUglyNumber_Solution(idx))