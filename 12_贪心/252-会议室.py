"""
easy 2022-05-06 贪心
题目：给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi]，
请你判断一个人是否能够参加这里面的全部会议。
思路:如果上一个会议先开始了，而且下一个会议开始了它还没结束，就不行
"""
class Solution:
    def canAttendMeetings(self, intervals): #List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda x: x[0]) # [[15, 30], [15, 10], [15, 20]]
        print(intervals)
        pretail=-1
        for i in range(len(intervals)):
            if intervals[i][0]<pretail:return False
            pretail=intervals[i][1]
        return True

# class Solution:
#     def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
#         # 根据会议开始时间排序
#         intervals.sort(key=lambda x:x[0])
#         return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))

if __name__ == '__main__':
    intervals = [[15, 30], [15, 10], [15, 20]] # F
    # intervals = [[7, 10], [2, 4]] # T
    print(Solution().canAttendMeetings(intervals))