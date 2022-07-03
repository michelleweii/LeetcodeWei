"""
easy 同向双指针
2021-07-19
需要重做
"""
class Solution:
    def findContinuousSequence(self, target):
        j = 1 # right 右端点
        s = 1 # 序列和
        res = []
        for i in range(1, target):
            # 当i固定时，right最远的点
            while s<target:
                j+=1
                s+=j
            # print(i,j, s)
            if s==target and j-i+1>1:
                path = []
                for k in range(i, j+1):
                    path.append(k)
                res.append(path[:])
            s -= i
        return res




if __name__ == '__main__':
    target = 7
    print(Solution().findContinuousSequence(target))