# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    """
    def __init__(self):
        self.Q = []
        self.hashmap = {}

    def FirstAppearingOnce(self):
        if self.Q:
            return self.Q[0]
        return "#"

    def Insert(self, char):

        if char in self.hashmap:
            self.hashmap[char] += 1
            if not self.Q:
                self.Q.pop()
        else:
            self.hashmap[char] = 1
            self.Q.append(char)
        # 因为list是可变的，所以每次会改变都是null
        # 要用str不可变，深拷贝的方法待完成
        """
    # 返回对应char
    def __init__(self):
        self.s=''
        self.dict1={}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict1[i]==1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s=self.s+char
        if char in self.dict1:
            self.dict1[char]=self.dict1[char]+1
        else:
            self.dict1[char]=1


if __name__ == '__main__':
    s = "BabyBaby"
    # print(s[:-1])
    for ch in s:
        Solution().Insert(ch)
    print(Solution().FirstAppearingOnce())