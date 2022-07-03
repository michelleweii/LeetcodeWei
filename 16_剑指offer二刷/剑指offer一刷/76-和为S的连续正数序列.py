# -*- coding:utf-8 -*-
# 双指针
class Solution:
    def FindContinuousSequence(self, tsum):
        s,j = 1,1
        res = []
        for i in range(1,tsum+1):
            while s<tsum:
                j += 1
                s += j
            if s==tsum and j-i+1>1:
                item = []
                for k in range(i,j+1):
                    item.append(k)
                res.append(item[:])
            s -= i
        return res

if __name__ == '__main__':
    n = 15
    print(Solution().FindContinuousSequence(n))