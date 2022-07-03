"""
hard 2022-05-19 栈
https://leetcode.cn/problems/basic-calculator/solution/ru-he-xiang-dao-yong-zhan-si-lu-lai-zi-y-gpca/
"""
class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = [] # 当右括号时，用于存储计算结果
        for ch in s:
            if ch.isdigit():
                num = 10 * num + int(ch)
            elif ch == "+" or ch == "-":
                print('sign',res,sign,num)
                res += sign * num
                num = 0
                sign = 1 if ch == "+" else -1 # 统计数字后的字符
            elif ch == "(":  # (之前的元素入栈，清空临时保存结果
                # 例如123+4, res存123，sign存4
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ")": # 元素出栈
                # 例如1+(4+5)，遇到）,res=9,先乘1+这里的+，sign；
                # 再去与原res相加；
                res += sign * num
                num = 0
                res *= stack.pop() # 符号
                res += stack.pop() # 数字
                print("for",res)
        # 这里怎么理解？
        # 出循环之后，如果没有),那么)之后的数值就要在这里重新计算
        # 12 -1 3
        print(res,sign,num) # 12-3=9
        res += sign * num
        return res

if __name__ == '__main__':
    s="1+(4+5+2)-3"
    # s="(1+(4+5+2)-3)+(6+8)"
    print(Solution().calculate(s))