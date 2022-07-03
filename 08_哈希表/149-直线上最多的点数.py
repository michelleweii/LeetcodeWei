"""
返回共线的点，最多的点数。
至少有1个点是答案。
枚举一个定点，有多少个点斜率是相同的。如果2个点斜率相同，说明和中心点是在同一条直线上的。+定点（中心点）
对2个点计算他们的斜率是多少,把斜率做hash。

特殊情况：
1、垂直直线上的点，垂直直线的斜率是正无穷;
2、重合的点，存在2点重合。

hash_map
k:斜率
v:出现多少次
"""
class Solution:
    def maxPoints(self, points):
        if not points:return 0
        res = 1
        for i in range(len(points)):
            verticals = 1 # 竖直斜率出现的次数，在一条垂直直线上的点
            duplicates = 0 # 除了中心点，和我当前点重合的点有多少个？
            for j in range(i+1, len(points)):
                if points[i][0] == points[j][0]: # 当x轴一样
                    verticals+=1
                    if points[i][1] == points[j][1]: # 当y轴一样
                        duplicates+=1

            # 其他点
            hash_map = {}
            for j in range(i + 1, len(points)):
                if points[i][0] != points[j][0]:
                    slope = (points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                    # 如果不存在，则有当前点+中心点
                    if not hash_map.get(slope,0): hash_map[slope]=2
                    else: hash_map[slope] += 1
                    res = max(res, hash_map[slope]+duplicates)

            res = max(res, verticals)
        return res

if __name__ == '__main__':
    points = [[1,1],[2,2],[3,3]] # 3
    # points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] # 4
    res = Solution()
    print(res.maxPoints(points))