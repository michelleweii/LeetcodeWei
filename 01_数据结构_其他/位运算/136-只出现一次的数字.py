"""
[数学]求和，作差，剩余的为target
[哈希]遍历一遍，返回value=1的key
[位运算]
"""
class Solution(object):
    def singleNumber(self, nums):
        # // 异或满足两条定律：
        # // 1、a^b = b^a
        # // 2、a^a=0
        # // 3、a^0=a;
        res = 0
        for x in nums:
            res^=x
        return res
    # 数学
    def singleNumber_math(self, nums):
        tmp = list(set(nums))
        sumtmp = 0
        for j in tmp:
            sumtmp += j*2
        return sumtmp-sum(nums)

if __name__ == '__main__':
    listA = [4,1,2,1,2]
    myResult = Solution()
    print(myResult.singleNumber(listA))