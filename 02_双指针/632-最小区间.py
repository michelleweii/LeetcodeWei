"""
hard 2022-05-22 双指针 类似LC76
映射了一层，滑动区间是组号
[看图]https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/solution/pai-xu-hua-chuang-by-netcan/
https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/solution/hua-dong-chuang-kou-de-tao-lu-zhao-dao-ke-xing-jie/g
"""
# 首先将 kk 组数据升序合并成一组，并记录每个数字所属的组，例如：
# [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# 合并升序后得到：
# [(0,1),(4,0),(5,2),(9,1),(10,0),(12,1),(15,0),(18,2),(20,1),(22,2),(24,0),(26,0),(30,2)]
# (解释一下，(0, 1) 这里表示数值 0 在第 1 个分组 [0,9,12,20] 中)
# 然后只看所属组的话，那么
# [1,0,2,1,0,1,0,2,1,2,0,0,2]
# 按组进行滑窗，保证一个窗口的组满足k组后在记录窗口的最小区间值。
from collections import defaultdict
class Solution:
    def smallestRange(self, nums):# List[List[int]]) -> List[int]:
        # (0, 1) 这里表示数值 0 在第 1 个分组 [0,9,12,20] 中
        lists=[]
        for i in range(len(nums)):
            for x in nums[i]:
                lists.append((x,i))
        lists.sort() # 根据第一位升序
        # print(lists)
        left,k=0,0
        res=[-10**9,10**9]
        curmap={}
        for right in range(len(lists)):
            # 判断所属组号
            if lists[right][1] not in curmap.keys():
                k+=1
                curmap[lists[right][1]]=1 # 所属组号的个数（该区间有1个数）
            else:
                curmap[lists[right][1]] += 1
            # 说明当前窗口，每组的数字都有覆盖
            if k==len(nums):
                while curmap[lists[left][1]]>1: # 寻找最优解
                    curmap[lists[left][1]]-=1
                    left+=1
                if res[1]-res[0]>lists[right][0]-lists[left][0]: # 数字差
                    res[1],res[0]=lists[right][0],lists[left][0]
        return res

        # dict_set = defaultdict(set)
        # for i in range(len(nums)):
        #     for x in nums[i]:
        #         dict_set[x].add(i)
        # print(dict_set)

if __name__ == '__main__':
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    # 输出：[20,24]
    # 解释：
    # 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
    # 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
    # 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
    print(Solution().smallestRange(nums))


