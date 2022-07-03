"""
middle 2022-03-02 二分查找+双指针
https://leetcode-cn.com/problems/heaters/solution/gong-shui-san-xie-er-fen-shuang-zhi-zhen-mys4/
二分的核心：二段性
    在以 res 为分割点的数轴上具有「二段性」：
    数值<res 的半径无法覆盖所有的房子；
    数值>=res 的半径可以覆盖所有房子。

考虑如何实现 check 函数。
先对 houses 和 heaters 进行排序，使用 i 指向当前处理到的 houses[i]；
j 指向 可能 覆盖到 houses[i] 的最小下标 heaters[j]；
x 代表当前需要 check 的半径。

当且仅当 heaters[j]+x<houses[i] 时，houses[i] 必然不能被 heaters[j] 所覆盖，此时让 j 自增。
找到合适的 j 之后，再检查 heaters[j]−x<=houses[i]<=heaters[j]+x 是否满足，即可知道 houses[i] 的覆盖情况。

"""
# https://leetcode-cn.com/problems/heaters/solution/er-fen-cha-zhao-de-jie-fa-by-li-xian-sen/
# 1、找到每个房屋离加热器的最短距离（即找出离房屋最近的加热器）。
# 2、在所有距离中选出最大的一个max(res)即为结果。

# 右边 >=item的最小数（可能不存在，用哨兵）
# 左边 <=item的最大数（可能不存在，用哨兵）

# 对任何一个房间，要不从他前面的取暖器采暖，要不从他后面的取暖。把这个思考清楚了，按照这个想法去实现代码很简单。
import bisect
class Solution:
    # 方法1
    def findRadius(self, houses, heaters):
        res = [] # 存放每个房屋与加热器的最短距离
        heaters.sort()



    # 方法2
    def findRadius2(self, houses, heaters):
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        res = 0 # 存放每个房屋与加热器的最短距离
        # for house in houses:
        #     loc = bisect.bisect_left(heaters, house)
        #     print("loc", loc)
        #     res = max(res, min(house - heaters[loc - 1], heaters[loc] - house))
        # return res

        # print(heaters) # [-inf, 2, inf]
        for house in houses:
            l, r = 0, len(heaters)-1
            # 在heaters中找到目标元素house第一次出现的位置
            while(l<r):
                mid = (l+r)//2
                if heaters[mid]>=house:r=mid  # 这里卡住
                else:l=mid+1

            # heaters[left] <= house:
            # 若该加热器的坐标值小于house ，说明该加热器的坐标与house之间没有别的加热器

            # else:
            # 说明house介于left和left-1之间，房屋到加热器的最短距离就是left和
            # left-1处加热器与house差值的最小值.
            res = max(res, min(house-heaters[l-1], heaters[l]-house)) #将距离房子最近的供暖器距离纳入统计
        return res


if __name__ == '__main__':
    # houses = [1,2,3] heaters = [2] # 1
    houses = [1, 2, 3, 4]
    heaters = [1, 4] # 1
    # houses = [1,5], heaters = [2] # 3,4,5 res=3
    res = Solution()
    print(res.findRadius(houses, heaters))