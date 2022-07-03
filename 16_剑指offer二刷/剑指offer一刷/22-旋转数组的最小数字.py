 # -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:return 0
        low, high = 0, len(rotateArray)-1
        while low < high - 1:
            mid = (low+high)//2
            if rotateArray[mid-1] > rotateArray[mid]:
                return rotateArray[mid]
            elif rotateArray[low] > rotateArray[mid-1]:
                high = mid
            else:
                low = mid
        return rotateArray[0]


if __name__ == '__main__':
    a = [3,4,5,1,2]
    # a = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    print(Solution().minNumberInRotateArray(a))

"""
    # error
    def minNumberInRotateArray(self, rotateArray):
        # 二分
        n = len(rotateArray)-1
        # print(n)
        if n<0: return -1
        while (n>0 and rotateArray[n]==rotateArray[0]):n-=1
        # print(n)
        if rotateArray[n]>=rotateArray[0]:return rotateArray[0]
        l,r = 0,n
        while (l<r):
            mid = (l+r)//2
            if rotateArray[mid]<rotateArray[0]:r=mid
            else: l=mid+1
        return rotateArray[mid]
"""