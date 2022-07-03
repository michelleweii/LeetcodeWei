# 分三种情况讨论： 
# 1. 判断是否为空：输入为空时，输出0，并标记是因为非法输入导致的 
# 2. 错误输入：如果字符串的前部分字符为空，此时忽略前面为空的部分，即从有正常字符的位置开始计算，如输入字符串为“ 42”，则输出为42； 
# 3. 特殊输入：第一个有效字符是否为‘+’或‘-’，则先判断最后输出的整数位正还是负数 
# 4. 考虑溢出等情况，如INT_MIN, INT_MAX;
class Solution:
    def myAtoi(self, str):
        str0 = str.lstrip()     #删除字符串前面的空格
        # print(str0)
        if len(str0)==0:
            return 0
        pos = 1                 #用pos记录整数的正负
        if str0[0] == '-':      # #首字符为正负号则用pos记录并删除首字符
            pos = -1
            str0 = str0[1:]
        elif str0[0] == '+': 
            pos = 1
            str0 = str0[1:]
        if len(str0) == 0:      #若删除首字符后字符串为空则返回为0
            return 0
        # isdigit() 方法检测字符串是否只由数字组成
        if not str0[0].isdigit():    #若首字符不为数字则返回为0
            return 0 
        i = 0
        while i<len(str0):
            if str0[i].isdigit():
                i+=1
            else:
                break
        result = pos*int(str0[:i])   
        if result>pow(2,31)-1:
            return (pow(2,31)-1)
        elif result<pow(2,31)*(-1):
            return pow(2,31)*(-1)
        else:
            return result

if __name__ == '__main__':
    string = " -42"
    print(Solution().myAtoi(string))

# 在没有出现有效字符前，遇到空格则跳过，而出现有效字符之后，遇到空格则要跳出，所以需要一个变量来标记出现空格时之前是否出现过有效字符
# 对于正负号，我们需要一个变量来记录他，但正负号只有首次出现才有效，在正负号之前出现过有效字符的话，正负号就是无效字符了，于是也需要一个变量来标记正负号之前是否出现过的有效字符
