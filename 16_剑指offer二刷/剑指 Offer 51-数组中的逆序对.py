"""
hard 归并排序进阶
2021-07-21
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-zhi-offer-51-shu-zu-zhong-de-ni-xu-pvn2h/
"""
# https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-zhi-offerdi-51ti-ti-jie-gui-bing-pa-7m88/
class Solution:
    def reversePairs(self, nums):
        self.res = 0
        return self.merge(nums, 0, len(nums)-1)

    def merge(self, nums, l, r):
        if l>=r:return 0
        mid = (l+r)//2

        res = self.merge(nums, l, mid) + self.merge(nums, mid+1, r)
        # a = self.merge(nums, l, mid)
        # b = self.merge(nums, mid+1, r)
        # print("a+b", a, b)
        i, j = l, mid+1
        temp = []
        while i<=mid and j<=r:
            if nums[i] <= nums[j]: # 如果左边<=右边，不构成逆序对
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
                res += mid-i+1
        temp += nums[i:mid + 1]
        temp += nums[j:r + 1]

        # 把临时数组的元素再放回去，实现原地更改
        for k in range(r-l+1):
            nums[l+k] = temp[k]
        # k = l
        # for x in temp:
        #     nums[k] = x
        #     k+=1
        print("temp", temp)
        return res


    # def reversePairs(self, nums):
    #     self.tmp = [0] * len(nums)
    #     return self.merge_sort(nums, 0, len(nums)-1)
    #
    # def merge_sort(self, nums, l, r):
    #     # 终止条件
    #     if l >= r: return 0
    #     # 递归划分
    #     m = (l + r) // 2
    #     res = self.merge_sort(nums, l, m) + self.merge_sort(nums, m + 1, r)
    #     # 合并阶段
    #     i, j = l, m + 1
    #     self.tmp[l:r + 1] = nums[l:r + 1]
    #     for k in range(l, r + 1):
    #         if i == m + 1:
    #             nums[k] = self.tmp[j]
    #             j += 1
    #         elif j == r + 1 or self.tmp[i] <= self.tmp[j]:
    #             nums[k] = self.tmp[i]
    #             i += 1
    #         else:
    #             nums[k] = self.tmp[j]
    #             j += 1
    #             res += m - i + 1  # 统计逆序对
    #     return res

if __name__ == '__main__':
    nums = [7,5,6,4]
    print(Solution().reversePairs(nums))