常用网站：

1. [企业题库](https://codetop.cc/home)
2. [代码随想录](https://programmercarl.com/)
2. [刷题模板](https://fuxuemingzhu.blog.csdn.net/article/details/101900729)
2. [十大排序算法](https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/)
2. [必刷题](http://www.chengxuchu.com/#/%E7%AE%97%E6%B3%95%E5%9F%BA%E5%9C%B0/README?id=%e7%ae%97%e6%b3%95%e5%9f%ba%e5%9c%b0)

题目关键字：

【dp关键字】能不能组成True or False、有多少种

【dfs关键字】打印所有结果（回溯）

【】前缀和~=hashmap



# 前置理论  

## 回文串



判断是否是有效的括号

右括号一定是比左括号多的，`if left>right:return`

```
# 前置知识：统计左括号、右括号数量是否平衡;
# 在任意一个时刻，右括号数量一定是<=左括号数量的,如果>说明左边至少一个右括号无法匹配
# count')'<=count'(', i<n-1
# count')'==count'(', i=n-1
def is_valid(self, s):
    count = 0
    for ch in s:
        if ch =='(': count+=1  # 相当于左括号先入栈
        elif ch ==')': count-=1 # 遇到右括号，左括号弹栈
        if count<0:return False
    return count==0
```

# 1. 排序算法

- 归并排序：时间复杂度O(nlogn)，从上到下(我学习的那种)，空间复杂度O(n); 从下到上，空间复杂度O(1)，应用题目LC148。
- 快排：从后面先开始找比pivot小的数，否则错误。
- 桶排序：桶排序 每个桶内部无序，但是桶与桶之间是有序的。

> 经典的找数组次大值的做法是使用两个变量 a 和 b 分别存储遍历过程中的最大值和次大值。

# 2. 二叉树

[图解bitree的遍历过程，加深理解](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/)

[bitree题目集合](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/solution/yi-tao-quan-fa-shua-diao-nge-bian-li-shu-de-wen-5/)

[树的遍历（递归+迭代）](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/die-dai-fa-by-jason-2/)

最大深度：从根节点到叶节点最长的那条路径，上的节点数。最大路径：任意两个节点最长的那条路径，上的边数。

## 2.1. 层次遍历
- 102.二叉树的层序遍历（已完成）
- 103.[二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal)  （已完成）
- 二叉树的右视图
- 二叉树的层平均值
- N叉树的前序遍历
- 在每个树行中找最大值
- 填充每个节点的下一个右侧节点指针
- 117.[填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii) （已完成，链表+层次遍历）
- 208 前缀树(字典树概念) 重做！！！

lc113: 找到所有路径，所以递归函数不要返回值！

> 最大深度：从根节点到叶节点最长的那条路径上的节点数。
> 最大路径：任意两个节点最长的那条路径上的边数。
>
> 二叉搜索树（BST）：对于树中每个节点,
> 若其左子树存在，则其左子树中每个节点的值都不大于该节点值；
> 若其右子树存在，则其右子树中每个节点的值都不小于该节点值。
>
> 性质：BST的中序遍历是升序的。

在二叉树中如何从低向上推导呢？使用后序遍历也就是左右中的顺序，这样就可以在回溯的过程中从下到上进行推导了。

# 3. 二分法
- 153.旋转数组最小值0513
- 162.寻找峰值0513
- 287.寻找重复解

二分刷题路线

[其他「二分」相关题解](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/)

[为什么去除首尾相同元素就可以恢复二分的两端性](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/)

<u>之前不明白为什么154相对于153的解决方案是“去除首尾元素”</u>

**<u>因为「二分」的本质是二段性，并非单调性。只要一段满足某个性质，另外一段不满足某个性质，就可以用「二分」。</u>**

LC153旋转数组最小值--> LC154(153升级版，有重复元素)--> LC33搜索旋转排序数组 (先找到最小值，确定target属于哪个递增区间，再次二分) --> LC81搜索旋转排序数组|| (LC33升级版，有重复元素【核心：恢复二段性】)

# 4. 字符串相关
- 686 KMP算法-middle

- 49 hash表 value是list[]

- 151 error

- 6 **zip()的使用以及边界**

- 无重复字符的最长子串

    > - **子串一定的是连续的；**
    > - **子序列不一定是连续的一段，但是下标要求是递增的；**
    > - **子数组（子数组最少包含一个元素）**

# 5. 双指针
**滑动窗口算法一定是双指针算法；双指针算法不一定是滑动窗口算法；**

## **5.1. 单向（滑动窗口）**

[https://www.bilibili.com/video/BV1P7411L7eV?from=search&seid=16847300039480678482](同向双指针（一）)
[https://www.bilibili.com/video/BV1P7411L7NK](同向双指针（二）)
[https://www.bilibili.com/video/BV1M741147Ta](双指针基础（一）)
[https://www.bilibili.com/video/BV1A7411L7EQ?from=search&seid=16847300039480678482](双指针基础（二）)

76：cnt元素维度，初始化是目标，每当window中包含一个，cnt--；

438：window中字符个数与目标保持一致，字符维度，flag++；

s长串、t短串，**两个while循环解决**。

```python
# 一般框架
"""
遍历s，求最小问题
    1、移动right，寻找可行解，满足t_tmp
        2、移动left，寻找最优解
"""
while right<len(s):
    # 当满足条件了，一般是hash表字符个数满足了
    if 满足条件:
    	while(根据题意，不用寻找最优解，就不用第二个while了)：
        left++ # 寻找最优解
    right++ # 寻找可行解
```



## **5.2. 双向**

- 75 荷兰国旗问题 （快排扩展）
https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
题解这里，关于窗口的开闭是很重要的。

- 80 

### 需要重做
- easy 7
- middle 260 hash
- middle 29 位运算
- middle 43 没做
- middle 71 堆栈
- hard 30 0530没做

# 6. dp

416. 分割等和子集——动态规划之01背包问题
494. 目标和——动态规划之01背包问题
322. 零钱兑换——动态规划之完全背包问题
518. 零钱兑换 II——动态规划之完全背包的组合问题
377. 组合总和 Ⅳ——动态规划之完全背包考虑顺序的组合问题


https://www.bilibili.com/video/BV1hf4y197w3
https://www.bilibili.com/video/BV1CD4y127CZ
https://www.bilibili.com/video/BV1sk4y1y7Dv
https://www.bilibili.com/video/BV12k4y127nP
https://www.bilibili.com/video/BV14z4y1f7hH


# 7. 链表
1. [myself【leetcode总结】解析链表系列](https://blog.csdn.net/weixin_31866177/article/details/84554245?spm=1001.2014.3001.5506)

2. [LC链表专题](https://leetcode-cn.com/tag/linked-list/problemset/)

LC148排序链表【如何寻找一个链表的中间点】与876的差别在哪？

快慢指针找到中点的时候，快指针最开始一定要设置为head.next，设置成head就会栈溢出。（方法2就是设置为head额？）

使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。中点 slow。
```python
## slow = fast = head
如果slow = fast = head,那么在链表只剩两个节点的时候有以下执行顺序：(首节点->尾节点->null)
0. 执行查找中点的while循环
1. 得出：slow = 尾节点，fast = null
2. mid = slow.next;
   slow.next = null; 
   //第2步为断链,需要注意的是,slow的next原本就是null(由第1步得出)
   //也就是说,断链操作根本没有生效,链表结构依然是:首节点->尾节点->null
3. 进入递归,由于链表结构没变,所以会继续进行查找中点、断链操作,重复以上步骤,导致栈溢出
4. mid中点是slow
-----------------------------------------------------------
## slow = head, fast = head.next
如果slow = head, fast = head.next,那么在链表只剩两个节点的时候有以下执行顺序：(首节点->尾节点->null)
0. 执行查找中点的while循环
1. 得出：slow = 首节点，fast = 尾节点
2. mid = slow.next;
   slow.next = null; 
   //这里的断链操作生效了,此时链表结构为：首节点->null,尾节点->null
3. 进入递归,重复以上步骤,此时的链表已经分解成两个节点,所以不会查找中点及断链,而是直接return。
4. mid中点是slow.next
```

```python
# 方法1
# LC109
slow, fast = head, head
pre = head
while fast and fast.next:
     pre = slow
     slow, fast = slow.next, fast.next.next
mid = slow
# 拆分左右链表
pre.next = None # 左子树断开

# 方法2
# LC148
# 找到中间点，并将链表分成两端，注意这里[链表寻找中间点]的方法。相关lc876
slow, fast = head, head.next
# 为什么fast=head.next 而不能是fast=head? 也可以
# 因为这样长度为2的那一支链表会一直递归下去，直到栈溢出。
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next # 中点 slow
mid = slow.next # 也可以mid=show, pre.next=None, 和109一样，标记pre
slow.next = None
```

找链表中点：109有序链表转为二叉搜索树、876链表的中间节点、148排序链表。

优雅地求一个链表的长度`while h: h, length = h.next, length + 1`



# 8. 单调栈

https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/dan-diao-zhan-jie-fa-by-lilin-k-7096/

> --栈底--------栈顶-----

- 单调递减栈：从栈底到栈顶数据是从大到小；**<u>序列从大到小，比栈顶元素小直接入栈，比栈顶元素大，则将比当前元素小的所有元素都干掉，一直出栈，直到满足性质后，当前元素入栈；</u>**

​		<u>**- 找（一边）两边比cur大**</u>【核心！】

​       - 单调递减栈操作：如果栈为空或入栈元素值小于栈顶元素值，则入栈；否则，如果入栈则会破坏栈的单调性，则需要把比入栈元素小的元素全部出栈。

- 单调递增栈：从栈底到栈顶数据是从小到大；<u>**序列从小到大，比栈顶元素大直接入栈，比栈顶元素小，则将比当前元素大的元素都干掉，一直出栈，直到满足性质后，当前元素入栈**</u>；

​		**<u> - 找（一边）两边比cur小</u>** 【核心！】

【小技巧】

好像同时找当前值左边and右边最小值的时候，要用哨兵。单独找左边or右边的时候不用哨兵？

- 应用场景：

> **对于找最近一个比当前值大/小的问题，都可以使用单调栈来解决**。
>
> 1.<u>需要找到两边（一边）比cur大（小）的值时可以用</u>，遇到时退栈并计算（更新），栈中一般存储下标（下标和值的pair，或值另外存在vector）
>
> 2.需要在无序数列中保证有序数列时，如去掉k位数使得数最小，此时栈中一般保存数而不是下标。
>
> 应用场景举例LC654. 在这个题中，我们要找到**元素右边第一个比它大的元素**作为**整个左侧区间的根结点**，因此我们可以维护一个【递减栈】，存放未找到右侧更大元素的元素。

```c++
// 单调递增
for(int i = 0; i < nums.size(); i++){ //for循环
    while(!st.empty() && nums[i] < st.top()){ //while循环
      // 一些操作
}
     st.push(nums[i]);
}
```

> 哨兵：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
>
> 需要考虑两种特殊的情况：1、弹栈的时候，栈为空；2、遍历完成以后，栈中还有元素；
> 为此可以我们可以在输入数组的两端加上两个高度为 0 （或者是 0.5，只要比 1 严格小都行）的柱形，可以回避上面这两种分类讨论。
>
> 这两个站在两边的柱形有一个很形象的名词，叫做哨兵（Sentinel）。
>
> 有了这两个柱形：
>
> - 左边的柱形（第 1 个柱形）由于它一定比输入数组里任何一个元素小，它肯定不会出栈，因此栈一定不会为空；
>- 右边的柱形（第 2 个柱形）也正是因为它一定比输入数组里任何一个元素小，它会让所有输入数组里的元素出栈（第 1 个哨兵元素除外）。

<u>逆序的单调栈</u>掌握不好：逆序的单调递减，指的是从后向前看数组的递减的。（就是正着看是递增啊）

```python
#       在构建单调栈的过程中计算的方法。stk.top()所在子数组最小值是它自己，
#       最右是马上要进栈的那个值的左边一格，最左是stk.top()出栈后的栈顶的右边一格。
```

- 42.接雨水（单调递减栈）# 先放入哨兵，在循环里就不用做非空判断 # <u>**找两边比cur大**</u>
- 84.柱状图中最大的矩形（单调递增栈，**双端添加哨兵**）# <u>**找两边比cur小**</u>
- 456.132模式（单调栈逆序）
- 496.下一个更大元素 I 
- 581.最短无序连续子数组2
- 739.每日温度
- 1856.子数组最小乘积的最大值

# 9. 图

一个无向图，需要用标记位，标记着节点是否走过，否则就会死循环！

## 9.1.1 dfs



## 9.1.2 回溯

回溯总结

- 子集问题、分割问题都是组合问题。可以不适用used数组来去重，因为递归的时候下一个startIndex是i+1而不是0。

- 如果要是全排列的话，每次要从0开始遍历，为了跳过已入栈的元素，需要使用used。

排列问题与组合问题的不同

- 每层都是从0开始搜索而不是startIndex
- 需要used数组记录path里都放了哪些元素了（而组合问题的used是用来标记相同元素是在树层还是树枝上的，树枝上used=1可以用，树层上used=0不可以用）

**组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点！**

组合是[1,2], [2,1] 都是同一个解集，但是排列问题中[1,2], [2,1] 是不同的解题。
如果是一个集合来求组合的话，就需要startIndex。
如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex。（排列问题不需要index）。
- 注意这里不要加return，因为要取树上的所有节点。（if出口的时候）

## 9.2. bfs

[岛屿类问题通解](https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/)

[Tree的BFS vs. 图的BFS](https://leetcode-cn.com/problems/01-matrix/solution/2chong-bfs-xiang-jie-dp-bi-xu-miao-dong-by-sweetie/)

- 对于「Tree 的 BFS」（典型的「单源 BFS」）大家都已经轻车熟路了：
	- 首先把 root 节点入队，再一层一层无脑遍历就行了。

- 对于「图 的 BFS」（「多源 BFS」）做法其实也是一样滴～，与「Tree 的 BFS」的区别注意以下两条就 ok ～

	- Tree 只有 1 个 root，而图可以有多个源点，所以首先需要把多个源点都入队；
	- Tree 是有向的因此不需要标识是否访问过，而对于无向图来说，必须得标志是否访问过哦！
	并且为了防止某个节点多次入队，需要在其入队之前就将其设置成已访问！

	- 总而言之，上面一句话的含义就是原地修改 or visited数据标记已访问！
	- 如果是原地修改矩阵，则在递归内部传参；
	- 如果是visited数组，则需要在递归外部就传；

## 9.3. 并查集

作用：检查图中是否存在环，主要实现两个方法：

1. def find_root(x) # 找到x节点的根；
2. def union(x,y) # 将x，y节点进行合并（将x，y结点连起来）；

在并查集里，每个节点会记录它的父节点。

> 详解：https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/

- 带权并查集

> https://leetcode-cn.com/problems/evaluate-division/solution/pythonbing-cha-ji-fu-mo-ban-by-milomusia-kfsu/
>
> 普通并查集只能判断两个元素是否在一个集合中，带权并查集可以维护集合元素之间的关系，这个关系由每个元素的权值维护。

四边形法则：https://www.cnblogs.com/enmac/p/13962764.html

四边形法则更新根节点的权重：`self.value[x_father] = self.value[y] * val / self.value[x]`





# 10. 堆/优先队列

堆是一种相当有意思的数据结构，它在很多语言里也被命名为「优先队列」。它是建立在数组上的「树」结构，类似的数据结构还有「并查集」「线段树」等。

python优先队列`from queue import PriorityQueue`

> PriorityQueue没有pop()的方法，就是get()元素之后，该元素还是在queue里，转用heapq。

优先队列不是O(logN)，因为remove()是个O(N)的操作，remove方法需要遍历所有元素。



# 11. 前缀和

概念：presum表示前缀和，index `i-j` 的前缀和为`nums[i ... j] = presum[j] - presum[i-1]`。

举例，`nums = [4, 2, 3, 1]`，那么`presum = [0, 4, 6, 9, 10]`。求`index=1`到`index=2`的前缀和，为` presum[3]-presum[1] = 9-4 = 5`。

**求前缀和的时候，index=0默认为0，从index=1开始计算。**

优雅计算前缀和，

```python
presum = [0]
for n in nums:
    presum.append(presum[-1] + n)
```

LC560. 和为k的子数组

```python
"""
2021-12-14 前缀和+哈希表
先对原数组求个前缀和
求前缀和技巧：sum表示前缀和，i-j前缀的和为nums[i...j]=sum[j]-sum[i-1]
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/dai-ni-da-tong-qian-zhui-he-cong-zui-ben-fang-fa-y/
思路：
这道题即“求前缀和=2的数量”
1、先求出nums的前缀和sums；
2、求满足`prefixSum[j] - prefixSum[i - 1] == k`的个数；
"""
class Solution:
    # 简单前缀和，时间复杂度O(N^2)
    # 有几种 i、j 的组合，满足 prefixSum[j] - prefixSum[i - 1] == k
    def subarrySum_native(self, nums, k):
        n = len(nums)
        # 计算前缀和数组
        pre_sum = [0]*(n+1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i]+nums[i]
        # print(pre_sum) # [0, 1, 2, 3]
        count = 0
        for left in range(0, n):
            for right in range(left, n):
                # 区间和 [left..right]，注意下标偏移
                # 求前缀和=2的数量
                if pre_sum[right+1]-pre_sum[left]==k: # 【Attention】
                    count += 1
        return count

    # 前缀和 + 哈希表优化，时间复杂度O(N)
    # key: 前缀和
    # value: key 对应的前缀和的个数
    def subarraySum(self, nums, k):
        hash_map = {}
        hash_map[0] = 1 # 前缀和为0的数量有1个。默认nums[-1]=0
        res = 0
        sums = 0 # 前缀和
        for x in nums:
            sums += x
            # print(sums) # 1,2,3
            # 问自己！当前前缀和（sums）-k，之前出现过吗？如果出现过了记作a，那么sums-a=k，count++
            # (a,b)=presum[b]-presum[a]=k
            # presum[b]=sums
            # 求a出现过几次
            res += hash_map.get(sums-k, 0) # hash_map[sums-k] KeyError: -1
            # 维护hashmap的定义
            hash_map[sums] = hash_map.get(sums, 0) + 1 # 计算前缀和为sums的个数

        # print(hash_map) # {0: 1, 1: 1, 2: 1, 3: 1}
        return res
    """
    不用求出 prefixSum 数组
    其实我们不关心具体是哪两项的前缀和之差等于k，只关心等于 k 的前缀和之差出现的次数c，就知道了有c个子数组求和等于k。
    遍历 nums 之前，我们让 -1 对应的前缀和为 0，这样通式在边界情况也成立。即在遍历之前，map 初始放入 {0:1} 键值对（前缀和为0出现1次了）。
    遍历 nums 数组，求每一项的前缀和，统计对应的出现次数，以键值对存入 map。`hash_map[sums] = hash_map.get(sums, 0) + 1 `
*    边存边查看 map，如果 map 中存在 key 为「当前前缀和 - k」，说明这个之前出现的前缀和，满足「当前前缀和a - 该前缀和b == k」，它出现的次数，累加给 count。
*   「当前前缀和 - 该前缀和 == k」等价于 「该前缀和 == 当前前缀和-k」

    遍历数组，根据当前“前缀和”，在 map 中寻找「与之相减 == k」的历史前缀和
    当前“前缀和”与历史前缀和，差分出一个子数组，该历史前缀和出现过 c 次，就表示当前项找到 c 个子数组求和等于 k。
    遍历过程中，c 不断加给 count，最后返回 count。
    """

if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    # print(Solution().subarrySum_native(nums, k))
    print(Solution().subarraySum(nums, k))
```



# 11. 哈希表

[41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/) hard

- 映射关系  nums[i]=i+1

- nums[nums[i]-1]≠nums[i] 如何理解？

- nums[i] ≠ i+1 （现在的位置不满足，i是下标）

- nums[i]-1 是应该要放置的index，要放置的位置也不满足nums[ num[i]-1 ] ≠ nums[i]-1+1 (nums[i]-1整体是index i )

- 位置交换，nums[nums[i]-1] = nums[i] 防止nums[i]改变，

  `nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] # 左边的会比右边的先赋值`

[136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/) easy

[448. 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/) easy





# 12. 二进制性质

位运算是2进制。

> 左移：m<<n —> m*2^n；
>
> 右移：m>>n —> m*2^(-n)；

针对奇数有：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。

```
# 举例：
#          0 = 0       1 = 1
#          2 = 10      3 = 11
```

针对偶数有：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。

```
# 举例：
#           2 = 10       4 = 100       8 = 1000
#           3 = 11       6 = 110       12 = 1100
```

如果n是2的幂，则1）n 二进制最高位为 1，其余所有位为 0；2）n−1 二进制最高位为 0，其余所有位为 1；[refer](https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/)

| 2^x  | n    | n - 1 | n & (n - 1)          |
| ---- | ---- | ----- | -------------------- |
| 2^0  | 0001 | 0000  | (0001) & (0000) == 0 |
| 2^1  | 0010 | 0001  | (0010) & (0001) == 0 |
| 2^2  | 0100 | 0011  | (0100) & (0011) == 0 |
| 2^3  | 1000 | 0111  | (1000) & (0111) == 0 |

> 因此，通过 `n > 0` 且 `n & (n - 1) == 0` 即可判定是否满足 n = 2^x。



# 13. 时间复杂度

判断字符是否在[栈]上存在需要 O(N) 的时间

判断字符是否在[hashmap]上存在需要 O(1) 的时间

查询给定字符是否在一个序列中存在的方法。根本上来说，有两种可能：
- 有序序列：可以二分法，时间复杂度大致是 O(logN)。
- 无序序列：可以使用遍历的方式，最坏的情况下时间复杂度为 O(N)。
  我们也可以使用空间换时间的方式，使用 N 的空间 换取 O(1)的时间复杂度——hashmap。

[461. 汉明距离](https://leetcode-cn.com/problems/hamming-distance/)求二进制中1的个数

```python
return bin(x^y).count('1')
```

# pytrick

- float("inf") # Python中可以用如下方式表示正负无穷：float("inf"), float("-inf")。

- lc31 对sort切片有了新的理解。

- 定义一个最大数 `dp=[sys.maxsize]*len(s)`。

- **子串一定的是连续的；**
- **子序列不一定是连续的一段，但是下标要求是递增的；**
- **子数组（子数组最少包含一个元素），要求下标是连续的；**







> 283、1047关于原地覆盖的问题，需要多次回顾。

134 for循环适合模拟从头到尾的遍历，而while循环适合模拟环形遍历，要善于使用while！



**递归函数的return：对递归函数什么时候要有返回值，什么时候不能有返回值很迷茫?**
**如果需要遍历整颗树，递归函数就不能有返回值。如果需要遍历某一条固定路线，递归函数就一定要有返回值！**



# python语法

A&B：无论A真假，B都运算。

A&&B：A真，B不运算。

for循环适合模拟从头到尾的遍历，而while循环适合模拟环形遍历，要善于使用while。

179 自定义比较函数

[关于 sorted 排序的多种情况](https://leetcode-cn.com/problems/top-k-frequent-words/solution/an-zhao-duo-ge-guan-jian-zi-pai-xu-by-ae-rd32/)

sorted默认升序；修改reverse=True参数，改为降序；

`nums = sorted(nums, key=abs, reverse=True) # 将nums按绝对值从大到小排列`

```python
# people[i] = [hi, ki]
# 按照第一个元素降序排，按照第二个元素升序排；
# lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序
people.sort(key=lambda x: (-x[0], x[1]))
```

```python
# points = [[10,16],[2,8],[1,6],[7,12]]
points.sort(key=lambda x: x[0]) # 按照第一个元素升序 # [[1, 6], [2, 8], [7, 12], [10, 16]]
```

```python
hash = collections.Counter(words)
res = sorted(hash, key=lambda word:(-hash[word], word)) #词频 倒序排列, 若词频相同，按字母顺序排序 正序排列
```

词频正序， 字母正序
`sorted(hash, key=lambda word:(hash[word], word))`

词频倒序， 字母倒序 （reverse=True 即将sorted方法修改为倒序排列）
`sorted(hash, key=lambda word:(hash[word], word), reverse=True)`

词频倒序， 字母正序（本题要求）
`sorted(hash, key=lambda word:(-hash[word], word))`

词频正序， 字母倒序
`sorted(hash, key=lambda word:(-hash[word], word), reverse=True)`



`list(str(n)) # 332->['3','3','2']`

- 切片

```python
nums = [1,2,3,4,5]
print(nums[:1]) # [1]
print(nums[:0]) # []
所以，nums[0:0] return 0
```

```python
# python判断字符是不是小写字母
# 如果是小写字母，返回大写
# 如果是大写字母，返回小写
from string import ascii_lowercase
if ch in ascii_lowercase:
    return ch.upper()
else:
    return ch.lower() 
```

将数字807转为[8, 0, 7]，`sums_list = list(map(int, str(sums)))`。

字典dict删除元素用pop()



字符串s转为列表 `ss=list(s)`

2进制转10进制 `int("100111",2)`



判断字符串s是否是本身是否是数字

```python
a = '12'
print(a.isdigit()) # True
```

ord()

```python
ord('1') # 49
ord('0') # 48
ord('A') # 65
ord('a') # 97
```





最大值 `max_int=2<<31`；


# top200未做题目

- [ ] 164 hard 基数排序
- [ ] 166 middle 竖式除法

【sql】

- [ ] 176 middle

- [ ] 177 middle

- [ ] 178 middle

- [ ] 180 middle
- [ ] 184 middle
- [ ] 185 hard

【bash】

- [ ] 192 middle
- [ ] 194 middle

# 常用模板

[1,2,3] list求和为123

```python
def get_sum(self, nums):
    s = 0
    for x in nums:
        s = s*10+x
    return s
```



# 重要算法

- 214 最短回文数（KMP算法,hard）
- 208 （字典树/前缀树）
- 214 kmp 
- 

刷题时光轴

2021/10/12回归呜呜

2021/12/06