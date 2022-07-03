"""
middle 2022-02-23 最长数字连续序列（高频题wxg）
题目：# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
题目要求：找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。-->可以断开
要求时间复杂度O(N)
【动规】https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/dong-tai-gui-hua-python-ti-jie-by-jalan/
【1个哈希】https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/ha-xi-zui-qing-xi-yi-dong-de-jiang-jie-c-xpnr/
"""
"""
思路（以下代码动规思想）：
2个哈希表
1-左端点所代表的区间的长度。
2-右端点对代表的hash表长度。
区间内部hash值是没有用的。所求的是最长的长度。
计算当前数的区间长度为：cur_length = left + right + 1
"""
class Solution:
    # 时间复杂度
    # 1、把数组转换成hashmap 使得查找的速度变成O（1）
    # 2、确保查找序列时是从最小点开始的，如果还有更小点就直接跳过，这也是减少复杂度的重点。
    # 所以，我理解的应该最终复杂度是O(2N)
    def longestConsecutive_hash(self, nums):
        # 每次以x为起点，找x+1,x+2,x+y，res=y-x+1
        # 如何确定x? 如果存在x-1则不是起点，如果不存在x-1，那么该点可以成为起始点。
        hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        for x in nums:hashmap[x] = x
        res = 0
        for x in hashmap:
            # if not hashmap.get(x-1,0):
            # 如果x-1不存在，说明x可以当做起始点
            if (x-1) not in hashmap:
                y = x # 以当前数x向后枚举
                while (y+1) in hashmap: # 如果x+1存在，y++
                    y+=1
                res = max(res, y-x+1) # 更新答案
        return res

    # 进阶
    # https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/dong-tai-gui-hua-python-ti-jie-by-jalan/791527
    def longestConsecutive(self, nums):
        """
        用哈希表存储（每个端点值）对应（连续区间的长度）
        （1）取出其左右相邻数已有的连续区间长度 left 和 right
        （2）计算当前数的区间长度为：cur_length = left + right + 1
        （3）根据 cur_length 更新最大长度 max_length 的值
        （4）更新区间两端点的长度值
        """
        res = 0
        # key表示num: value表示num所在连续区间的长度
        # 举例，当hashmap的key为5，value为3时，这就表明当前有一个包含5且长度为3的连续区间，
        # 当然有多种可能，可以是[3,4,5],[4,5,6],[5,6,7]。
        left_hash_map = {}
        right_hash_map = {}
        for x in nums:
            # left为num-1所在连续区间的长度，更进一步理解为：左连续区间的长度
            left = right_hash_map.get(x-1,0) # x左边的点，它向左维护的长度
            # right为num+1所在连续区间的长度，更进一步理解为：右连续区间的长度
            right = left_hash_map.get(x+1,0) # x右边的点，它向右维度的长度
            # 当前连续区间的总长度left+1+right
            cur_x_len = left+1+right
            # 区间更新, 因x的加入，导致区间可能的合并
            # 更新当前连续区间左边界和右边界对应的区间长度
            left_hash_map[x-left] = max(left_hash_map.get(x-left,0), cur_x_len)
            right_hash_map[x+right] = max(right_hash_map.get(x+right,0), cur_x_len)

            res = max(res, cur_x_len)

        return res
    """
    class Solution(object):
    def longestConsecutive(self, nums):
        hash_dict = dict()
        
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                
                # 这里不是用于端点记录的，而是标记num已经在hash中，所以可以是随便一个值...
                hash_dict[num] = 'haha'
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
                
        return max_length
        
    解释：
    在代码中的left和right能够分别代表num-1的左连续区间的长度和num+1的右连续区间长度，那么为什么map中的value能够时而表示左区间的长度，时而表示右区间的长度呢？
    关键在于判断条件上：if (!map.containsKey(num))，这行代码表示num之前并未出现过。那么对于key=num-1来说，它的value表示的区间就只能是[num-value,num-1]，num-1只能是该区间的左边界值，而其它可能的连续区间都会包含num，不符合上述条件；
    同理，对于key=num+1来说，它的value表示的区间就只能是[num+1,num+value]，num+1只能是该区间的右边界值。
    当num已经出现了，这两个区间就可以被联通表示为[num-value1,num+value2]，当前连续区间的左右边界会发生变化，变为num-value1和num+value2，因此我们需要更新这两个边界点对应的区间长度。
    """

if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    # 最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
    #     nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] # 9
    print(Solution().longestConsecutive(nums))
    # nums = [0,-1] # 2
    print(Solution().longestConsecutive_hash(nums))
