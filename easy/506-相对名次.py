# 用map
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # rs = []
        # ori = nums.copy()
        # # print(ori)
        # nums.sort() # 小到大
        # award = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        # k = 4
        # res = []
        # tmp=nums[0:-3]
        # for i in tmp[::-1]: #[2,1]
        #     rs.append(k)
        #     k+=1
        # ans = award+list(map(str,rs))
        # print(dict(zip(nums[::-1],ans)))
        # # dict1 = dict(zip(nums[::-1],ans))
        # # print(dict1.items())
        # # i = 0
        # # for i in range(len(ori)):
        # #     res.append(dict1.get(nums[i]))
        # print(nums[::-1])
        # return list(map(dict(zip(nums,ans)).get,nums[::-1]))
        # # print(res)
        # # return res
        sort = sorted(nums)[::-1] # 和nums.sort()不同，不改变nums的顺序
        print(sort)
        print(nums)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)).get, nums)



def main():
    nums = [10,3,8,9,4]
    myResult = Solution()
    print(myResult.findRelativeRanks(nums))

if __name__ == '__main__':
    main()