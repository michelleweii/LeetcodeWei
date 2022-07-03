"""
middle 2021-12-23 贪心（这题好像没什么意义）
https://leetcode-cn.com/problems/task-scheduler/solution/tong-zi-by-popopop/
总排队时间 = (桶个数-1) * (n+1) + 最后一桶的任务数
"""
class Solution:
    def leastInterval(self, tasks, n): #List[str], n: int) -> int:
        # 1、统计max_frequency
        import collections
        counter = collections.Counter(tasks) # 使用就是字典
        # print(counter) # Counter({'A': 3, 'B': 3})
        # 每组个数+remains
        # aabbc, maxfreq=2, n=2, [a b c| a b _], _就是remains的位置，因为数组已经结束了，不用再idle了
        # pairs = (maxfreq-1)*(n+1)
        # res = pairs+remains
        maxfreq = 0 # 单词的最大频率
        remains = 0
        for val in counter.values():
            if val>maxfreq:
                maxfreq = val
                remains=1
            # 如何理解? 最后一桶的任务数（只有满足maxfreq才会有出现，因为不满足的总是能在空闲位置将其插入）
            elif val==maxfreq:
                remains+=1
        # print(remains) # 2
        # len(tasks)
        return max(len(tasks), (maxfreq-1)*(n+1)+remains)
    # 首先整个题目只有两种情况：1.存在空闲。2.不存在空闲。
    # 在第一种情况的时候即有空闲块：这时候的NUM2是不满足整个调度算法的要求的，所以我们只能取NUM1，
    # 此时的NUM1肯定比NUM2大。

    # 在第二种情况的时候即没有空闲块：
    # 这时候NUM1可能会出现不满足调度算法的要求的答案，比如：["A", "A", "A", "B", "B", "C", 'C', 'D'], 2 这种情况，
    # 此时的NUM1是7，明显不满足要求。所以此时只能取较大的数NUM2=8。

if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(Solution().leastInterval(tasks, n))