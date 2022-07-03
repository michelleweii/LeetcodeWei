# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:return False
        numbers = sorted(numbers)
        k = 0
        while not numbers[k]:k+=1 # 过滤开头的0
        # print(k,numbers)
        for i in range(k+1,len(numbers)):
            if numbers[i]==numbers[i-1]:
                return False
        return numbers[-1]-numbers[k]<=4


if __name__ == '__main__':
    n = [0,2,3,4,5]
    print(Solution().IsContinuous(n))