class Solution(object):
    def findMaxConsecutiveOnes1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls1 = [str(i) for i in nums]
        str_nums = "".join(ls1) # 原来nums里是数字不是str，所以这一个步骤没效果
        # print(str_nums) # 110111


        count = 1
        rs = []
        if len(nums)==1 and nums[0]==1:
            return 1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and nums[i]==1:
                count += 1
                # print(i,count)
                rs.append(count)
            else:
                count = 1
        if len(rs) == 0 and any(nums): # nums = [1,0,1] 没考虑
            return 1
        elif len(rs) == 0:
            return 0
        else:
            return max(rs)


    def findMaxConsecutiveOnes2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
        ans.append(count)
        return max(ans)


    def findMaxConsecutiveOnes(self, nums):
        str_nums = ''.join(map(str,nums))
        print(str_nums)
        n = str_nums.split('0')
        print(n) # ['1', '11', '1']
        # return len(max(n))
        return max(map(len,n))



if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0, 1]
    # [1,0]
    # [1]
    print(Solution().findMaxConsecutiveOnes(nums))