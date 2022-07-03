"""
middle 2021-12-17 贪心
https://programmercarl.com/0452.%E7%94%A8%E6%9C%80%E5%B0%91%E6%95%B0%E9%87%8F%E7%9A%84%E7%AE%AD%E5%BC%95%E7%88%86%E6%B0%94%E7%90%83.html
1、按照气球的起始位置排序
2、从前向后遍历气球数组，靠左尽可能让气球重复；
3、如果气球重叠了，重叠气球中右边边界的最小值 之前的区间一定需要一个弓箭。

看链接的图：可以看出首先第一组重叠气球，一定是需要一个箭，气球3，的左边界大于了 第一组重叠气球的最小右边界，所以再需要一支箭来射气球3了。
"""
# 而且寻找重复的气球，寻找重叠气球最小右边界，其实都有代码技巧。
# 求重复区间
class Solution:
    def findMinArrowShots(self, points):
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[0]) # 按照第一个元素升序，左边界排序
        # print(points) # [[1, 6], [2, 8], [7, 12], [10, 16]]
        result = 1
        # print(points[0][0])
        for i in range(1, len(points)):
            # 气球i和气球i-1不挨着，注意这里不是>=
            # 如果一个气球的左边界>了，最小右边界，那么需要一个箭对之前的重叠气球戳一下
            if points[i][0] > points[i-1][1]: # 不挨着
                result += 1 # 如果后面一个区间的开始大于前一个区间的结尾 就需要新增一支箭。
            else: # 挨着
                # 更新重叠气球最小右边界
                # print(i)
                points[i][1] = min(points[i][1], points[i-1][1])

        return result


if __name__ == '__main__':
    # x方向上[气球开始index，结束index]
    points = [[10, 16], [2, 8], [1, 6], [7, 12]] # 2
    print(Solution().findMinArrowShots(points))