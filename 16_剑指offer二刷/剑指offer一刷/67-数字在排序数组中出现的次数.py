# 统计一个数字在排序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:return 0
        l,r = 0,len(data)-1
        while l<r:
            mid = (l+r)//2
            if data[mid]<k: l = mid+1
            else: r = mid
        if data[r]!=k:return 0
        left = r
        l, r = 0, len(data) - 1
        while l<r:
            mid = (l+r+1) // 2
            if data[mid] <= k: l = mid
            else: r = mid-1
        cnt = l-left+1
        return cnt



if __name__ == '__main__':
    data = [1,2,3,3,3,3,4,5]
    k = 3
    print('len',len(data))
    print(Solution().GetNumberOfK(data,k))