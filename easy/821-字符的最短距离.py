# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        rs = []
        pos = []
        # length = len(S)
        for pos_i,pos_val in enumerate(S):
            if pos_val==C:
                pos.append(pos_i)
        print(pos)
        # 用绝对值计算的方法没有想到

        for i in range(len(S)):
            tmp = []
            for j in pos:
                tmp.append(abs(i-j))
            rs.append(min(tmp))
        print(rs)

"""
        # method two 寻找每个字符左右相邻的C字符, 简化运算
        res = []
        for i in range(len(S)):
            left , right = S[i-len(S)::-1].find(C) , S[i:].find(C)
            
            # 反向,t,正向
            # teelevol,t,tcode
            # min(1,4)=1
            
            if left == -1: left = 10000
            if right == -1: right = 10000
            res.append(min(left , right)) 
        return res

"""


def main():
    S = "loveleetcode"
    C = 'e'
    myResult = Solution()
    print(myResult.shortestToChar(S,C))

if __name__ == '__main__':
    main()

