"""
middle python内置函数
2021-07-18
"""
import functools
class Solution:
    """
    若拼接字符串 x+y>y+x ，则 x “大于” y ；
    反之，若 x+y<y+x ，则 x “小于” y ；
    比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
    """
    def sort_rule(self,x,y):
        a, b = x+y, y+x
        if a>b: return 1
        elif a<b:return -1
        else:
            return 0

    def minNumber(self, nums):
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(self.sort_rule))
        return ''.join(strs)


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    print(Solution().minNumber(nums))
    # a = ['3', '30', '31', '300']
    # print(sorted(a)) # ['3', '30', '300', '31']

