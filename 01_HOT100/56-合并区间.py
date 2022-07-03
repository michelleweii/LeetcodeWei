"""
middle 2021-10-18 同向双指针（字节、腾讯、百度）
双指针思路：根据第一个元素升序，前后看谁大谁小, intervals[l]and intervals[r]
题目：合并所有重叠的区间
双指针视频：https://www.bilibili.com/video/BV11t411J7zV?from=search&seid=15285910176650766234&spm_id_from=333.337.0.0
贪心解题思路：https://programmercarl.com/0056.%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.html#_56-%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4
"""
class Solution:
    def merge(self, intervals):
        if not intervals:return intervals
        intervals.sort() # 默认先按第一个元素升序，再按第二个元素升序
        # print(intervals) # [[1, 3], [2, 6], [8, 10], [15, 18]]
        l, r = 0, 1
        while r<len(intervals): # 这里一定要动态的变化
            x1,y1 = intervals[l]
            x2,y2 = intervals[r]
            if x2>y1:
                l,r = l+1,r+1
            else:
                intervals[l] = [x1, max(y1,y2)]
                intervals.pop(r) # 删除指定index
        return intervals

if __name__ == '__main__':
    intervals = [[1, 3],  [8, 10], [2, 6], [15, 18]]
    # [[1, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))