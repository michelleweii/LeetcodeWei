"""
middle 2022-05-16 超级经典栈（蘑菇街2）
https://leetcode.cn/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-shuang-zhan-chao-xi-s2ha/
思路：双栈
1、定义运算符的优先级
2、避免负号，所以0+s
3、空格跳过
4、(入栈 ；(只和)发生匹配
5、)开始『计算』，直到遇见(结束，结束之前(要弹出来
6、遇见数字，求完整的数字，数字入栈
7、遇到操作符，
【特别地，1-(-2），遍历到-，但是前一个是(, 需要补0】
如果栈顶不是(, 且栈内元素的优先级>=当前元素，开始『计算』，
把遇到的这个操作符入栈
8、结束遍历，如果ops栈不为空，一直『计算』，栈顶是答案

- 单栈做法：https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-bu-dai-gua-hao-shuang-br4d5/
单栈做法：https://leetcode.cn/problems/basic-calculator-ii/solution/zhan-dong-tu-shi-jie-227-ji-ben-ji-suan-2hhvq/
"""
class Solution:
    # 【题解】https://leetcode.cn/problems/basic-calculator-ii/solution/shi-yong-shuang-zhan-jie-jue-jiu-ji-biao-c65k/
    # 【图例】https://leetcode.cn/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-shuang-zhan-chao-xi-s2ha/
    def calculate(self, s):
        s.strip()
        nums, ops = [], []
        hashmap = {'+': 1, '-': 1, '*': 2, '/': 2} # 定义运算符优先级
        s = '0' + s # 03+2*2
        n = len(s)
        i = 0
        while i < n:
            ch = s[i]
            if ch == ' ':
                i += 1
                continue
            elif ch == '(':
                ops.append(ch)
            elif ch == ')':
                # 计算到最近的一个左括号为止, 直到(弹掉
                while ops:
                    if ops[-1] != '(':
                        self.eval(nums, ops)
                    else:
                        ops.pop()  # ()内的数字已经计算完成
                        break
            elif ch.isdigit():#'0' <= ch <= '9':  # 数字,读取一个连续的数字
                u = 0  # 临时计算数字
                j = i
                while j < n and '0' <= s[j] <= '9':
                    u = u * 10 + int(s[j])
                    j += 1
                nums.append(u)
                i = j-1
            else:  # 符号
                # LC224 这一句必须要有，s="1-(-2)" = 3
                if i > 0 and (s[i - 1] == '(' or s[i - 1] == '+' or s[i - 1] == '-'): nums.append(0)
                # // 有一个新操作要入栈时，先把栈内可以算的都算了
                # // 只有满足「栈内运算符」比「当前运算符」优先级高/同等，才进行运算
                while ops and ops[-1] != '(':
                    prev = ops[-1]
                    if hashmap[prev] >= hashmap[ch]:
                        self.eval(nums, ops)
                    else:
                        break
                ops.append(ch)
            i += 1
        # 将剩余的计算完
        print(nums,ops)
        while ops: self.eval(nums, ops)
        return nums[-1]

    def eval(self, nums, ops):
        # if not nums or len(nums)<2: return
        if not nums:return
        if not ops: return
        b, a = nums.pop(), nums.pop() if nums else 0
        print('b,a',b,a)
        op = ops.pop()
        ans = 0
        if op == '+':
            ans = a + b
        elif op == '-':
            ans = a - b
        elif op == '*':
            ans = a * b
        elif op == '/':
            ans = a // b  # a*1.0/b
        nums.append(ans)

if __name__ == '__main__':
    # s = "3+2*2"
    s="1-(-2)"
    print('10'.isdigit())
    print(Solution().calculate(s))


    #     def calculate_old(self, s):
    #         n = len(s)
    #         stk = []
    #         pre_sign = '+' # 用 pre_op 记录上一个运算符的方法
    #         num = 0
    #         # 入栈的过程中把乘除法的中间结果算出来
    #         for i in range(n):
    #             # 遍历123，是一个一个枚举，要累加才是最终的数字
    #             if s[i]!=' ' and s[i].isdigit():
    #                 num = num*10 + ord(s[i]) - ord('0')
    #
    #             if i==n-1 or s[i] in '+-*/':
    #                 if pre_sign == '+':
    #                     stk.append(num)
    #                 elif pre_sign == '-':
    #                     stk.append(-num)
    #                 elif pre_sign == '*':
    #                     stk.append(stk.pop()*num)
    #                 else:
    #                     # 这里需要注意一些 -3/2=-1 不是(-3)//2=-2 所以不能是//
    #                     stk.append(int(stk.pop()/num))
    #                 pre_sign = s[i]
    #                 num = 0
    #         return sum(stk)