# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # if not numbers:return 0
        dict = {}
        for num in numbers:
            dict[num] = 1 if num not in dict else dict[num]+1
            if dict[num]>len(numbers)//2:
                return num
        return 0


if __name__ == '__main__':
    n = [1,2,3,2,2,2,5,4,2]
    # 2
    print(Solution().MoreThanHalfNum_Solution(n))