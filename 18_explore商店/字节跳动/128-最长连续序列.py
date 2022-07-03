
# 2022-02-25
class Solution:
    # 时间复杂度
    # 1、把数组转换成hashmap 使得查找的速度变成O（1）
    # 2、确保查找序列时是从最小点开始的，如果还有更小点就直接跳过，这也是减少复杂度的重点。
    # 所以，我理解的应该最终复杂度是O(2N)
    def longestConsecutive_hash(self, nums):
        if not nums:return 0
        # 每次以x为起点，找x+1,x+2,x+y，res=y-x+1
        hashmap = {}
        res = 0
        for i in range(len(nums)):
            hashmap[nums[i]]= i
        for x in hashmap:
            # print(x)
            y = x
            tmp = x
            if x-1 not in hashmap:
                # print(x, "ok")
                while x+1 in hashmap:
                    y += 1
                    # print(x + 1)
                    x += 1
                x = tmp
                res = max(res, y - x + 1)
        return res

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    # 最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
    #     nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] # 9
    print(Solution().longestConsecutive_hash(nums))
    # nums = [0,-1] # 2