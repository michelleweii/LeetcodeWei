"""
middle 模拟题
copy 没有写
2021-07-19
"""
# 2.正确样例"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"
# 3.错误样例"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4
#

# 1.包含的元素1-9,+-,e,小数点
# 2.小数点,只能包含一个,可以在最前面和最后面
# 3.正负号,在没有e的时候 正负号只能在最前面,且只能有一个
# 4.e,e的后面只能是整数,e的前后都有数字
# 5.不能为空,不能只有'+-e.'

# 是否包含数字
# 是否包含小数点,记录小数点的坐标
# 是否包含正负号
# 是否包含e,记录e的坐标

class Solution:
    def isNumber(self, s: str):
        s = s.strip()
        if s == '':
            return False

        v2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        v3 = ['+', '-']
        v4 = ['e', 'E']
        v5 = '.'

        # 包含的元素1 - 9, +-, e, 小数点
        # 小数,正负号,包含E,正整数
        f_flag, pm_flag, have_e, i_flag = False, False, False, False
        e_index, dot_index = 0, 0
        index = 0
        for i in s:
            if i in v2:
                index += 1
                i_flag = True
                continue
            elif i == v5:  # 小数点, 只能包含一个
                if f_flag: return False
                f_flag = True
                dot_index = index
            elif i in v3:
                if index != 0 and not (have_e and index == e_index + 1):
                    return False
            elif i in v4:
                if have_e: return False
                have_e = True
                e_index = index
            else:
                return False
            index += 1

        if not i_flag: return False
        if have_e:  # 包含e
            if f_flag and dot_index > e_index: return False
            if s[:e_index] in ['.', '+', '-'] or s[e_index + 1:] in ['.', '+', '-']: return False
            if e_index == 0 or e_index == len(s) - 1: return False

            return True
        else:  # 不包含e
            if f_flag and s in ['.', '+', '-']: return False

        return True


    def isNumber2(self, s):
        try:
            float(s)
            return True
        except Exception as err:
            return False



if __name__ == '__main__':
    s = "    .1  " # true
    print(Solution().isNumber(s))