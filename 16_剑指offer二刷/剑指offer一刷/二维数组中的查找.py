# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array or not array[0]:return False
        n = len(array)
        i,j = 0,len(array[0])-1
        while i<n and j>=0:
            # print(array[i][j])
            if array[i][j]>target:j-=1
            elif array[i][j]<target:i+=1
            else:return True
        return False

if __name__ == '__main__':
    nums = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    k = 7
    print(Solution().Find(k,nums))