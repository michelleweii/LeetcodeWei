"""
操作进行分解：
1、先将每个单词倒过来 "the sky is blue" -> "eht yks si eulb";
2、将整个字符串逆序;
o(n)
"""
class Solution:
    def reverseWords(self, s):
        if not s:return s
        s = s.strip() # 等价while(k<len(s) and k==' '):k+=1
        # 先把多余的空格删掉
        i,k=0,0
        while(k<len(s)):
            if s[k] != ' ':
                s[i],s[k] = s[k],s[i]
                i+=1
                k+=1
            else:
                s[i] = ' ' # 补上一个单词与单词之间的空格
                i+=1
                while (k<len(s) and s[k]==' '):k+=1 # 将空格都过滤了

        # 将每个单词翻转（内部翻转）
        for i in range(len(s)):
            j = i
            while(j<len(s) and s[j]!=' '): j+=1
            tmp = s[i:j][::-1]
            print(tmp)


        # 再翻转整个字符串






if __name__ == '__main__':
    strs = "hello world!"
    a = strs[1:3][::-1]
    # print(a)
    # print(strs.split()[::-1]) #['world!', 'hello']
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    # print(myResult.reverseWords(strs))

    # test
    strs = "ad bc"
    for i in range(len(strs)):

        j = i
        while(j<len(strs) and strs[j]!=' '):
            j+=1
        # print(j) # 5,12
        print(i, strs[i:j])
        i=j
        print('i:j ', i,j)

