"""
Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        newS = ""
        for i, ch in enumerate(S):
            # 如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
            if ch.isalpha(): # 检测字符串是否只由字母组成
                newS += ch
        # print(newS) # TestngLeetcodeQ
        newS = newS[::-1]  # reverse string

        # feed reversed strings back into
        index = 0
        r = ""
        for i, ch in enumerate(S):
            if ch.isalpha():
                r += newS[index]
                index += 1
            else:
                r += ch
        return r

    # def reverseOnlyLetters(self, S):
    #     i, j = 0, len(S) - 1
    #     S = list(S)
    #     while i < j:
    #         while i < j and not S[i].isalpha(): i += 1
    #         while i < j and not S[j].isalpha(): j -= 1
    #         S[i], S[j] = S[j], S[i]
    #         i, j = i + 1, j - 1
    #     return "".join(S)
def main():
    S = "Test1ng-Leet=code-Q!"
    myResult = Solution()
    print(myResult.reverseOnlyLetters(S))

if __name__ == '__main__':
    main()

"""
没有考虑example3 
length = len(S)
# Sp = S.split("-")
Sp = re.split('=|-|!|\?',S)
print(Sp)
reSp = "".join(Sp)
reSp = list(reSp)
reSp.reverse()
# strreSp = "".join(reSp)
# print(strreSp) # jIhgfEdCba
pos = []
for i in range(length):
    if S[i] == '-':
        pos.append(i)
print(pos)
i = 0
k = 0
while i<length:
    # print(i)
    if i == pos[k]:
        reSp.insert(i,'-')
        k += 1
    if k == len(pos):
        return "".join(reSp)
    i+=1
# print(reSp)
"""