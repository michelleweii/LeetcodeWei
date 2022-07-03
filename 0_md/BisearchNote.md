[其他「二分」相关题解](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/)

[为什么去除首尾相同元素就可以恢复二分的两端性](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/)

<u>之前不明白为什么154相对于153的解决方案是“去除首尾元素”</u>

**<u>因为「二分」的本质是二段性，并非单调性。只要一段满足某个性质，另外一段不满足某个性质，就可以用「二分」。</u>**

LC153旋转数组最小值--> LC154(153升级版，有重复元素)--> LC33搜索旋转排序数组 (先找到最小值，确定target属于哪个递增区间，再次二分) --> LC81搜索旋转排序数组|| (LC33升级版，有重复元素【核心：恢复二段性】)



[LC162. 关于能够「二分」的两点证明](https://leetcode-cn.com/problems/find-peak-element/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-qva7v/)

最早在 LC33搜索旋转排序数组 中，我们强调，二分的本质是「二段性」而非「单调性」，
而经过本题LC162，我们进一步发现「二段性」还能继续细分，不仅仅只有满足 01 特性（满足/不满足）的「二段性」可以使用二分，
满足 1? 特性（一定满足/不一定满足）也可以二分。



- [ ] LC287.寻找重复数