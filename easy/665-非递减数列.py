class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = 0
        i = 0
        while i<len(nums)-1:
            if nums[i] <= nums[i+1]:
                i+=1
            else:
                if not flag:
                    tmp=nums[i]
                    del nums[i]
                    if not self.isDescending(nums):
                        nums.insert(i,tmp)
                        # print(nums)
                        del nums[i+1]
                        if self.isDescending(nums):
                            return True
                    i = 0
                    flag = 1
                    # print(nums)
                else:
                    return False
        return True

    # 类里怎么调用函数呢？忘记了。。。。。
    def isDescending(self,num):
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                return 0
        return 1




def main():
    # nums = [4, 2, 3]  # del nums[i]
    nums = [2, 3, 3, 2, 4] # del nums[i+1]
    myResult = Solution()
    print(myResult.checkPossibility(nums))

if __name__ == '__main__':
    main()