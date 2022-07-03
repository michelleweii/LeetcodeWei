"""
hard 2022-03-03 二分
要求算法的时间复杂度应该为 O(log(m+n))
如果是先归并排序，再返回中位数，时间复杂度 O(m+n)
中位数：求第k小的数。求第k=1小数，那么index=0。
【解法三】https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/ 图例的模拟走一遍
"""
# 时间复杂度：每进行一次循环，我们就减少 k/2 个元素，所以时间复杂度是 O(log(k)，而 k=(m+n)/2，所以最终的复杂也就是O(log(m+n))。
"""
【关于left和right的解释】
int left = (len1 + len2 + 1) / 2;   // 总数为奇数的情况: 则取中间那个数  +  总数为偶数的情况: 则取中间偏前那个数
int right = (len1 + len2 + 2) / 2;  // 总数为奇数的情况: 也是取中间那个数  +  总数为偶数的情况: 则取中间偏后那个数
// 求两次，从而将奇偶问题解决。
//      如果是偶数: 则需要寻找中间前后两位 (此时left=right-1);
//      如果是奇数: 则只需寻找中间那一位   (此时left=right)
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        lens1,lens2=len(nums1),len(nums2)
        # 因为数组是从索引0开始的，因此我们在这里必须+1，即索引(index=k+1)的数，才是第k个数。
        # 将偶数和奇数的情况合并，如果是奇数，会求两次同样的 k
        left = (lens1+lens2+1)//2 # left_k
        right = (lens1+lens2+2)//2 # right_k
        # 应对m+n奇偶数两种情况的通用做法。如果m+n为偶数 那么取值为中间两值，如果为奇数则第left right为同一个数
        return (self.get_kthmin(nums1,0,lens1-1,nums2,0,lens2-1,left) \
                + self.get_kthmin(nums1,0,lens1-1,nums2,0,lens2-1,right)) \
               *0.5
        # 【第一次这里不理解，为什么求left，求right】
        # // 二分查找
        # // 一半儿一半儿的排除。假设我们要找的中位数为 合并数组后的 第k位数，我们可以每次循环排除掉 k/2 个数
        #
        # // 关键点
        # // (1)合并后数组的元素个数有奇偶两种情况：
        # //      偶数，需要找两次。结果为第len/2或(len+1)/2 和 第(len+2)/2或(len+3)/2 两个数的平均值，
        # //      奇数，需要找一次。结果为第(len+1)/2或(len+2)/2的那个数
        # //    综合起来,只需要两次 即第 (len+1)/2 和 (len+2)/2 的那两个数，再取平均值，即可兼顾奇偶两种情况
        # //
        # // (2)两种可能的情况： 即递归中两中返回值情况 (len1==0 或 k==1)
        # // (3)确定nums1比nums2范围更小，从而确定了其中一种返回条件(len==0)
        # // (4)当数组范围大小 len<k/2 时，参与比较的元素下标就不能是k/2-1，而是len-1
        # //
        # // 之后就是根据比较大小的结果 更新区间和k值

    # k是所求中位数的一半，还是看图
    # 求第k小的数
    def get_kthmin(self, nums1, start1, end1, nums2, start2, end2,k):
        # 1. 特殊处理
        len1 = end1-start1+1
        len2 = end2-start2+1
        # 让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1
        # 就是如果len1长度小于len2，把getKth()中参数互换位置，即原来的len2就变成了len1，即len1，永远比len2小
        if len1>len2:return self.get_kthmin(nums2,start2,end2,nums1,start1,end1,k)
        # 如果一个数组中没有了元素，那么即从剩余数组nums2的其实start2开始加k再-1

        # 【特别说明】len==0与k==1先后顺序不能换，否则会下标越界。因为len==0的时候，无法取到nums[s1]
        # 因为k代表个数，而不是索引，那么从nums2后再找k个数，那个就是start2 + k-1索引处就行了。因为还包含nums2[start2]也是一个数。因为它在上次迭代时并没有被排除
        # 情况一：
        if len1==0:return nums2[start2+k-1]
        # 如果k=1，表明最接近中位数了，即两个数组中start索引处，谁的值小，中位数就是谁(start索引之前表示经过迭代已经被排出的不合格的元素，即数组没被抛弃的逻辑上的范围是nums[start]--->nums[end])
        # 情况二：求第一小的数
        if k==1: return min(nums1[start1], nums2[start2])
        ################################################################################################################
        # 完成特殊处理
        ################################################################################################################


        # 2.求k//2元素的下标
        # 为了防止数组长度<k//2,每次比较都会从当前数组所生长度和k/2作比较，取其中的小的(如果取大的，数组就会越界)
        # 然后数字如果len1<k//2，表示数组经过下一次遍历就会到末尾，然后后面就会在那个剩余len2数组中寻找中位数
        # 二分
        i = start1+min(k//2,len1)-1 # 第k=3小的数字，index=2，所以要减一
        j = start2+min(k//2,len2)-1 # nums2中第j位是比较位置

        # 3.删除元素
        # nums2中index<=j的元素都不要了
        if nums1[i]>nums2[j]:
            return self.get_kthmin(nums1,start1,end1,nums2,j+1,end2,k-(j-start2+1))
        else:
            return self.get_kthmin(nums1,i+1,end1,nums2,start2,end2,k-(i-start1+1))


if __name__ == '__main__':
    nums1 = [1, 3] # 2
    nums2 = [2] # 1
    print(Solution().findMedianSortedArrays(nums1,nums2))

    # 14:33-15:08 1h