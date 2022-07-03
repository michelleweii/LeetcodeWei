# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        B = []
        if not A:return B
        n = len(A)
        p = 1
        for i in range(n):
            B.append(p)
            p *= A[i]
            # print(i,A[i])
        # print(B) # [1, 1, 2, 6, 24]
        p = 1
        for i in range(n-1,-1,-1):
            print("B", B[i])
            B[i] *= p
            p *= A[i]
        return B
        # print(B)


if __name__ == '__main__':
    A = [1,2,3,4,5]
    print(Solution().multiply(A)) # [120, 60, 40, 30, 24]




