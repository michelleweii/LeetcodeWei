"""
easy
2021-07-19
"""
# A为1, K为13
class Solution:
    def isStraight(self, nums):
        if not nums:return False
        min_value, max_value = 14, -1
        repeat = set() # 除大小王外，所有牌 无重复, 有重复的当然是对子，不能构成顺子了
        for x in nums:
            if x==0:continue
            max_value = max(max_value, x)
            min_value = min(min_value, x)
            if x in repeat: return False  # 若有重复，提前返回 false
            repeat.add(x)  # 添加牌至 Set
        return max_value-min_value<5

if __name__ == '__main__':
    nums = [0, 0, 1, 2, 5]
    print(Solution().isStraight(nums))