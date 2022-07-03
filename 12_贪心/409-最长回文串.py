"""
easy 2022-05-13 贪心
"""
# 最长的回文数，只要字母是偶数个时，全都可以拿来用；
# 如果字母个数是奇数时，大于1的时候，可以舍掉一个字母，只用里面的偶数个构成字符串；
# 单个字母最多可以用一个，放在字母的最中间。
import collections
class Solution(object):
    def longestPalindrome(self, s):
        ans=0
        count=collections.Counter(s)
        for ch in count.values():
            ans += ch//2 *2 # 在回文串的左侧和右侧分别放置
            if ans%2==0 and ch%2==1: # 有任何一个字符的出现次数为奇数，就可以aba
                ans+=1
        return ans
        # myDict = collections.Counter(s)
        # max_length = 0
        # odd = 0
        # for i in myDict.keys():
        #     if myDict[i]%2 == 0:
        #         # 为偶数时，直接相加
        #         max_length += myDict[i]
        #     else:
        #         # 当d=3的时候，可以只用2个d构成字符串
        #         # 如果d=1,max_length=0,odd=1
        #         max_length += myDict[i]-1
        #         odd = 1
        # return (max_length+odd)


if __name__ == '__main__':
    s = "ccc"
    myResult = Solution()
    print(myResult.longestPalindrome(s))