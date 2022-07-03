"""
middle 2021-12-12 单调递减栈
动图很好https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/
"""
class Solution:
    def dailyTemperatures(self, temperatures): #List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        res = [0]*n
        for i in range(n):
            # 单调递减栈
            while stk and temperatures[i]>temperatures[stk[-1]]:
                index = stk.pop() # 大于
                res[index] = i-index
            stk.append(i)
        return res

if __name__ == '__main__':
    temperatures = [30, 40, 50, 60]
    print(Solution().dailyTemperatures(temperatures))