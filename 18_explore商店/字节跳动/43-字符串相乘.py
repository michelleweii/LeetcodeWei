"""
middle 2022-02-27 竖式乘法（高频题）
https://leetcode-cn.com/problems/multiply-strings/solution/you-hua-ban-shu-shi-da-bai-994-by-breezean/
相关题：计算字符串数字累加其实就是 415. 字符串相加
"""
# 普通竖式：遍历 num2 每一位与 num1 进行相乘，将每一步的结果进行累加。
# 模拟乘法：https://leetcode-cn.com/problems/multiply-strings/solution/zui-jian-dan-de-li-jie-pythonmo-ni-cheng-1krb/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' == num1 or '0' == num2:return  '0' # is会报错
        res = '0' # 保存计算结果
        # num2 逐位与 num1 相乘
        num1_l = list(num1)
        num1 = [int(i) for i in num1_l]
        num2_l = list(num2)
        num2 = [int(i) for i in num2_l]
        # num2 逐位与 num1 相乘
        for i in range(len(num2)-1,-1,-1):
            carry = 0
            temp = [] # 保存 num2 第i位数字与 num1 相乘的结果
            # 补 0 ! 重要
            for j in range(len(num2)-1-i):
                temp.append(0)
            n2 = num2[i]
            k = len(num1)-1
            # num2 的第 i 位数字 n2 与 num1 相乘
            while k>=0 or carry !=0:
                n1 = 0 if k<0 else num1[k]
                product = (n1 * n2 + carry) % 10
                temp.append(product)
                carry = (n1 * n2 + carry) // 10
                k-=1
            # print(temp)
            temp = ''.join([str(x) for x in temp[::-1]])
            # 将当前结果与新计算的结果求和作为新的结果
            res = self.StringPlusString(res, temp)
        return res

    # LC415
    def StringPlusString(self, s1, s2):
        # 这个函数的功能是：计算两个字符串的和。
        # 举例：输入为“123”， “456”, 返回为"579"
        # PS：LeetCode415题就是要写这个函数
        # print(s1,s2)
        if s1 is '0': return s2
        if s2 is '0': return s1
        s1 = [int(x) for x in s1]
        s2 = [int(x) for x in s2]
        carry = 0
        builder = []
        i,j =len(s1)-1,len(s2)-1
        while i>=0 or j>=0 or carry!=0:
            x = s1[i] if i>=0 else 0
            y = s2[j] if j>=0 else 0
            # print(x,y)
            sum = (x+y+carry)%10
            carry=(x+y+carry)//10
            builder.append(sum)
            i-=1
            j-=1
        # print(builder)
        builder = builder[::-1]
        return "".join(str(x) for x in builder)


if __name__ == '__main__':
    num1 = "123"
    num2 = '0'#"456"
    print(Solution().multiply(num1,num2))
    # print(Solution().StringPlusString(num1, num2))