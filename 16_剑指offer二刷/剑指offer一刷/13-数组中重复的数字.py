# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        # 在一个长度为n的数组里的所有数字都在0到n-1的范围内
        for x in numbers:
            if x<0 or x>=n:return False
        for i in range(n):
            while i != numbers[i] and numbers[numbers[i]]!=numbers[i]:
                numbers[numbers[i]],numbers[i] = numbers[i],numbers[numbers[i]]
                # print(i,numbers)
            # print(i)
            if i != numbers[i] and numbers[numbers[i]]==numbers[i]:
                # nums[i]已重复
                # print("0000")
                # print(i)
                duplication[0] = numbers[i]
                return True
        return False


if __name__ == '__main__':
    nums = [2,3,1,0,2,5,3]
    dup = [0]
    print(Solution().duplicate(nums,dup))
