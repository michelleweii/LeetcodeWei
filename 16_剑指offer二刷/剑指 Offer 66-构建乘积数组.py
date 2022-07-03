"""
middle 双向遍历
2021-07-20
---------------------------------------------------------------
思路：
原数组：       [1       2       3       4]
左部分的乘积：   1       1      1*2    1*2*3
右部分的乘积： 2*3*4    3*4      4      1
结果：        1*2*3*4  1*3*4   1*2*4  1*2*3*1
----------------------------------------------------------------
当前位置的结果就是它左部分的乘积再乘以它右部分的乘积。因此需要进行两次遍历，第一次遍历用于求左部分的乘积，
第二次遍历在求右部分的乘积的同时，再将最后的计算结果一起求出来。
"""
class Solution:
    def constructArr(self, a):
        if not a:return a
        p = 1
        b = [1 for _ in range(len(a))]
        for i in range(len(a)):
            b[i] = p
            p *= a[i]
        # print(b)
        p = 1
        for j in range(len(a)-1, -1, -1):
            # print(j)
            b[j] *= p
            p *= a[j]
        # print(b)
        return b



if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(Solution().constructArr(a))