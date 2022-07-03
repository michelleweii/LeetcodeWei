"""
middle 2022-06-20 模拟题
https://leetcode.cn/problems/multiply-strings/solution/python-zi-fu-chuan-bao-li-mo-ni-shu-shi-cheng-fa-j/
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 123 * 45 = 123 * 5 + 123 *40 = 615 + 4920 = 5535
        # 让num1 依次乘上 num2 的每一位的和
        # 把第一步里得到的所有和累加在一起，就可以得到 num1 * num2 的结果
        if num1 == "0" or num2 == "0": # 处理特殊情况
            return "0"
        
        l1, l2 = len(num1), len(num2) 
        if l1 < l2: 
            num1, num2 = num2, num1 #保障num1始终比num2长， 个人习惯
            l1, l2 = l2, l1

        res='0'
        for i in range(l2-1,-1,-1):
            # print(num1, num2[i])
            tmp=self.mulStrings(num1, int(num2[i])) + (l2-i-1)*'0'  # #计算num1和num2的当前位的乘积
            # print('mul',tmp)
            res=self.addStrings(res,tmp) # #计算res和tmp的和
        return res

    def mulStrings(self, s, n):
        # 每一位相乘
        # 输入为 "123", 3，返回"369"
        res = []
        ls = len(s) - 1
        carry = 0
        for i in range(ls,-1,-1):
            num = int(s[i]) * n + carry
            carry = num // 10
            res.append(num % 10)
        if carry:
            res.append(carry)
        res=res[::-1]
        return "".join(str(x) for x in res)


    # LC415.字符串相乘
    def addStrings(self, num1: str, num2: str) -> str:
        # 求两数的和
        # 输入为“123”， “456”, 返回为"579"
        res = ""
        i, j, carry = len(num1)-1, len(num2)-1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res