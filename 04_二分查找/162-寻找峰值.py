"""
middle 2022-03-02 二分
本题核心：只要数组中存在一个元素比相邻元素大，那么沿着它一定可以找到一个峰值
https://leetcode-cn.com/problems/find-peak-element/solution/hua-jie-suan-fa-162-xun-zhao-feng-zhi-by-guanpengc/
# 整理一下由「证明 1」得出的推理：如果当前位置大于其左边界或者右边界，那么在当前位置的右边或左边必然存在峰值。
# 换句话说，对于一个满足 nums[x]>nums[x−1] 的位置，x的右边一定存在峰值；或对于一个满足nums[x]>nums[x+1] 的位置，x 的左边一定存在峰值。
# 因此这里的「二段性」其实是指：在以 mid 为分割点的数组上，根据 nums[mid]与nums[mid±1] 的大小关系,
可以确定其中一段满足「必然有解」，另外一段不满足「必然有解」（可能有解，可能无解）。
#
# 如果不理解为什么「证明 2」的正确性可以由「证明 1」推导而出的话，可以重点看看「证明 1」的第 2 点的证明。
# 至此，我们证明了始终选择大于边界一端进行二分，可以确保选择的区间一定存在峰值，并随着二分过程不断逼近峰值位置。
# 链接：https://leetcode-cn.com/problems/find-peak-element/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-qva7v/
"""
"""
特点：
# 无两段性的性质，但可以用二分来做
# 二分95%应用于有两段性性质的区间，本题属于剩下的5%
思路：
由于假设左右端点的值为负无穷，所以每次在区间中找出一点，
其到右端点要么单调递减，要么存在峰值
左端点到该点要么单调递增，要么存在峰值
步骤：
我们每次找出区间中间的点，判断它与它右边的数的大小关系（也可比较与左边的数）
若nums[mid] < nums[mid+1]说明存在单调递增，则可以判断Mid右边的区间必存在峰值，
因为只有右边是单调递减才会不存在峰值
每次筛选出的是一定存在峰值的区间，不代表另一半就没有峰值哦
若nums[mid] >= nums[mid+1]，不代表右边一定没峰值，只是代表左边一定有峰值
所以为了节省时间快速找到任意一个峰值，我们把右指针 r = mid

链接：https://www.acwing.com/solution/content/7955/
"""
class Solution:
    def findPeakElement(self, nums) -> int:
        l = 0; r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            # 严格大于左右相邻值的元素
            #  if nums[mid]<=nums[mid+1]: # 也可以AC
            if nums[mid] < nums[mid+1]: # 若当前点比右边小，则峰值在右边
                l = mid + 1
            else:
                r = mid
        return r

if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    # nums = [1, 2]
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(Solution().findPeakElement(nums))
