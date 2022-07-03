# -*- coding:utf-8 -*-
from collections import deque
class Solution:
    def reOrderArray(self, array):
        # 双端队列
        q = deque()
        n = len(array)
        for i in range(n):
            if array[i]%2==0:#偶数
                q.append(array[i])
            if array[n-i-1]%2==1:#奇数
                q.appendleft(array[n-i-1])
        return list(q)

    def quickSort(self,array): # 非稳定排序
        if not array:return array
        n = len(array)
        i,j = 0,n-1
        while i<=j:
            while (i<=j) and array[i]%2 == 1:
                i+=1
            while (i<=j) and array[j]%2 == 0:
                j-=1
            if i<j: array[i],array[j] = array[j],array[i]
        return array
        # print(array)

"""
类似快排的做法会交换元素的相对位置，不符合题意
//第一个思路：类似冒泡算法，前偶后奇数就交换
//第二个思路：再创建一个数组，遇见偶数，就保存到新数组，同时从原数组中删除
将新数组的数添加到老数组，也可用双端队列
"""

if __name__ == '__main__':
    array = [1,2,3,4,5]
    print(Solution().reOrderArray(array))