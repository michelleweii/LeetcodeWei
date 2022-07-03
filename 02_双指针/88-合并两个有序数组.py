"""
easy 2021-09-07 同向双指针（逆序归并）
https://leetcode-cn.com/problems/merge-sorted-array/solution/hua-jie-suan-fa-88-he-bing-liang-ge-you-xu-shu-zu-/
难死了 easy个锤子
思路：
- 标签：从后向前数组遍历
- 因为 nums1 的空间都集中在后面，所以从后向前处理排序的数据会更好，节省空间，一边遍历一边将值填充进去
- 设置指针 len1 和 len2 分别指向 nums1 和 nums2 的有数字尾部，从尾部值开始比较遍历，同时设置指针 len 指向 nums1 的最末尾，每次遍历比较值大小之后，则进行填充
- 当 len1<0 时遍历结束，此时 nums2 中还有数据未拷贝完全，将其直接拷贝到 nums1 的前面，最后得到结果数组
- 时间复杂度：O(m+n)
"""

"""
easy 2022-03-02 三指针（从后向前数组遍历）
因为 nums1 的空间都集中在后面，所以从后向前处理排序的数据会更好，节省空间，一边遍历一边将值填充进去
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        lens1=m-1
        lens2=n-1
        len=m+n-1
        while lens1>=0 and lens2>=0:
            if nums1[lens1]>=nums2[lens2]:
                nums1[len]=nums1[lens1]
                lens1-=1
            else:
                nums1[len]=nums2[lens2]
                lens2-=1
            len -= 1
        # while lens1>=0:
        #     nums1[len]=nums1[lens1]
        #     len-=1
        #     lens1-=1
        while lens2>=0:
            nums1[len]=nums2[lens2]
            len-=1
            lens2-=1
        return nums1

# 2022-01-04 逆序的归并，这次理解了很多
class Solution:
    def merge(self, nums1, m, nums2, n):
        p, q = m-1, n-1
        last = m+n-1
        while p>=0 and q>=0:
            if nums1[p] > nums2[q]:
                nums1[last] = nums1[p]
                p -= 1
                last -= 1
            else:
                nums1[last] = nums2[q]
                q -= 1
                last -= 1

        # 如果p的元素一直比q大的话，nums1先结束。nums2还没有遍历完成。
        # 直接将nums2的元素放在nums1之前
        res = nums2[:q+1]+nums1 # 这里不是特别理解
        return res[:m+n]


if __name__ == '__main__':
    nums1 = [0] #[1,2,3,0,0,0]
    m = 0#3
    nums2 = [1]#[2,5,6]
    n = 1#3
    print(Solution().merge(nums1, m, nums2, n))
