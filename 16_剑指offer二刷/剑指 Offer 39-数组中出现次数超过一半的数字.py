"""
easy
hashmap 2021-07-15 once ok
摩尔投票法 https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/
"""
class Solution:
    # hashmap
    def majorityElement(self, nums):
        if not nums:return nums
        n = len(nums)
        half = n//2
        hash_map = {}
        for x in nums:
            hash_map[x] = hash_map.get(x,0)+1
            if hash_map.get(x,0)>half:
                return x
    # 摩尔投票法, 核心理念为 票数正负抵消
    def majorityElement1(self, nums):
        cnt = 0
        val = -1
        for x in nums:
            if not cnt:
                val=x
                cnt+=1
            else:
                if x==val:cnt+=1
                else:cnt-=1
        return val




if __name__ == '__main__':
    n = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().majorityElement(n))