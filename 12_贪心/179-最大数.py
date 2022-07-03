"""
middle 2021-12-16 贪心
同剑指offer，自己实现一个排序规则，好吧，如果这算作贪心。
剑指 Offer 45-把数组排成最小的数.py

为什么要拼接？
首先拼接成的两个字符串一定是等长的。等长的字符串在比较的时候，是按照字符串的各个字符从前向后逐个比较的，所以相当于先比较了百分位，
然后比较十分位，最后比较个位。所以在字符串等长的情况下，字符串大，那么对应的整型也更大。但两个不等长的字符串就没有这个结论了，
比如 "2" > "10"，但是 2 < 10。
"""
import functools
class Solution:
    def largestNumber(self, nums): #List[int]) -> str:
        strs = map(str, nums) # 将nums中的int转为str
        # print(strs) # <map object at 0x0000024045858648>
        strs = sorted(strs, key=functools.cmp_to_key(self.sort_rule), reverse=True) # reverse=True是降序
        return ''.join(strs) if strs[0] != '0' else '0' # case: nums = [0,0] # 0
        # return ''.join(strs)
    """
    若拼接字符串 x+y>y+x ，则 x “大于” y ；
    反之，若 x+y<y+x ，则 x “小于” y ；
    比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
    """
    def sort_rule(self,x,y):
        a, b = x+y, y+x
        if a>b: return 1
        elif a<b:return -1 # '12'<'21' ——>‘1’不该排在‘2’前面
        else:
            return 0

"""
# https://leetcode-cn.com/problems/largest-number/solution/fu-xue-ming-zhu-zhuan-cheng-zi-fu-chuan-mm2s6/
# 更为python的写法
nums_str = map(str, nums)
compare = lambda x, y: 1 if x + y < y + x else -1
nums_str.sort(cmp=compare)
res = "".join(nums_str)
return "0" if res[0] == "0" else res
"""

if __name__ == '__main__':
    # nums = [3, 30, 34, 5, 9] # "9534330"
    # nums = [10, 2] # "210"
    nums = [0,0] # 0
    print(Solution().largestNumber(nums))