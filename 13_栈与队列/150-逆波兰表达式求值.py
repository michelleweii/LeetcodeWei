"""
middle
栈
思路：
用一个栈S2来实现计算，扫描从左往右进行，如果扫描到操作数，则压进S2，
如果扫描到操作符，则从S2弹出两个操作数。进行相应的操作，并将结果压进S2(S2的个数出2个进1个)，
当扫描结束后，S2的栈顶就是表达式结果。
"""
class Solution:
    def evalRPN(self, tokens) :
        stack = []
        for c in tokens:
            if c.isdigit() or ('-' in c and len(c)>1):
                stack.append(int(c))
            else:
                # 注意除数与被除数 [0,3,/]
                b,a = stack.pop(),stack.pop()   # list中弹出最后一个
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(a - b)
                elif c == '*':
                    stack.append(a * b)
                elif c == '/':
                    stack.append(int(a/b))
        return stack[0]

if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    a = "-88" # print(a.isdigit()) # False
    b = "88" #print(b.isdigit()) # True
    print(3/2) # 1.5
    print(int(3/2)) # 1
    print(Solution().evalRPN(tokens))
