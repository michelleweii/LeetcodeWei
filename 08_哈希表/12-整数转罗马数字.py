"""
middle
哈希表
"""
class Solution(object):
    def intToRoman(self, num):
        res = ""
        # map需要按顺序从小到大排
        hash_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                    50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        idx = 12
        while num:
            if num >= nums[idx]:
                res += hash_map[nums[idx]]
                num -= nums[idx]
            else:
                idx -= 1
        return res

if __name__ == '__main__':
    num = 3
    print(Solution().intToRoman(num))
