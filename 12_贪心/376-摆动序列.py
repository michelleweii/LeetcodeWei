"""
middle 2021-12-22 贪心
https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html
思路：
局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。
整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。
统计数组的峰值数量——>最长摆动子序列的长度
考虑特殊情况，数组最左面和最右面是最不好统计的，[2,5]是res=2
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        if (len(nums)<=1): return len(nums)

        # cur_diff = 0 # 当前一对差值
        pre_diff = 0 # 前一对差值
        result =  1 # 记录峰值个数，默认1

        for i in range(len(nums)-1):
            cur_diff = nums[i+1]-nums[i] # 当前元素的差值
            # 出现峰值
            if (cur_diff>0 and pre_diff<=0) or (pre_diff>=0 and cur_diff<0):
                result += 1 # 统计数组的峰值数量
                pre_diff = cur_diff  # 如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return result


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    print(Solution().wiggleMaxLength(nums))