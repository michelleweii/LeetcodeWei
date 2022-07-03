"""
middle 2022-05-07 贪心
题目：求解删除被覆盖区间后的区间数==》求被覆盖的区间数
求区间问题的套路都是先排序然后画图找规律
【画图】https://leetcode-cn.com/problems/remove-covered-intervals/solution/sao-miao-xian-fa-by-liweiwei1419/
https://leetcode-cn.com/problems/remove-covered-intervals/solution/pai-xu-tan-xin-jian-dan-yi-dong-by-ybzdq-bmzw/
思路：
如果intervals[i][1](右端点)大于右边界max_right，则证明区间没有被前一个区间覆盖，此时将
右边界大于右边界max_right向右推进，更新为max(大于右边界max_right, intervals[i][1])，
以备下一次判断，如此循环遍历结束后返回的区间数
"""
class Solution:
    def removeCoveredIntervals(self, intervals): #List[List[int]]) -> int:
        n = len(intervals)
        if n<2:return intervals
        # 按照起点升序排列，起点相同时降序排列，对于这两个起点相同的区间，
        # 我们需要保证长的那个区间在上面（按照终点降序），这样才会被判定为覆盖，否则会被错误地判定为相交
        intervals.sort(key=lambda x:(x[0],-x[1]))
        # [[1, 4], [2, 8], [2, 6]]
        remove_cnt = 0
        max_right=intervals[0][1]
        for i in range(1, n):
            if intervals[i][1]<=max_right:
                remove_cnt+=1 #
            else:
                max_right=intervals[i][1]
        return n-remove_cnt

if __name__ == '__main__':
    intervals = [[1, 4], [2, 6], [2, 8]] # 2
    print(Solution().removeCoveredIntervals(intervals))