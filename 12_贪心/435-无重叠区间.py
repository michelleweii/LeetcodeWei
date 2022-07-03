"""
middle 2021-12-22 贪心
题目：找到需要移除区间的最小数量，使剩余区间互不重叠。
思路：
1、按照右边界排序，从左向右记录非交叉区间的个数。最后用区间总数减去非交叉区间的个数就是需要移除的区间个数了。
2、求非交叉区间的最大个数
3、右边界排序之后，局部最优：优先选右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，从而尽量避免交叉。全局最优：选取最多的非交叉区间。
【直接求重复的区间是复杂的，转而求最大非重复区间个数。】
"""
# 总结：类似lc452，求反过程。
# 本题记录非重叠个数，concat，总数-非重叠个数=重叠个数

# 难点一：一看题就有感觉需要排序，但究竟怎么排序，按左边界排还是右边界排。
# 难点二：排完序之后如何遍历，如果没有分析好遍历顺序，那么排序就没有意义了。
# 难点三：直接求重复的区间是复杂的，转而求最大非重复区间个数。
# 难点四：求最大非重复区间个数时，需要一个分割点来做标记。
class Solution:
    def eraseOverlapIntervals(self, intervals): #: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        # intervals.sort(key=lambda x: x[1]) # 按照第二个元素升序->按照右边界排序
        # print(intervals) # [[1, 2], [2, 3], [1, 3], [3, 4]]
        intervals.sort()
        count = 0 # 统计移除数组个数
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]: # 发生重叠
                count+=1
                # 按照前两个数组中右边界最小的那个来重置右边界
                intervals[i][1]=min(intervals[i-1][1],intervals[i][1])
        return count

if __name__ == '__main__':
    # intervals = [[1, 2], [1, 2], [1, 2]] # 2
    intervals = [ [1,2], [2,3], [3,4], [1,3] ] # 1 # 移除 [1,3] 后，剩下的区间没有重叠。
    print(Solution().eraseOverlapIntervals(intervals))