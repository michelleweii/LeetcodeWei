双指针

[为什么双指针不会错过正确答案？双指针的本质。！](https://leetcode-cn.com/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/)

双指针找最长子串，最短子串，最小覆盖，必然要搭配hashmap。其中，k为char字符，v为该字符出现几次。

基础题

LC3.无重复字符的最长子串

```python
"""
思路;
定义两个指针i,j。表示当前扫描到的子串是[i,j]，
扫描过程中维护一个哈希表，表示[i,j]中每个字符出现的次数。
1、指针j向后移动一位，同时将哈希表s[j]的计数+1，hash[s[j]]++；
2、假设j移动前的区间[i,j]中没有重复字符，则 j 移动后，只有s[j]可能出现2次。<重点>
因此我们不断向后移动i，直至区间[i,j]中s[j]的个数等于1为止；
"""
# 以s[j]为右端点，向左延生，最远能延生到的i的位置
def _lengthOfLongestSubstring(self, s):
    hash_map = {}
    i = 0
    res = 0
    for j in range(len(s)):
        hash_map[s[j]] = hash_map.get(s[j],0)+1
        while hash_map[s[j]]>1:
            hash_map[s[i]] = hash_map[s[i]]-1
            i += 1 # i是最左的有边界
        res = max(res,j-i+1)
    return res
```

思路总结

> [滑动窗口：当窗口大小与 t 长度相等时，可能得到一个可行解](https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-hua-dong-chuang-k-sos8/)
>
> 基本都是[left, right]指针维护一个区间，第一个while right<len(nums)，right右区间一直++，
>
> 当不满足or满足题意是，第二个while进行left++，尝试缩小窗口，
>
> 在缩小窗口的同时，更新 res = max/min(res, right-left+1)，更新res的位置依据题意。（收缩窗口的时候更新结果）

相关题目：

- LC3.无重复字符的最长子串

- LC209.长度最小的子数组

- LC76.最小覆盖子串

- LC438.找到字符串中所有字母的异位词

- LC567.字符串的排列

**LC76+LC567总结**
在寻找最优解的时候，如果没有破坏窗口性质，left直接++；
如果破坏窗口性质则要做破坏处理：
1）计数器++ or --;
2）curmap中的元素个数++ or --;



LC11.盛最多水的容器 vs LC.42 接雨水

- LC11.盛最多水的容器：反向双指针（求最大的就行了）
- LC.42 接雨水：单调递减栈（每个空档都可以盛水），也可以使用双指针，只不过麻烦一点。

两者的区别是？

- 反向双指针使用场景：？？？一类思路

- **单调栈使用场景：对于找最近一个比当前值大/小的问题。**





百做百不会

-_-||

LC26. 删除有序数组中的重复项

```python
"""
easy 2021-09-07 同向双指针<--因为要保证顺序不变。
要求：不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
因为数组是有序的，那么重复的元素一定会相邻。
"""
# 如果两个元素相等，j++
# 不相等，i++, nums[i]=nums[j]
class Solution:
    def removeDuplicates(self, nums):
        # i 左边是已经处理好的元素；
        # 元素如果要话，ij都要右移；
        # 元素如果不要的话，j右移，i不动；
        # 当ij不在同一个位置上时，j标记的位置如果要的话，则将j的值赋给i。i++
        # 【i 左边是处理好的元素】。
        i, j = 0, 1
        # i=0说明i左边什么都没有，第一个元素肯定是不重复的
        while j < len(nums):
            # 如果相等，j++
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j] # 是赋值操作，不是交换操作！
            # print(i, j, nums)
            # 0 2 [1, 1, 2]
            # 1 2 [1, 2, 2]
            # 1 3 [1, 2, 2]
        return i+1 # 2
```

LC27. 移出元素

```python
# 如果等于目标值就跳过，不等于目标值则插入。
# 删除nums中=val的值
class Solution(object):
    def two_points(self, nums, val):
        """双指针法
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(nums)
        if not n: return 0
        slow, fast = 0, 0
        while fast<n:
            # 不相等则开始交换
            # 交换完成，slow++, fast++
            if val != nums[fast]:
                nums[slow] = nums[fast]
                slow+=1
            # 如果快指针=val，快指针++
            fast+=1
        return slow
```



重要题目

LC56. 合并区间

```python
"""
middle 2021-10-18 （字节、腾讯、百度）
双指针思路：根据第一个元素升序，前后看谁大谁小, intervals[l]and intervals[r]
题目：合并所有重叠的区间
"""
class Solution:
    def merge(self, intervals):
        if not intervals:return intervals
        intervals.sort() # 默认先按第一个元素升序，再按第二个元素升序
        # print(intervals) # [[1, 3], [2, 6], [8, 10], [15, 18]]
        l, r = 0, 1
        while r<len(intervals):
            x1,y1 = intervals[l]
            x2,y2 = intervals[r]
            if x2>y1:
                l,r = l+1,r+1
            else:
                intervals[l] = [x1, max(y1,y2)]
                intervals.pop(r)
        return intervals

if __name__ == '__main__':
    intervals = [[1, 3],  [8, 10], [2, 6], [15, 18]]
    # [[1, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))
```

LC26.删除有序数组中的重复项 & 80.删除有序数组中的重复项II

LC27.移出元素 & 283.移动零 ：不等于0就交换，且slow++,fast++；等于0就fast++；





https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/gong-shui-san-xie-shuang-zhi-zhen-shi-xi-t5hc/





# 套路题

76、438、567



