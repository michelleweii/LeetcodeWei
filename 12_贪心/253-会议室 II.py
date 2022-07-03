"""
middle 2022-04-28 上下车问题
【05-05简单总结】：
下一个新item开始了，如果上一个还没有结束，count+1,并将新item的结束时间入小顶堆；
如果不是，上一个结束时间已用，出堆，新item的结束时间入小顶堆。
------------------------------------------------------------
https://leetcode-cn.com/problems/meeting-rooms-ii/solution/hui-yi-shi-ii-jian-dan-tan-xin-you-xian-x7kuo/
# 题目：给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
返回 "所需会议室的最小数量" 。
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
总结：
"""
# 解决方案，
# 1. 优先级队列，存放当前正在开的会的结束时间，优先级队列中元素的个数表示当前有多少个会正在开，需要的会议室的数量也是该个数。
# 2. 小顶堆
# 3. 贪心

# 首先按照开始时间排序，遍历会议，看当前会议的开始时间是否小于已经安排会议的最早结束时间，
#
# 如果小于：则需增加会议室，同时添加当前结束时间到结束时间列表
# 如果大于等于：则不需增加，但是需要将之前的最早结束时间替换为当前会议的结束时间
# 因为每次都要找最早结束时间，所以我们用优先队列来存储结束时间列表。
#【优先队列】它的“优先”意指取队首元素时，有一定的选择性，即根据元素的属性选择某一项值最优的出队~
import heapq
class Solution:
    def minMeetingRooms(self, intervals): #List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        # end_time是小顶堆，pop()弹出的就是最小值。
        end_time=[intervals[0][1]] # 结束时间
        count=1
        for i in range(1,n):
            # 开始时间<结束时间
            # 发生重叠了，需要多一间房子
            if intervals[i][0]<end_time[0]:# 会议开始时间比最早结束的还要早，需增加会议室
                count+=1
                heapq.heappush(end_time,intervals[i][1]) # 将该会议室的结束时间添加进入小顶堆
            else:# 可以在最早结束的会议之后开始当前会议，之前的最早结束时间变成当前会议结束的时间
                # 一定要先将当前的最小元素弹出
                heapq.heappop(end_time)
                heapq.heappush(end_time,intervals[i][1])
        return count


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().minMeetingRooms(intervals))

