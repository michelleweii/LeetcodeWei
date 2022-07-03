"""
middle
哈希表
"""
class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        # count = 1
        for i in nums:
            if i not in dict.keys():
                dict[i]=1
            else:
                count = dict[i]
                count += 1
                dict[i] = count

        for key, value in dict.items():
            # print("key:value=={}:{}".format(key,value))
            # print(value)
            if value!=3:
                # !=要比==1遍历速度快
                return key

if __name__ == '__main__':
    nums = [0,1,0,1,0,1,99]
    myResult = Solution()
    print(myResult.singleNumber(nums))

