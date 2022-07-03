"""
easy 2021-12-09 同向双指针
# 进位如何考虑？初始化carry=0, 求进位 carry = tmp // 10
# python可以左加
# loop choose while or for? while
https://leetcode-cn.com/problems/add-strings/solution/add-strings-shuang-zhi-zhen-fa-by-jyd/
"""
# 2022-01-05 链表题LC445类似
class Solution:
    def addStrings(self, num1: str, num2: str):# -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res # 左加
            i, j = i - 1, j - 1
        return "1" + res if carry else res

if __name__ == '__main__':
    num1 = "456"
    num2 = "77"
    # 533
    print(Solution().addStrings(num1,num2))