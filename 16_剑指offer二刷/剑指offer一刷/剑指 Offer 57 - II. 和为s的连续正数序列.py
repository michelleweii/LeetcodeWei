class Solution:
    def findContinuousSequence(self, target):
        i, j = 1, 1 # 题目要求正整数，1+14=15这种才算正整数。不过题目要求连续正整数，1+14=15故不符合s
        s = 1
        res = []
        for i in range(1,target+1):
            while s<target:
                j += 1
                s += j

            if s==target and j-i>0:
                line = []
                for k in range(i,j+1):
                    line.append(k)
                res.append(line)

            s -= i
        return res

if __name__ == '__main__':
    target = 9
    print(Solution().findContinuousSequence(target))