"""
easy 2021-05-18 单调队列
通过Stack、HashMap解决
先遍历大数组nums2，首先将第一个元素入栈；
继续遍历，当当前元素小于栈顶元素时，继续将它入栈；当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key-value键值对，存入HashMap中；
当遍历完nums2后，得到nums2中元素所对应的下一个更大元素的hash表；
遍历nums1的元素在hashMap中去查找‘下一个更大元素’，当找不到时则为-1。
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stk = [] # 维护单调递增栈,栈存的是下标
        hash = {}
        for num in nums2:
            # 如果item比栈顶元素大，则栈顶元素一定是没有用的
            # k:栈顶元素，v：item
            while stk and num > stk[-1]:
                # 比item大的元素就是栈顶元素
                t = stk.pop()
                hash[t] = num
            stk.append(num)

        # print(hash)
        res = [hash.get(x,-1) for x in nums1]
        return res

if __name__ == "__main__":
    nums1 = [2, 1, 3]
    nums2 = [2, 3, 1]
    myresult = Solution()
    print(myresult.nextGreaterElement(nums1, nums2))
