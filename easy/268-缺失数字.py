class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        # 0,1,2
        for value in nums:
            if i-value != 0:
                return i
            else:
                i += 1
        return i


def main():
    nums = [0]
    myResult = Solution()
    print(myResult.missingNumber(nums))

if __name__ == '__main__':
    main()