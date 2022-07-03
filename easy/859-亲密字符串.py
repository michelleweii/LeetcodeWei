"""
分析：出现亲密字符串的结果有两种：
(1)第一种是两个字符串有且只有两个位置的字符不相同且并且交换两个位置的字符能使两字符串相同；
(2)另一种情况是两个字符串完全相同并且字符串中存在至少有一个字符出现了两次的情况，
此时交换这两个相同的字符也可使两字符串相同。

在代码中首先判断两字符串长度是否相同，长度不同无论怎么交换字符也不能使两字符串相等。
接下来设置一个数组存放遍历字符串得到的两字符串不相等的字符索引。
根据数组长度及内容判断两字符串是否为亲密字符串。
当数组长度为0时，判断字符串中是否有相同字符元素，如果有则返回true，如果没有则返回false。
当数组长度为2时，判断A[k]与[j]、A[j]与B[k]是否都相等，相等则返回true，不相等返回false。
当数组长度为其余数的时候，都返回false。

"""
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # a1 = list(set(list(A))) # 这个set是随机去重的
        if len(A)!=len(B):
            return False
        pos=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                pos.append(i)
        # print(pos)
        if len(pos)==0:
            # 判断一个list中是否有相同元素
            for i in A:
                if A.count(i)>=2:
                    return True
            return False
        elif len(pos)==2:
            if A[pos[0]] == B[pos[1]] and A[pos[1]] == B[pos[0]]:
                return True
            return False
        else:
            return False






def main():
    A = "aba"
    B = "aba"
    myresult = Solution()
    print(myresult.buddyStrings(A, B))

if __name__ == "__main__":
    main()