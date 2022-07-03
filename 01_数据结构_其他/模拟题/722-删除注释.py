"""
middle 2022-06-22 模拟题
删除//，/**/ 这两种注释中的内容
https://leetcode.cn/problems/remove-comments/solution/python3-fen-qing-kuang-chu-li-722-by-lio-sw3q/
"""
class Solution:
    def removeComments(self, source):# List[str]) -> List[str]:
        inBlock = False     #用于判断当前是否处于注释中, 一开始是不在注释中
        res = []
        newLine=[]
        for line in source: #遍历所有字符串
            i = 0
            if not inBlock: #如果当前不在注释中，说明是新的一行，无论尾注释在哪里
                newLine = []
            while i < len(line):    #遍历当前行
                if line[i:i + 2] == "/*" and not inBlock:   #注释起始位置
                    inBlock = True
                    i += 1
                elif line[i:i + 2] == "*/" and inBlock:     #注释结束位置
                    inBlock = False
                    i += 1
                elif line[i:i + 2] == "//" and not inBlock: #当前行跳过，全部注释
                    break
                elif not inBlock:                           #如果没有注释，则添加到新行里面
                    newLine.append(line[i])
                i += 1
            if newLine and not inBlock:                     #如果新行有数据，且当前不在注释中，则更新到结果
                res.append("".join(newLine))
        return res

source = ["a/*comment", "line", "more_comment*/b"]
print(Solution().removeComments(source))