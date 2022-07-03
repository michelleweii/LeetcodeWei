"""
hard 2021-12-23 dp/优先队列
（思路）https://leetcode-cn.com/problems/minimum-number-of-refueling-stops/solution/xian-gao-ming-bai-qi-che-wei-shi-yao-xu-qkpug/
（代码）https://leetcode-cn.com/problems/minimum-number-of-refueling-stops/solution/cpython3java-1dp-by-hanxin_hanxin-f4ef/
思路：此题本意还是消耗过程，我们采用逆向思维：化消耗过程为收集过程。
汽车为什么需要加油？1.当前油箱中的油不能到达下一个加油站+2.当前油箱中的油不能到达目的地
# 汽车行驶过程中，我们的汽车油箱的油可能不够支持我们到达下一个加油站或者目的地了，此时我们需要加油（看看前提条件：汽车为什么需要加油？），
# 这时我们后备箱收集的加油站就派上用场了，选择最大的加油站加上油即可，如果还要加油，则再选择一个次大的加油站。。。。
"""
# 百度笔试（贪心+优先队列）
# 假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
# 当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
# 为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
# 注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

# from queue import PriorityQueue # 没有pop()的方法，就是get()元素之后，该元素还是在queue里
# 转用heapq
import heapq
class Solution:
    # 优先队列（大根堆）
    def minRefuelStops(self, target, startFuel, stations):
        res = 0
        # 初始边界条件, 不用加油现有汽油能到终点
        if startFuel>=target: return 0
        q = [] # 默认是小根堆，但是我们需要大根堆，找到“路过的，最大的加油站加上油”
        cur_fuel = startFuel # 当前汽车汽油
        distance = 0 # 已经走过的路程

        i = 0
        # 还有加油站或者后备箱里面还有备用油可加
        while i<len(stations) or q:
            # (stations[i][0]-distance) 我走过的距离
            # (cur_fuel-(stations[i][0]-distance))>= 0 保证我现有的油量能到下一点
            # 如果我能一直走，先把加油站记录
            while (i<len(stations) and (cur_fuel-(stations[i][0]-distance))>= 0):
                heapq.heappush(q,(-stations[i][1], stations[i][0]))
                i += 1
            # 退出while循环
            # 此时，两种情况：1、当前油箱的油量，已经不够到达下一个加油站了，2、已经走完了所有加油站
            # 判断是否能够到达终点
            if cur_fuel>=(target-distance):
                return res

            # 还有备用油
            if q:
                max_station = heapq.heappop(q) # 选择路过加油站中，油量最多的
                print(max_station) # (-60, 10)
                # 更新汽油
                # -max_station[0] # 该位置汽油
                # max_station[1] # 该位置距离
                # (max_station[1]-distance) 上次pos到当前pos的距离
                cur_fuel -= (max_station[1]-distance) # 我到该加油站消耗的
                cur_fuel += (-max_station[0]) # 新增汽油
                distance = max_station[1] # 更新已经走过的距离
                res += 1
            else:
                # 没有了备用油，也到不了终点
                return -1
        return res if cur_fuel >= (target- distance) else -1

if __name__ == '__main__':
    target = 100
    startFuel = 10
    stations = [[10, 60], [20, 30], [30, 30], [60, 40]] #2
    # target = 100
    # startFuel = 1
    # stations = [[10, 100]] #-1
    print(Solution().minRefuelStops(target, startFuel, stations))
    # [公里，+汽油]
# 我们出发时有 10 升燃料。
# 我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
# 然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
# 并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
# 我们沿途在1and4两个加油站停靠，所以返回 2 。