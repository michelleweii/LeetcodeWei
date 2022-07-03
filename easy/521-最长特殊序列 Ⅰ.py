# 看不懂题目
# 空序列为所有字符串的子序列
"""
解题思路：
如果两个字符串A和B，如果A比B的长度大，那么A肯定不能由B删除某些字符得到啊，那么A的长度肯定就是这个最大长度了。

其次，如果A和B等长的话，看他们是不是相等的，如果相等的那么一个字符串肯定能由另外一个字符串不用删除都等得到。

最后如果A和B等长并且他们还不相等，那么其中字符串A肯定就不能由字符串B删除字符之后得到，因为人家本来长度都相等了，你再删除肯定短了嘛，不可能再相等了。
"""
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a)!=len(b): # a,b长度不同
            return max(len(a),len(b))
        elif len(a)==len(b) and a==b: #a,b等长，还相同
            return -1
        else: # a，b等长，不相同
            return len(a)





def main():
    a = "aefawfawfawfaw"
    b = "aefawfeawfwafwaef"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.findLUSlength(a, b))

if __name__ == '__main__':
    main()
