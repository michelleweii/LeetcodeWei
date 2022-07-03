"""
middle 2022-03-02 指针模拟题/二分法
intervals = [[1,3],[6,9]], newInterval = [2,5]
[[1,5],[6,9]]
[二分法题解](https://leetcode-cn.com/problems/insert-interval/solution/python3er-fen-fa-by-simpleson/)
[秒懂力扣区间题目：重叠区间、合并区间、插入区间](https://mp.weixin.qq.com/s/ioUlNa4ZToCrun3qb4y4Ow)
"""
# 相关题目：LC56合并区间、LC57插入区间、LC435无重叠区间
# https://leetcode-cn.com/problems/insert-interval/solution/57-cha-ru-qu-jian-mo-ni-cha-ru-xiang-jie-by-carlsu/
class Solution:
    # 1.找到需要合并的区间
    # 2.合并区间
    #   2.1 intervals[index]需要合并
    #   2.2 intervals[index]不用合并，插入区间直接插入就行
    # 3.处理合并区间之后的区间
    def insert(self, intervals, newInterval):
        res = []
        index = 0 # intervals的索引
        # 1. 找到需要合并的区间（过掉不重叠的区间）
        while index<len(intervals) and intervals[index][1]<newInterval[0]:
            # 当 intervals[index][1]>newInterval[0] 就要合并了
            res.append(intervals[index])
            index+=1
        # 2. 合并区间
        # 为什么这样合并？看图
        # https://leetcode-cn.com/problems/insert-interval/solution/shou-hua-tu-jie-57-cha-ru-qu-jian-fen-cheng-3ge-ji/
        # 现在看重叠的。我们反过来想，没重叠，就要满足：绿区间的左端，落在蓝区间的屁股的后面，反之就有重叠：绿区间的左端 <= 蓝区间的右端。
        while index<len(intervals) and intervals[index][0]<=newInterval[1]:
            newInterval[0]=min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index+=1

        res.append(newInterval)
        # 3.处理合并区间之后的区间
        while index<len(intervals):
            res.append(intervals[index])
            index += 1
        return res

"""
"""
# middle 2022-03-02 双指针
# 一个list一个list的滑
"""
# LC57前，先完成LC56，2022-03-02 AC
class Solution:
    def merge(self, intervals): #List[List[int]]) -> List[List[int]]:
        if not intervals:return []
        intervals.sort()
        # print(intervals)
        l,r=0,1
        while r<len(intervals):
            if intervals[r][0]<=intervals[l][1]:
                intervals[l][1] = max(intervals[r][1], intervals[l][1])
                intervals.pop(r)
            else:
                l+=1
                r+=1
        return intervals

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[15,18],[8,10]]
    # [[1,6],[8,10],[15,18]]
    print(Solution().merge(intervals))
"""

if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals,newInterval))