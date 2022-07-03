"""
middle 位运算
2021-07-19
"""
class Solution:
    def singleNumbers(self, nums):
        n = 0
        for num in nums:         # 1. 遍历异或
            n ^= num
        # print(n) # 7
        # 获取x^y的首位1出现的位置
        # x 和 y 的此m二进制位一定不同
        m = 1 # 现在不同的位置是右边第一位
        while n&m ==0:           # 2. 循环左移，计算 m
            m <<= 1
        x,y=0,0
        for num in nums:          # 3. 遍历 nums 分组
            if num & m: x ^= num  # 4. 当 num & m != 0
            else: y ^= num        # 4. 当 num & m == 0
        return [x,y]


if __name__ == '__main__':
    nums = [4, 1, 4, 6]
    print(Solution().singleNumbers(nums))

# m = 3
# m <<= 1
# print("after", m) # 6
