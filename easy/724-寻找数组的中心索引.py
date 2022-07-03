class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        count_left = 0
        count_right = 0
        for i in range(1,len(nums)):
            count_right += nums[i]
        # print(count_right)
        # print(count_left)
        i = 0
        while i<len(nums):
           if count_left == count_right:
               return i
           else:
                i += 1
                count_left += nums[i-1]
                if i!=len(nums):
                    count_right -= nums[i]
        return -1


def main():
    nums = [1, 7, 3, 6, 5, 6]
    myResult = Solution()
    print(myResult.pivotIndex(nums))

if __name__ == '__main__':
    main()
