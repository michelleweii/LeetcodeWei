# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:return False
        n = len(sequence)
        root = sequence[-1]
        k = 0
        while k < n and sequence[k] < root:k += 1
        for i in range(k,n):
            if sequence[i]<root:return False
        left = True
        if k > 0:# 说明有左子树
            left = self.VerifySquenceOfBST(sequence[0:k])
        right = True
        if k < n-1: # 若右子树存在
            right = self.VerifySquenceOfBST(sequence[k:-1])
        return left and right


if __name__ == '__main__':
    # s = [1,3,2]
    s = [7,4,6,5]
    print(Solution().VerifySquenceOfBST(s))