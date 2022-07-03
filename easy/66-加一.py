# 看题以为只是简单的末尾加一，没有考虑到进位问题，进位+1，有可能还进位啊！
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = []
        res = []
        for i in range(len(digits)):
            i = str(digits[i])
            nums.append(i)
        num = "".join(nums)
        # print(int(num))
        num = int(num)
        # print(type(num))
        tmp = num+1
        tmp = str(tmp)
        # print(type(tmp[0]))
        for i in tmp:
            i = int(i)
            res.append(i)
        # print(type(res[0]))
        return res


# @ 1
# class Solution:
#     def plusOne(self, digits):
#         last = 1
#         res = []
#         for i in range(len(digits)):
#             tmp = digits.pop() + last
#             last = int(tmp/10)
#             res.insert(0, tmp%10)
#         if last != 0:
#             res.insert(0, last)
#         return res

# @ 2
    # if len(digits) == 0:
    #     digits = [1]
    # elif digits[-1] == 9:
    #     digits = self.plusOne(digits[:-1])
    #     digits.extend([0])
    # else:
    #     digits[-1] += 1
    # return digits



def main():
    digits = [4,3,2,1]
    myResult = Solution()
    print(myResult.plusOne(digits))

if __name__ == '__main__':
    main()