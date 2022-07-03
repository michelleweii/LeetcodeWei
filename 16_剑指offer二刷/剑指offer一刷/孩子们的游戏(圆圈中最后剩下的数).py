# -*- coding:utf-8 -*-
class Solution:
    # https: // blog.csdn.net / tingyun_say / article / details / 52343897
    def LastRemaining_Solution(self, n, m):
        # 递归做法，寻求相邻两项之间的关系
        if (n == 0):return -1
        if (n == 1):return 0
        else:
            return (self.LastRemaining_Solution(n - 1, m) + m) % n


"""
        if not m or not n:
            return -1
        res = range(n)
        i = 0
        while len(res)>1:
            i = (m+i-1)%len(res)
            res.pop(i)
        return res[0]

"""
if __name__ == '__main__':
    n = 5
    m = 3
    print(Solution().LastRemaining_Solution(n,m))