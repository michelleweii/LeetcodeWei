"""
easy 2021-12-25 (有限变量 + 遍历)/堆排序
https://leetcode-cn.com/problems/third-maximum-number/solution/gong-shui-san-xie-yi-ti-shuang-jie-pai-x-pmln/
经典的找数组次大值的做法是使用两个变量 a 和 b 分别存储遍历过程中的最大值和次大值。
# 要求算法时间复杂度必须是O(n)。
"""
class Solution(object):
    # 有限变量 + 遍历，时间复杂度O(n)
    # 经典的找数组次大值的做法是使用两个变量 a 和 b 分别存储遍历过程中的最大值和次大值。
    def thirdMax(self, nums):
        a,b,c = float('-inf'),float('-inf'),float('-inf') # 最大，次大，第三大
        for x in nums:
            if x>a:
                c = b
                b = a
                a = x
            elif (x<a and x>b):
                c = b
                b = x
            elif (x<b and x>c):
                c = x
        return c if c!=float('-inf') else a

    # 堆排序，时间复杂度nlogn
    # 一直维护pq里只有3个元素
    def thirdMax_heap(self, nums):
        import heapq # 小顶堆
        nums = set(nums) # 使用 Set 去重的复杂度为 O(n)
        if len(nums)<3: return max(nums)
        q = []
        for x in nums:
            heapq.heappush(q,x)
            if len(q)>3: # 一直维护pq里只有3个元素
                heapq.heappop(q) # 返回堆中最小的元素
        return q[0]

def main():
    nums = [2,2,2,1,3,4,6,7]
    myResult = Solution()
    print(myResult.thirdMax(nums))

if __name__ == '__main__':
    main()

