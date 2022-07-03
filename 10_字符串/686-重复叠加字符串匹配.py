"""
middle
kmp
# 在字符串b的长度范围内循环累加a并且判断是否存在子串，
# 但要注意边界，所以循环结束后如果不存在，需要在累加一次并进行判断。
"""
import copy
class Solution(object):
    def repeatedStringMatch(self, A, B):
        tmpA = copy.copy(A)
        lenb = len(B)
        count = 1
        while len(A)<lenb:
            A = A + tmpA
            count += 1
        # print(A)
        # print(count)
        if B in A:
            return count
        A = A + tmpA
        # print(A)
        count += 1
        if B in A:
            return count
        return -1
        # if set(A)!=set(B):
        #     return -1
        # tmp = A
        # i = 2
        # while i<10000:
        #     if B in A:
        #         return i-1
        #     if len(B)==len(A)-len(tmp):
        #         return -1
        #     else:
        #         A=tmp*i
        #         i+=1
        # return -1

if __name__ == "__main__":
    A = "abc"
    B = "cabcabca"
    myresult = Solution()
    print(myresult.repeatedStringMatch(A, B))
