class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        after_nums = set(nums)
        if len(after_nums)==len(nums):
            return False
        else:
            return True


def main():
    listA = [1,2,3,4]
    myResult = Solution()
    print(myResult.containsDuplicate(listA))

if __name__ == '__main__':
    main()