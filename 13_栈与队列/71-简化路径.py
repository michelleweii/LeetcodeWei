"""
middle 2021-10-24
栈解决,把当前目录压入栈中,遇到..弹出栈顶,最后返回栈中元素.（这道题主要是题意不理解）
举个例子："/a//b////c/d//././/.."
先去掉双斜 /a/b/c/d/././.. 然后去掉 ‘.’ /a/b/c/d/.. 然后去掉‘..’ /a/b/c/
最后一个..代表返回父目录，也就是说目前目录是a/b/c/d，对应的父目录是a/b/c，所以返回a/b/c
---
1\如果是 . 或者 空字符串 则跳过
2\如果是.. 说明需要返回上一级，即弹出一个文件名，但是这里有一个细节需要注意，只有res非空的时候才能弹出，否则对于测试用例 '/../'不能通过
3\如果是普通的文件名，则加入res
"""
class Solution:
    def simplifyPath(self,path):
        stack = []
        path = path.split("/")
        print(path)

        for item in path:
            if item == "..":
                if stack : stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)

if __name__ == '__main__':
    # path = "/home/"
    path = '/../'
    print(Solution().simplifyPath(path))