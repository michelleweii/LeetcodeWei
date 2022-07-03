"""
middle 2021-12-06 贪心
https://programmercarl.com/0134.%E5%8A%A0%E6%B2%B9%E7%AB%99.html#%E6%80%BB%E7%BB%93
"""
# for循环适合模拟从头到尾的遍历，而while循环适合模拟环形遍历，要善于使用while！
class Solution:
    def canCompleteCircuit(self, gas, cost):
        # i出发，到i+1，剩余油量 gas[i]-cost[i]
        # 到i+1,可以+gas[i+1]
        start = 0
        rest_sum = 0 # 每个加油站的剩余量rest[i]，逐步累加
        total_sum = 0 # 所有加油站的总量
        # i从0开始累加rest[i]，和记为rest_sum，一旦rest_sum<0，
        # 说明[0, i]区间都不能作为起始位置，起始位置从i+1算起，再从0计算rest_sum。
        for i in range(len(gas)):
            rest_sum += gas[i] - cost[i]  # 每个加油站的剩余量rest[i]
            total_sum += gas[i] - cost[i]
            if rest_sum < 0: #  当前累加rest[i]和 = rest_sum 一旦小于0，车根本开不到下一个加油站
                rest_sum = 0 # rest_sum 从0开始，归零，继续下一个加油站当做出发点开始累加
                start = i + 1 # 起始位置更新为i+1

        # 如果总油量减去总消耗大于等于零那么一定可以跑完一圈，
        # 说明 各个站点的加油站 剩油量rest[i]相加一定是大于等于零的
        if total_sum < 0: return -1 # 说明怎么走都不可能跑一圈了
        return start

"""
暴力做法--遍历每一个加油站为起点的情况，模拟一圈。
如果跑了一圈，中途没有断油，而且最后油量大于等于0，说明这个起点是ok的。

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        for (int i = 0; i < cost.size(); i++) {
            int rest = gas[i] - cost[i]; // 记录剩余油量
            int index = (i + 1) % cost.size();
            while (rest > 0 && index != i) { // 模拟以i为起点行驶一圈
                rest += gas[index] - cost[index];
                index = (index + 1) % cost.size();
            }
            // 如果以i为起点跑一圈，剩余油量>=0，返回该起始位置
            if (rest >= 0 && index == i) return i;
        }
        return -1;
    }
};
"""

if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(gas,cost))
# https://leetcode-cn.com/problems/gas-station/