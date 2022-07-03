# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stk = []
        self.min_stk = []
    def push(self, node):
        self.stk.append(node)
        if not self.min_stk or self.min_stk[-1] >= node:
            self.min_stk.append(node)
    def pop(self):
        if self.stk[-1]==self.min_stk[-1]:
            self.min_stk.pop()
        self.stk.pop()
    def top(self):
        return self.stk[-1]
    def min(self):
        return self.min_stk[-1]


if __name__ == '__main__':
    nums = [2,9,4,1,10,5,1]
    for x in nums:
        print(Solution().push(x))
        print(Solution().min())