"""
easy 2021-05-18 单调递减栈
通过Stack、HashMap解决
先遍历大数组nums2，首先将第一个元素入栈；
继续遍历，当当前元素小于栈顶元素时，继续将它入栈；当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key-value键值对，存入HashMap中；
当遍历完nums2后，得到nums2中元素所对应的下一个更大元素的hash表；
遍历nums1的元素在hashMap中去查找‘下一个更大元素’，当找不到时则为-1。
"""
# 2021-12-16
# 寻找比当前cur大的元素-->单调递减栈
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stk, hashmap = [], {}
        # 维护单调递减栈，栈内存的是index
        for i in range(len(nums2)):
            #  如果item比栈顶元素大，则栈顶元素一定是没有用的【单调栈模板】
            while stk and nums2[i]>nums2[stk[-1]]:
                # 操作
                index_t = stk.pop() # # 比item大的元素就是栈顶元素
                hashmap[nums2[index_t]] = nums2[i]
            stk.append(i)

        # 再遍历一次nums1
        res = [hashmap.get(x, -1) for x in nums1]
        return res

if __name__ == "__main__":
    nums1 = [2, 1, 3]
    nums2 = [2, 3, 1]
    myresult = Solution()
    print(myresult.nextGreaterElement(nums1, nums2))