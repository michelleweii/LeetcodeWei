"""
middle 2022-01-13 回溯|组合问题
# 求不同集合之间的组合，而LC77\LC216是求同一个集合中的组合!
https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html#%E5%9B%9E%E6%BA%AF%E6%B3%95%E6%9D%A5%E8%A7%A3%E5%86%B3n%E4%B8%AAfor%E5%BE%AA%E7%8E%AF%E7%9A%84%E9%97%AE%E9%A2%98
# 这个index不是之前的startIndex了。这个index是记录遍历第几个数字了，就是用来遍历digits的，同时index也表示树的深度。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.md
链接里的图很重要，有助于理解
"""
class Solution(object):
    def __init__(self):
        self.res = []
        self.path = ""
        self.hash_map = {'0': "", '1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    def letterCombinations(self, digits):
        if not digits:return self.res
        self.dfs(digits,0) # 0是从digits的第0位开始
        return self.res

    def dfs(self,digits,index):
        # 回溯函数没有返回值

        # 定义出口，终止条件就是如果index 等于 输入的数字个数（digits.size）了（本来index就是用来遍历digits的）
        if len(self.path) == len(digits):
            self.res.append(self.path)
            return
        # 确定单层遍历逻辑
        # 首先要取index指向的数字，并找到对应的字符集
        # 然后for循环来处理这个字符集，代码如下：
        letters = self.hash_map[digits[index]]  # 取出数字对应的字符集
        for letter in letters: # 控制树的第2层
            self.path += letter
            self.dfs(digits, index+1) # digits的下一个字符串 #递归，注意index+1，下一层要处理下一个数字了
            self.path = self.path[:-1] #  回溯

    """
    def letterCombinations(self, digits):
        # 存储结果的数组
        res = []
        inputstr = []
        if len(digits) == 0:
            return res
        hash_map = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        for i in digits:
            inputstr.append(hash_map[int(i)])
        # print(inputstr) # ['abc', 'def']
        # 闭包
        def dfs(cur_str,i,res):
            if len(cur_str)==len(inputstr): # abc def ghi
                res.append(cur_str)
                return
            for count in range(len(inputstr[i])): # abc
                dfs(cur_str+inputstr[i][count],i+1,res)

        dfs("",0,res)
        return res
    """


if __name__ == '__main__':
    digits ="23"
    print(digits[:-1]) #2
    print(Solution().letterCombinations(digits))