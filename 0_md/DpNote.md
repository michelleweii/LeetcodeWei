Fighting!

# 一维DP

明确概念，

- 数组：要求连续`i-1, i, i+1`;
- 子序列：不要求连续`i-3, i, i+5`;

序列dp https://leetcode.cn/problems/number-of-longest-increasing-subsequence/solution/gong-shui-san-xie-lis-de-fang-an-shu-wen-obuz/

dp套路，

- 单个数组或者字符串要用动态规划时，可以把动态规划 `dp[i]` 定义为 `nums[0:i]` 中想要求的结果；
- 当两个数组或者字符串要用动态规划时，可以把动态规划定义成两维的 `dp[i][j]` ，其含义是在 `A[0:i]` 与 `B[0:j]` 之间匹配得到的想要的结果。

【**小技巧**】

- 求多少种 or **方案数** or 数量？状态与状态之间**相加**。

- 一般字符串的题都需要多初始化一位，`dp = [False] * (len(s)+1)`，一般都要考虑空串，然后才是1个字符、2个字符...len(s)个字符。

- 如果没有任何一组解，返回-1。`return -1 if dp[amount]==max_int else dp[amount]`，先给答案赋一个大数，如果没改变就return -1，改变就返回值。

--------

[序列dp题目集合](https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/gong-shui-san-xie-lis-de-fang-an-shu-wen-obuz/)

### LC53.最大子数组和

题目：`nums = [-2,1,-3,4,-1,2,1,-5,4]`，连续子数组 `[4,-1,2,1]` 的和最大，为 6 。

状态定义（序列DP）：`dp[i]`表示以 `nums[i]` **结尾** 的 **连续** 子数组的最大和。

转移方程：根据状态的定义，由于 `nums[i]` 一定会被选取。`dp[i-1]` 有可能是负数，所以问题转为`dp[i-1]`选or不选。

`dp[i] = max(nums[i], dp[i-1]+nums[i])`

### LC300.最长递增子序列

题目：`nums = [0,1,0,3,2,3]`，最长递增子序列是 `[0,1,2,3]`，因此长度为 4。

状态定义（序列DP）：`dp[i]` 的值代表 `nums` 以 `nums[i]` 结尾的最长子序列长度。

转移方程：`dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)`。

```python
# 我的疑问？为什么不能只判断前一位？而是要判断前面的所有位？
# 因为题目是子序列，不要求下标连续！！！

# max也不能少！为啥呢?
# 因为在遍历[0,j)的时候，dp[i]的值会一直变化，如果不加max，则dp[i]一定等于最后一个状态j的值+1；
# 但是此刻状态不一定是最大的。
def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

### LC673.最长递增子序列的个数（没懂）

[LC673.最长递增子序列的个数](https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-dp673-9txt/) 题目，给定一个未排序的整数数组，找到最长递增子序列的个数。`[1,3,5,4,7]`，答案是2，有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

状态定义（序列DP）：

1. dp[i]：以 `nums[i]` 结尾的最长递增子序列长度；
2. count[i]：以`nums[i]`为结尾的字符串，最长递增子序列的个数；

转移方程：

`count[i]`的更新难死啦~！

> 那么如何更新count[i]呢？
>
> 以nums[i]为结尾的字符串，最长递增子序列的个数为count[i]。
>
> 1、那么在nums[i] > nums[j]前提下，如果在[0, i-1]的范围内，找到了j，使得dp[j] + 1 > dp[i]，说明找到了一个更长的递增子序列。
>
> ​	那么以j为结尾的子串的最长递增子序列的个数，就是最新的以i为结尾的子串的最长递增子序列的个数，即：count[i] = count[j]。
>
> 2、在nums[i] > nums[j]前提下，如果在[0, i-1]的范围内，找到了j，使得dp[j] + 1 == dp[i]，说明找到了两个相同长度的递增子序列。
>
> ​	那么以i为结尾的子串的最长递增子序列的个数 就应该加上以j为结尾的子串的最长递增子序列的个数，即：count[i] += count[j];

```python
for i in range(1,len(nums)):
    for j in range(i):
        # 更新最长递增子序列长度
        # 说明找到了一个更长的递增子序列
        if nums[i]>nums[j] and dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                cnt[i] = cnt[j] # 【Attention】
        # 更新最长递增子序列个数
        # 说明找到了两个相同长度的递增子序列
        elif nums[i]>nums[j] and dp[i] == dp[j]+1:
            print(i,j, dp[i], dp[j]+1) # 4 3 4 4
            cnt[i] += cnt[j]
            # 【Attention】
            # [1,3,5], 以nums[2]为结尾的LIS，那么cnt[2]=1
            # [1,3,4], 以nums[3]为结尾的LIS，那么cnt[3]=1
            # 所以 cnt[4] = cnt[4]+cnt[3] = 2， 以nums[4]为结尾的最大个数
            # 有2个状态可以转换过来
    max_len = max(max_len,dp[i]) # 最长递增子序列的长度

for k in range(len(nums)):
    # 以nums[k]结尾的最长递增子序列长度
    if dp[k] == max_len:
        res += cnt[k]
return res
```

### LC198.打家劫舍

入门题，核心 **选or不选**！

状态定义：`dp[i]`表示前 `i` 间房屋能偷窃到的最高总金额。

转移方程：`dp[i]=max(dp[i−2]+nums[i],dp[i−1])`。 选nums[i] vs. 不选nums[i]。

### LC213.打家劫舍2

与LC198不同，该题是环型，首尾会联系。解题思路是转化成2个LC198打家劫舍。

状态定义：`dp[i]` 代表前` i `个房子在满足条件下的能偷窃到的最高金额。

转移方程：`dp[i] = max(dp[i-1], dp[i-2]+nums[i])`。

```python
#         转化成2个打家劫舍
#         /*分析：依然使用动态规划,只不过最后一个元素需要特殊处理
#         * 核心：第一个元素与最后一个元素,只能取一个--->分解成两问题*/
#         // 遍历dp --> 不用最后一个元素
#         // 遍历dp --> 不用第一个元素

# /*
# 环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃，
# 因此可以把此环状排列房间问题约化为两个单排排列房间子问题(198)：
# 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是p1；
# 在不偷窃最后一个房子的情况下（即 nums[:n-1]），最大金额是p2。
# 综合偷窃最大金额： 为以上两种情况的较大值，即 max(p1,p2)。
# */
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n==0:return 0
        if n==1:return nums[0]
        res1 = self.rob_range(nums, 0, n-2) # 遍历dp --> 不用最后一个元素
        res2 = self.rob_range(nums, 1, n-1) # 遍历dp --> 不用第一个元素
        return max(res1,res2)

    # lc198
    def rob_range(self, nums, start, end):
        if start==end:return nums[start]
        dp = [0]*len(nums)
        dp[start] = nums[start]
        dp[start+1] = max(nums[start], nums[start+1])
        for i in range(start+2, end+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]) # 不选第i个屋子，选第i个屋子

        return dp[end] # dp[-1]
```

### LC337.打家劫舍3

[LC337.打家劫舍3](https://www.programmercarl.com/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.html#_337-%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D-iii)题目，树节点都当做路径点，在一棵树上打家劫舍。如果抢了当前节点，两个孩子就不能动，如果没抢当前节点，就可以考虑抢左右孩子（**注意这里说的是“考虑”**）。

状态定义（树型dp）：`dp[0][1]`下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。

转移方程：` val2 = max(left[0], left[1]) + max(right[0], right[1])`

```python
# 树形DP就是在树上进行递归公式的推导
class Solution:
    def rob(self, root: TreeNode):
        if not root:return 0 # 没有node时
        if not root.right and not root.left: return root.val # 只有一个根节点时
        # dp = # 注意这里没有dp数组，遍历树的时候记录结果
        # 长度为2的数组，0：不偷，1：偷
        dp = self.rob_tree(root)
        return max(dp[0],dp[1])

    # 后序遍历
    # 首先明确的是使用后序遍历。 因为通过递归函数的返回值来做下一步计算。
    def rob_tree(self, cur):
        if not cur:return [0, 0] # 确定终止条件，在遍历的过程中，如果遇到空节点的话，很明显，无论偷还是不偷都是0
        left = self.rob_tree(cur.left)
        right = self.rob_tree(cur.right)
        # 偷cur
        # 那么cur的左右孩子要跳过, left[0] + right[0]
        val1 = cur.val + left[0] + right[0]
        # 不偷cur
        val2 = max(left[0], left[1]) + max(right[0], right[1])
        # 如果不偷当前节点，那么左右孩子就可以偷，至于到底偷不偷一定是选一个最大的，
        # 所以：val2 = max(left[0], left[1]) + max(right[0], right[1]);
        return [val2, val1]
```

### LC5.最长回文子串

状态定义：`dp[i][j]` 表示 s[i, j] 是否是回文串。

转移方程：`dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]`。

```python
# s[i..j]，所以必然有i<=j
for j in range(1,n):
    for i in range(0,j):
        if s[i]!=s[j]:
            dp[i][j]=False
        else: # s[i]==s[j]
            if j-i+1<=3:
                dp[i][j]=True # aa, aba
            else:
                dp[i][j] = dp[i+1][j-1] # 从两边向里面
        # 只要 dp[i][j] == true 成立，就表示子串 s[i..j] 是回文，此时记录回文长度和起始位置
        if dp[i][j] and j-i+1>maxlen:
            maxlen = j-i+1
            start = i
return s[start:start+maxlen]
```

### LC32.最长有效括号

给你一个只包含 `'('` 和 `')'` 的字符串，找出最长有效（格式正确且连续）括号子串的长度。[下标图例](https://leetcode-cn.com/problems/longest-valid-parentheses/solution/dong-tai-gui-hua-si-lu-xiang-jie-c-by-zhanganan042/)

状态定义：dp[i] 表示以 i 结尾的最长有效括号。

转移方程：`dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]`

思路分析：
1. 当 s[i] 为` (`, dp[i] 必然等于 0，因为不可能组成有效的括号；
2. 那么 s[i] 为 `)`
    2.1 当 s[i-1] 为` (`，那么 `dp[i] = dp[i-2] + 2`；
    2.2 当 s[i-1] 为 `)` 并且 `s[i-dp[i-1] - 1]` 为 `(`，那么 `dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]`；

```python
    def dp(self,s):
        if not s: return 0
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if s[i] == '(': dp[i] = 0  # <---- 虽然已经初始化过
            if s[i] == ')' and i > 0:
                if s[i-1] == '(':
                    if i - 2 >= 0:  # <---- 判断 i - 2
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif s[i-1] == ')' and s[i - dp[i-1] - 1] == '(' and i - dp[i-1] - 1 >= 0:
                    if i - dp[i-1] - 2 >= 0:   # <---- 判断 i - dp[i-1] - 2
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
                    else:
                        dp[i] = dp[i-1] + 2
        return max(dp)
```

### LC70.爬楼梯

状态定义：`dp[i]`代表爬到有i个台阶的楼顶，有dp[i]种方法。

转移方程：`dp[i] = dp[i-1]+dp[i-2] # 可以爬 1 或 2 个台阶`

```python
if n<=2:return n
dp = [0]*(n+1) # 爬到有i个台阶的楼顶，有dp[i]种方法。
dp[1] = 1 # 1阶台阶,只有一种方式(1)
dp[2] = 2 # 2阶台阶,有两种方式(1+1, 2)
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2] # 可以爬 1 或 2 个台阶
return dp[n]
```

### LC91.解码方法

状态定义：以`s[i]`结尾的解码方案数。即定义 `dp[i]` 为考虑前 i 个字符的解码方案数。

状态转移：

```python
f[i]=f[i−1],1⩽a≤9
f[i]=f[i−2],10⩽b⩽26
f[i]=f[i−1]+f[i−2],1⩽a≤9,10⩽b⩽26
```

具体代码，

```python
class Solution:
    def numDecodings2(self, s):
        if s[0] == '0': return 0 # 前导0为无效
        if len(s) == 1: return 1
        legalstr = set(str(i) for i in range(1, 27)) # 合法集合
        # print(legalstr)
        dp = [0] * (len(s))
        dp[0] = 1 # s[0]只有一种方案数
        if s[1] not in legalstr:  # s[1]为0时，只能和s[0]进行组合。
            dp[1] = 1 if s[: 2] in legalstr else 0
        else: # s[1]不是0时，可以组合，可以单独出结果
            dp[1] = 2 if s[: 2] in legalstr else 1
        # 因为要用到i-2 所以至少初始化 dp[0] dp[1]
        for i in range(2, len(s)):
            if s[i] not in legalstr:
                # 向前一位组合
                if s[i - 1: i + 1] in legalstr:
                    dp[i] = dp[i-2]
            else:
                if  s[i - 1: i + 1] in legalstr:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]

        return dp[-1]
```

### LC96.不同的二叉搜索树（卡特兰数 公式）

[LC96.不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/solution/dong-tai-gui-hua-python-bu-tong-de-er-ch-jpog/) 给定整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？

状态定义：`f(i)`表示以第`i`个结点为根的二叉搜索树的种类。`G(n)`代表`n`个结点可以构成BST种类。

假设`n`个结点可以构成`G(n)`种不同的二叉树，令`f(i)`表示以第`i`个结点为根的二叉搜索树的种类，所以有:
`G(n) = f(1)+f(2)+f(3)+......+f(n)`
而当`i`为根节点时，左孩子结点有`i-1`个，右孩子结点有`n-i`个，所以有
`f(n) = G(i-1) * G(n-i)`
两式联立可得：
`G(n)=G(0)G(n-1) + G(1)G(n-2) + ...... + G(n-2)G(1) + G(n-1)G(0)`

> 举个例子，dp[5]指的就是5个连续数字可以组成的二叉搜索树的个数
> 这5个数字不一定是[1,2,3,4,5]，也可以是[7,8,9,10,11]，只要是i个连续的数，就一定可以排列出dp[i]个二叉搜索树。

转移方程：

```python
class Solution:
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                # G(n) = G(0)*G(n-1) + G(1)*(n-2) + ... + G(n-1)*G(0)
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]
```

### LC132.分割回文串2hard（没做）

状态定义：

转移方程：



### LC152.乘积最大子数组

[LC152.乘积最大子数组 输入[2,3,-2,4]，子数组 [2,3] 有最大乘积 6。

> 思路：需要维护两个变量，当前的最大值，以及最小值，最小值可能为负数，
>
> 但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了
>
> 注意元素为0的情况，如果A[i]为0，那么maxDP和minDP都为0，我们需要从A[i + 1]重新开始。

状态定义：两个DP分别定义为【以i结尾的子数组】的最大积与最小积。

转移方程：

```python
#  //最大积的可能情况有：元素i自己本身，上一个最大积与i元素累乘，上一个最小积与i元素累乘；
#  //与i元素自己进行比较是为了处理i元素之前全都是0的情况；
for i in range(1,n):
  max_dp[i] = max(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
  min_dp[i] = min(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
  #  //记录ans；
  res = max(res, max_dp[i])
```

### LC338.比特位计数easy

[LC338.比特位计数easy](https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/)计算从 0 到 n 的每个整数的二进制表示中的 1 的数目。

状态定义：数字`i`的二进制中含`dp[i]`个 1。

转移方程：

```python
# 0的二进制0个, dp[0]=0
# 【二进制】性质有，
数字分为奇数、偶数，
针对奇数有：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
#           举例：
#          0 = 0       1 = 1
#          2 = 10      3 = 11
针对偶数有：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，
除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。
#            举例：
#           2 = 10       4 = 100       8 = 1000
#           3 = 11       6 = 110       12 = 1100

# 根据奇偶性开始遍历计算
for i in range(1,n+1):
  # 如果是奇数
  if i%2==1:
     dp[i]= dp[i-1]+1
  # 如果是偶数
  else:
      dp[i] = dp[i//2]
```



# 背包问题

https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/

背包问题具备的特征：是否可以根据一个 target（直接给出或间接求出），target 可以是数字也可以是字符串，再给定一个数组 arrs，问：能否使用 arrs 中的元素做各种排列组合得到 target。

## 01背包

> 最基本的背包问题就是 01 背包问题：一共有 N 件物品，第 i（i 从 1 开始）件物品的重量为 w[i]，价值为 v[i]。在总重量不超过背包承载上限 W 的情况下，能够装入背包的最大价值是多少？

如果是 **01 背包**，即数组中的元素不可重复使用，**外循环遍历 arrs**，**内循环遍历 target**，且**内循环倒序**。

**01背包要优化空间，所以内循环的背包容量target要倒序。**

[一套框架解决背包问题](https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/)

### LC416.分割等和子集

[LC416.分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/) 请你判断是否可以将`nums = [1,5,11,5]`分割成两个子集，使得两个子集的元素和相等。数组可以分割成 [1, 5, 5] 和 [11]，返回True。

思路：target 是什么？sum//2。

状态定义：`dp[i]` 表示是否存在和为 i 的 组合。

转移方程：`dp[j] = dp[j] or dp[j-x] # 不选or选`。

```python
# 01背包--dp[i][j]表示从数组的 [0, i] 这个子区间内挑选一些正整数，
# 每个数只能用一次，使得这些数的和恰好等于 j
dp = [False for _ in range(target+1)]
dp[0] = True # 什么都不取 # dp[i] 表示是否存在和为 i 的 组合
#【模板】外循环遍历 arrs，内循环遍历 target，且内循环倒序
for x in nums: # 遍历物品体积
    for j in range(target, x-1, -1): # i>=x # 遍历背包容量，背包容量必然要>=物品体积
      dp[j] = dp[j] or dp[j-x] # 不选or选
```

LC474.一和零

[lc474.一和零 middle](https://leetcode-cn.com/problems/ones-and-zeroes/solution/gong-shui-san-xie-xiang-jie-ru-he-zhuan-174wv/)题目也太复杂！

### LC494.目标和

[LC494.目标和](https://leetcode-cn.com/problems/target-sum/solution/gong-shui-san-xie-yi-ti-si-jie-dfs-ji-yi-et5b/) 给你一个整数数组 `nums=[1,1,1,1,1]` 和一个整数 `target=3`，nums中的数字可以+ or -，运算结果为target的表达式方案数。

核心：转为 总和为某个值（求pos的值） --> 背包问题 --> 动态规划。

题目转为：从nums[i]中挑选数字，只做+，这些数字满足`sumA=(sum + target)//2`。

> 【数学知识】
>
> 我们想要的 target = 正数和 - 负数和 = x - y；
>
> 已知 x 与 y 的和是数组总和：x + y = sum；
>
> 可以求出 x = (target + sum) / 2 ， 我们令『正值部分』的绝对值总和为x。
>
> 问题转换为-> **只使用 - 运算符（只做减法），从 nums 凑出 x 的方案数。**
>
> [详细推导](https://leetcode-cn.com/problems/target-sum/solution/hen-xiang-xi-de-zhuan-hua-wei-0-1bei-bao-irvy/)
>
> 每个数字都有两种状态：被进行“+”， 或者被进行“-”，因此可以将数组*<u>分成</u>*A和B两个部分：
> A部分的数字全部进行“+”操作，B部分的数字全部进行“-”操作。
>
> 设数组的和为sum，A部分的和为sumA，B部分的和为sumB
> 根据上面的分析，我们可以得出： sumA + sumB = sum (1)
> 同时有： sumA - sumB = target (2)
> 将(1)式与(2)式相加，可以得到： 2sumA = sum + target (3)
>
> 即：sumA = (sum + target) / 2 ，自此，原问题可以转化为0-1背包问题：
> 有一些物品，第i个物品的重量为nums[i]， 背包的容量为sumA，问：有多少种方式将背包【恰好填满】
>
> 这里需要注意的是，由于每个数字都是非负整数，因此sumA, sumB, sum都是非负整数。
> 根据(3)， 2sumA一定为偶数(自然数的性质，2n是偶数)，因此sum + target也应该是偶数。如果计算出的sum + target不是偶数，则与推导过程矛盾，本题无解。

状态定义：`f[i][j]`为从 nums 凑出总和「恰好」为 `j` 的方案数。

<u>优化后：`dp[i]` 表示和为 `i` 的 num 组合有 `dp[i]` 种。</u>

转移方程：这道题的关键不是nums[i]的选与不选，而是nums[i]是加还是减，那么我们就可以将方程定义为，`f[i][j]=f[i−1][j]+f[i−1][j-nums[i−1]]`，优化后，`dp[i] = dp[i] + dp[i-num]`

```python
class Solution:
    def findTargetSumWays(self, nums, target):
        sums = sum(nums)
        if target>sums or (sums + target) % 2 == 1: return 0
        positive = (target+sums)//2
        dp = [0]*(positive+1) # 表示和为 i 的 num 组合有 dp[i] 种。
        dp[0] = 1 # 表示只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案。
        for num in nums: # 物品体积
            for i in range(positive, num-1, -1): # 背包容量
                # f[i][j]=f[i−1][j]+f[i−1][j+nums[i−1]]
                dp[i] = dp[i] + dp[i-num] # i >= num，
                # 背包容量i要大于物品体积num
                # dp[i] 不选
                # dp[i-num] 选
        return dp[positive]
```

879.盈利计划 hard

## 完全背包

> 完全背包与 01 背包不同就是每种物品可以有无限多个：一共有 N 种物品，每种物品有无限多个，第 i（i 从 1 开始）种物品的重量为 w[i]，价值为 v[i]。在总重量不超过背包承载上限 W 的情况下，能够装入背包的最大价值是多少？
> 可见 01 背包问题与完全背包问题主要区别就是物品是否可以重复选取。

（1）如果是完全背包，即数组中的元素可重复使用并且不考虑元素之间顺序，arrs 放在外循环（保证 arrs 按顺序），target在内循环。且内循环正序。

（2）如果组合问题需考虑**元素之间的顺序**，需将 target 放在外循环，将 arrs 放在内循环，且内循环正序。

### LC139.单词拆分

[LC139.单词拆分](https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/)给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。请你判断是否可以利用字典中出现的单词拼接出 `s` 。 `s = "leetcode"`, `wordDict = ["leet", "code"]`，返回True。

**注意：**不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。-->考虑顺序的完全背包。codeleet就是False，当然是考虑顺序的。

状态定义：`dp[i]` 表示以 `i` 结尾的字符串是否可以被 wordDict 中单词组合而成。

转移方程：`dp[i] = dp[i] or dp[i-sz]`

```python
class Solution:
    def wordBreak(self, s: str, wordDict):
        # dp[i] 表示以 i 结尾的字符串是否可以被 wordDict 中组合而成
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for word in wordDict:
                sz = len(word)
                # if i-word_len>=0:print(i, word_len, s[i-word_len: i])
                if i-sz>=0 and s[i-sz: i] in wordDict:
                    dp[i] = dp[i] or dp[i-sz]
                    # 选 dp[i]
                    # 不选 dp[i-sz]
        return dp[-1]
```

### LC322.零钱兑换

状态定义：`dp[i]`为构成金额`i`所需的最少的硬币数。

题目是『不考虑元素顺序的完全背包』，一个硬币可以重复拿。

举例，`coins = [1, 2, 5]`, `amount = 11`，返回`3`，因为`11 = 5 + 5 + 1`。

转移方程：`dp[i] = min(dp[i], dp[i-coin]+1)`。

> 不考虑元素之间顺序，arrs 放在外循环（保证 arrs 按顺序），target在内循环。且内循环正序。

```python
class Solution(object):
    def coinChange2022(self, coins, amount):
        max_int = 2 << 31
        dp = [max_int]*(amount+1) # 构成金额i的最少硬币数
        dp[0] = 0  # 构成金额0，需要0个硬币数
        for coin in coins: # 外层遍历arrs
            for i in range(amount+1): # 内层遍历target
                # 物品体积不能大于背包容量
                if coin<=i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount]==max_int else dp[amount]
```

### LC518.零钱兑换2

LC322是求构成target的硬币数，LC518是构成target的<u>***方案数***</u>（有几种）。

状态定义：`dp[i]` 表示和为 i 的 coin 组合有 `dp[i]` 种。

转移方程：`dp[i] = dp[i]+dp[i-coin]`。

```python
class Solution:
    def change(self, amount, coins):
        # dp[i] 表示和为 i 的 coin 组合有 dp[i] 种。
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1 # 只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案
        for coin in coins: # 外层arrs
            for i in range(amount+1): # 内层target
                # 物品体积不能大于背包容量
                if i>=coin:
                    dp[i] = dp[i]+dp[i-coin]
        return dp[amount]
```

### LC279.完全平方数

[题意](https://leetcode-cn.com/problems/perfect-squares/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-nqes/) 给你一个整数 `n` ，返回 *和为 `n` 的完全平方数的最少数量* 。

状态定义：dp[i] 表示完全平方数和为i的 最小个数。

转移方程：`dp[j] = min(dp[j],dp[j-curr]+1)`

```python
def numSquares(self, n: int) -> int:
    # 不要求顺序的完全背包13=4+9，13=9+4
    # 初始化一个大值（不能达到的）
    dp = [0] + [n] * n # [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
    rg = int(n**0.5) # 开根
    # 遍历arrs
    for i in range(1, rg + 1): # 1.2.3
        curr = i * i # 1.4.9
        # 遍历target
        for j in range(curr,n+1):
            dp[j] = min(dp[j],dp[j-curr]+1)
    return dp[n]
"""
    # dp[i]：表示完全平方数和为i的 最小个数
    # 初始状态dp[i]均取最大值i，即 1+1+...+1，i个1; dp[0] = 0
    # dp[i] = min(dp[i], dp[i-j*j]+1)，其中, j是平方数, j=1~k,其中k*k要保证 <= i
    # 意思就是：完全平方数和为i的 最小个数 等于 当前完全平方数和为i的 最大个数
    #   与 （完全平方数和为 i - j * j 的 最小个数 + 完全平方数和为 j * j的 最小个数）
    #   可以看到 dp[j*j] 是等于1的
"""
```

### LC377.组合总和

从`nums = [1,2,3]`中重复挑选`num`构成`target = 4`，顺序不同的序列被视作不同的组合**<u>*（方案数）*</u>**。

状态定义：`dp[i]` 表示和为 i 的 num 组合有 `dp[i]` 种。

转移方程：`dp[i] += dp[i - num]`。

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1) # 和为 i 的 num 组合有 dp[i] 种
        dp[0] = 1 # 当不选取任何元素时，元素之和才为 0，因此只有 1 种方案
        for i in range(1, target + 1): # 外层循环target
            for num in nums: # 内层循环arrs
                if num <= i: # 物品体积不能大于背包容量
                    dp[i] += dp[i - num] # 求方案数套路
        return dp[target]
```

LC1449.数位成本和为目标值的最大数字 hard

状态定义：

转移方程：

# 二维DP

大概分为一下几步，

1. 状态定义；
2. 定义出口；
3. 初始化边界；
4. 状态转移方程；

> 求方案数的基本都是相加的。

## 初始化

以[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)为例，状态定义

```python
dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数
```

一般都是表示前 i 个字符，前 j 个字符。e.g. 前5个字母，下标index=4。【这个错位一定要知道！】

初始化多申请一位的原因？

```python
m, n = len(word1), len(word2) # m行n列
dp = [[0] * (n + 1) for _ in range(m + 1)]
```

**考虑空字符串的因素，然后才是第一个字符到最后一个字符。**

删除一个元素`dp[i][j]=dp[i-1][j]+1`，

增加一个元素`dp[i][j]=dp[i][j-1]+1，`

替换一个元素`dp[i][j]=dp[i-1][j-1]`。

为什么是这样？因为题意要求从word1到word2，word1是可变的，word2是不可变的。

### LC72.编辑距离

状态定义：`dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数`。

转移方程：

```python
dp = [[0] * (n+1) for _ in range(m+1)] # 多一位表示空字符
word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]
# 替换，删除，增加
word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
```

### LC97.交错字符串

[LC97.交错字符串](https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/) 题目：给定三个字符串 `s1`、`s2`、`s3`，请你帮忙验证 `s3` 是否是由 `s1` 和 `s2` **交错** 组成的。

`s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac", True.`

状态定义：`dp[i][j]表示 s1 的前i个(s1[i-1])个字符和s2的前j个(s2[j-1])字符是否能构成 s3 的前i+j个字符`。

转移方程：

s1的前i位和s2的前j位能否构成s3的前i+j(index=i+j-1)位，取决于2种情况：

1. s1最后一个字符和s3最后一个字符匹配；
2. s2最后一个字符和s3最后一个字符匹配；

```python
# 多初始化一维是为了放置空字符。
# dp[0][0] = True # s1的0个字符，s2的0个字符，当然可以构成s3的0个字符。

# 边界初始化
# 1、只由s1构成s3 # s1的前i位是否能构成s3的前i位
for i in range(1, len1+1):
  # s1的前i位能构成s3的前i位的前提条件是：
  # 前i-1位可以构成s3的前i-1位，且s1的第i位（s1[i-1]）等于s3的第i位（s3[i-1]）
  dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]

  # s1的前i位和s2的前j位能否构成s3的前i+j(index=i+j-1)位，取决于2种情况：
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # s1 的前 i 个字符和 s2 的前 j−1 个字符能否构成 s3 的前 i+j−1 位，# （s1最后一个字符和s3最后一个字符匹配）
        # or s2 的第 j 位（s2[j−1]）是否等于 s3 的第 i+j 位（s3[i+j−1]）。# （s2最后一个字符和s3最后一个字符匹配）
        dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) \
        or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
```

### LC115.不同的子序列

[LC115.不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/solution/shou-hua-tu-jie-xiang-jie-liang-chong-ji-4r2y/)题目：给定一个字符串 `s` 和一个字符串 `t` ，计算在 `s` 的子序列中 `t` 出现的个数。翻译为**『在 s 串身上 “挑选” 字符，去匹配 t 串的字符，求挑选的方式数』**

状态定义：从0到 `s[i-1]` 的子串中，出现『从0到 `t[j-1]` 的子串』的 次数。**即，从 前者 选字符，去匹配 后者 的方案数**

转移方程：

```python
# dp出口
# 1) 小到 t 变成空串，此时 s 为了匹配它，方式只有1种：什么字符也不用挑（或 s 也是空串，什么都不做就匹配了，方式数也是1）
# 2) 小到 s 变成空串，但 t 不是，s 怎么也匹配不了 t，方式数为 0
for i in range(s_len+1):
    for j in range(t_len+1):
        if j==0: dp[i][j] = 1 # 小到 t 变成空串
        # elif i==0:dp[i][j] = 0
        else:
            if s[i-1] == t[j-1]:
                # 核心是选or不选
                # 最后一个字符可以匹配
                # 情况一：用s的第i个字母匹配t的第j个字符，有 dp[i-1][j-1] 个匹配情况；
                # 情况二：不用s的第i个字母去匹配t的第j个字母, 情况就等于 dp[i-1][j]；
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # 为什么还要加没有配上的case呢？
            else:
                # 从s中挑选，最后一个字符不匹配，那么这个字符有和没有情况是一样的
                dp[i][j] = dp[i-1][j]
```

### LC10.正则表达式匹配

[LC10.正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/solution/shou-hui-tu-jie-wo-tai-nan-liao-by-hyj8/) 题目：给你一个字符串 `s` 和一个字符规律 `p`，请你来实现一个支持 `'.'` 和 `'*'` 的正则表达式匹配。翻译一下，p能不能变成s。

状态定义：`dp[i][j]`表示`s`的前`i`个字符与`p`的前`j`个字符是否能够匹配，Ture or False问题。

1. p[-1] 有3种情况，`. * 字符`。
2. `p[-1]=='*'`又有3种情况，`*`让它前面的字符出现`0/1/n`次。

转移方程，

```python
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
dp = [[False] * (p_len+1) for _ in range(s_len+1)] # 状态定义

# 出口，用p的前0个字符去匹配s的前0个字符
# 1、s为空，p为空，能匹配上
dp[0][0] = True
# 2、p为空，s不为空，必为false(boolean数组默认值为false，无需处理)
# 3、s为空，p不为空，由于*可以匹配0个字符，所以有可能为true
"""
base case
p为空串，s不为空串，肯定不匹配。
- s为空串，但p不为空串，要想匹配，只可能是右端是星号，它干掉一个字符后，把 p 变为空串。
s、p都为空串，肯定匹配。
"""
for j in range(1, p_len+1):
    if p[j-1]=='*': dp[0][j] = dp[0][j-2]

# 4、填表（状态转移）
for i in range(1, s_len+1):
    for j in range(1, p_len+1):
        # dp[i][j]表示s的前i个字符s[0:i-1]与p的前j个字符p[0:j-1]是否匹配
        if s[i-1]==p[j-1] or p[j-1]=='.':
            dp[i][j] = dp[i-1][j-1]
        # *特判, *可以让它前面的字符出现0-n次
        if p[j-1]=='*':
            if s[i-1]==p[j-2] or p[j-2]=='.':
                # dp[i][j] = dp[i-1][j-2] # *让它前面的字符出现1次,  aa与a*以及 aa与.*
                # dp[i][j] = dp[i-1][j-3] # *让它前面的字符出现0次， aa与aac*
                # 还可以dp[i][j] = dp[i][j-2]
                # dp[i][j] = dp[i-1][j] # *让它前面的字符出现多次， aaaaaaa与a*
                dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
            elif s[i-1]!=p[j-2]: # a与ab*, 干掉b
                dp[i][j] = dp[i][j-2]
```

### LC1143.最长公共子序列

[LC1143.最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/)

状态定义：`dp[i][j]` 表示 `text1[0:i-1]` 和 `text2[0:j-1]` 的最长公共子序列。

> （注：`text1[0:i-1]` 表示的是 text1 的 第 0 个元素到第 i - 1 个元素，两端都包含）
> 之所以 `dp[i][j]` 的定义不是 text1[0:i] 和 text2[0:j] ，是为了方便当 i = 0 或者 j = 0 的时候，`dp[i][j]`表示为空字符串和另外一个字符串的匹配，这样 `dp[i][j]` 可以初始化为 0。

转移方程，

```python
for i in range(1, m+1):
    for j in range(1, n+1):
        # 举个例子，比如对于 ace 和 bc 而言，
        # 他们的最长公共子序列的长度等于 ① ace 和 b 的最长公共子序列长度0;
        # ② ac 和 bc 的最长公共子序列长度1 的最大值，即 1。
        if text1[i-1]==text2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

-----

### LC62.不同路径

[62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

状态定义：`到达网格(i,j)时, 共有 dp[i][j] 种走法。`

转移方程：

```python
# 左上角到右下角，每次只能向下或者向右移动一步。问总共有多少条不同的路径？
dp = [[0 for j in range(n)] for i in range(m)] # 不用表示空字符
dp[i][j] = dp[i-1][j]+dp[i][j-1] # 将向右和向下两条路径的方案数相加起来。
```

### LC63.不同路径2

[63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)与LC62不同，本次路径中障碍物，不能走。

状态定义：`dp[i][j]表示从(0,0)走到(i,j)的所有不同路径的方案数`。

转移方程：

```python
# 重点：如果网格 (i, j) 上有障碍物，则 dp[i][j] 值为 0，表示走到该格子的方案数为 0；
# dp[0][0] = 1，从(0,0)到达(0,0)只有一条路径
for i in range(1,m):
  for j in range(1,n):
    if obstacleGrid[i][j]==0: # 多一个限制条件，不是障碍物的时候才转移。
      dp[i][j] = dp[i-1][j]+dp[i][j-1]
```

### LC64.最小路径和

状态定义，

转移方程

### LC120.三角形最小路径和

[LC120.三角形最小路径和](https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/) 题目：给定一个三角形 `triangle` ，找出自顶向下的最小路径和。

**注意点：从下开始向上推。**

状态定义：`dp[i][j]`为从点`(i,j)`到<u>底边</u>的最小路径和。

转移方程，

```python
dp = [[0]*(m+1) for _ in range(m+1)] # (i,j)点到底边的最小路径和
# [i,j]
# [i+1,j] [i+1,j+1]
for i in range(m-1, -1, -1):
    for j in range(i, -1, -1):
        # 到达[i,j]的最短路径
        dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        ## 从三角形的最后一行开始递推，如下循环也ok
        # for (int i = n - 1; i >= 0; i--) 
        #     for (int j = 0; j <= i; j++) 
        return dp[0][0]
```

### LC174.地下城游戏（没做）

（不是特别重要，没考过）



### LC221.最大正方形

[LC221.最大正方形](https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/) 题目：在一个由 `'0'` 和 `'1'` 组成的二维矩阵内，找到只包含 `'1'` 的最大正方形，并返回其面积。

状态定义：`dp[i][j]` 以 `matrix[i][j] `为右下角的正方形的最大边长。

转移方程，

```python
# dp[i][j] 以 matrix[i-1][j-1] 为右下角的正方形的最大边长
# dp = [[0]*(n+1) for _ in range(m+1)] 
for i in range(0, m):
    for j in range(0, n):
        # //base case
        # 初始化边界值
        if (i == 0 or j == 0):
            dp[i][j] = int(matrix[i][j])
            if matrix[i][j]=='1':
                # 状态方程为什么这样呢？具体看链接里的图
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                max_side = max(max_side, dp[i][j]) # 记录最大边
# dp[i-1][j-1] 左上也记录的原因？
# 若形成正方形（非单 1），以当前为右下角的视角看，则需要：当前格、上、左、左上都是 1
```

### LC647.回文子串（矩阵遍历）

[LC647.回文子串](https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html#_647-%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2) 题目给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

状态定义：`dp[i][j]`表示区间范围`[i,j]` （注意是左闭右闭）的子串是否是回文子串。

输入："aaa" 输出：6 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"。

【注意】矩阵遍历一定要从下到上，从左到右遍历，这样保证`dp[i+1][j-1]`都是经过计算的。

转移方程：

```python
# 从下到上
for i in range(len(s)-1, -1, -1):
    # 从左到右
    # 因为dp[i][j]的定义，所以j一定是大于等于i的，那么在填充dp[i][j]的时候一定是只填充右上半部分
    for j in range(i, len(s)):
        if s[i] == s[j]:
            if j-i <= 1: # a, aa
                res += 1
                dp[i][j] = True
             elif dp[i+1][j-1]: # cabac
              	res += 1
              	dp[i][j] = True
return res
```

# 股票问题

[我的题解~](https://blog.csdn.net/weixin_31866177/article/details/119798636)

[通解](https://leetcode.cn/circle/article/qiAgHn/)

状态定义：

- 0：持有现金，买入股票需要减钱，需要减手续费；
- 1：持有股票，卖出股票需要加钱；
- return dp[][][0]，最后都是一个持有现金的状态。

`dp[i][j][flag] `

- **i 表示第i个交易日，也就是prices的第i个节点。**
- **j 是买入的次数，也就是记录交易次数（这里不是卖出）。**
- **flag 是否持有股票的标志，持有为1，没有0。**

转移方程，

```python
dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i]) # 不买股票，卖股票
dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]) # 不卖股票，买股票
```

### LC121.买卖股票的最佳时机（easy）

> （只能买卖一次股票，求最大利润）

状态定义：`dp[i]` 代表以 `prices[i]`为结尾的子数组的最大利润（以下简称为 **前 i 日的最大利润** ）。

转移方程： 由于题目限定 “买卖该股票一次” ，因此前`i` 日最大利润 `dp[i]` 等于前 `i-1`日最大利润 `dp[i-1]`和第 `i` 日卖出的最大利润中的最大值。

`前i日最大利润=max(前(i−1)日最大利润, 第i日价格−前i日最低价格)`

`max(dp[i-1], prices[i]-min(cost, prices[i])) `

```python
class Solution(object):
    # 只要考虑当天买和之前买哪个收益更高，当天卖和之前卖哪个收益更高
    # dp[i]以 prices[i]为结尾的子数组的最大利润（以下简称为 前 i 日的最大利润 ）
    # 扩展可以交易两次（买卖算一次交易）求最大值
    def maxProfit_dp(self, prices):
        if not prices: return 0
        dp = [0 for _ in range(len(prices))]
        cost = prices[0]
        for i in range(1, len(prices)):
            cost = min(cost, prices[i])
            dp[i] = max(dp[i-1], prices[i]-min(cost, prices[i])) 
        return max(dp)

    def maxProfit(self, prices):
        # 在价格最低的时候买入，差价最大的时候卖出
        if len(prices) < 2: return 0
        cost = prices[0] # 每日更新最低价格
        profit = 0 # 首日利润为0
        for price in prices:
            cost = min(cost, price) # 找到最低那天的价格
            profit = max(profit, price-cost)
        return profit
```

### LC122.买卖股票的最佳时机 II（middle）

> （可以买卖多次股票，求最大利润）

状态定义：`dp[i][j] 表示到下标为 i 的这一天，持股状态为 j 时，我们手上拥有的最大现金数。`

- 第一维 i 表示下标为 i 的那一天（ 具有前缀性质，即考虑了之前天数的交易 ）；
- 第二维 j 表示下标为 i 的那一天是持有股票，还是持有现金。***这里 0 表示持有现金（cash），1 表示持有股票（stock）。***

转移方程：

```python
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
dp = [[0]*2 for _ in range(n)]
dp[0][0] = 0 # 什么都不做，持有现金
dp[0][1] = -prices[0] # 持有股票，第一天买入股票，持有现金数为负

for i in range(1, n):
    # [0]现金状态，从持有股票的状态转来，再加上卖出股票的利润
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) # 持有现金，股票要卖出
    # [1]持股状态，从现金状态转来，再减去买入股票的价格
    dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]) # 持有股票，现金要减少
return dp[-1][0] # 最后一天，持有现金
```

### LC309.最佳买卖股票时机含冷冻期（middle）

> （可以买卖多次股票，但是卖出之后有一天冷冻期，求最大利润）

状态定义：`dp[i][j]` 表示 `[0, i]` 区间内，在下标为 i 这一天状态为 j 时，我们手上拥有的金钱数。***这里 0 表示持有现金（cash），1 表示持有股票（stock）。***

转移方程：

```python
# 初始化
dp[0][0] = 0 # 第0天，持有现金为0
dp[0][1] = -prices[0] # 第0天，持有股票-prices[0]
dp[1][0] = max(0, prices[1]-prices[0])# 第1天，持有现金(需要第0天买入，第1天卖出)
dp[1][1] = max(-prices[0], -prices[1])# 第1天，持有股票(第0天买股票，第1天可以不操作)
# 状态转移
for i in range(2, n):
    # 股票：买股票，可以什么都不做+可以从持有现金状态转为持有股票状态
    # 卖出 ---- 冷冻期 ----  买入
    dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    # 现金：卖股票，可以什么都不做+可以从股票状态转为现金状态
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
return dp[-1][0]
```

### LC714.买卖股票的最佳时机含手续费（middle）

> [（可以买卖多次股票，但是交易股票有手续费，求最大利润）](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/mai-mai-gu-piao-wen-ti-by-chen-wei-f-xvs1/)

状态定义：`dp[i][j]` 表示 [0, i] 区间内，在下标为 i 这一天状态为 j 时，我们手上拥有的金钱数。

转移方程：

```python
# 每次交易要支付手续费 我们定义在卖出的时候扣手续费
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
```

```python
# 初始化
dp[0][0] = 0 # 持有现金
dp[0][1] = -prices[0] # 持有股票

for i in range(1, n):
    # 从持有现金的状态，转为持有股票的状态
    dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
    # 从持有股票的状态，转为持有现金的状态
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee) # 定义在卖出的时候扣手续费
return dp[-1][0]
```

### LC901.股票价格跨度（middle）（单调栈）

### LC123.买卖股票的最佳时机 III（hard）

> （可以买卖 2 次股票，求最大利润）

状态定义：`dp[i][k][j]` 表示到下标为` i`的这一天，还可以交易`k`次，持股状态为`j`时，拥有的最大现金数。

转移方程：

```java
dp[i][k][0] = Math.max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
dp[i][k][1] = Math.max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
```

```python
# 结束时的最高利润=[第i天数][卖出次数][是否持有股票]
# [i,j]第i天，j持股状态。3是交易次数（0、1、2笔）
# int[][][] dp = new int[prices.length][3][2];
dp = [[[0, 0] for _ in range(3)] for _ in range(n)]

# 定义为-1之后初始化容易很多！！！
# 最后一天不可能卖出
# 存在0\1\2笔交易数状态
# 在没有进行股票交易时不允许持有股票
for k in range(3):
    dp[-1][k][1] = -float("inf")
    
# 一次都不交易，持有股票也是不存在的状态
for i in range(n):
    dp[i][0][1] = -float("inf")

for i in range(n):
    for k in range(1,3):# 最多只能买卖2次
        # 最多可以完成 两笔 交易，定义最多可以买2次股票
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i]) # 卖股票变成现金状态
        # [1]，从现金状态买入股票，转为持有股票状态
        # 买入一次，减去一次交易机会
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i]) # 买股票变成持股状态，买股票消耗一次机会
return dp[-1][2][0]
```

### LC188.买卖股票的最佳时机 IV（hard）

> （可以买卖 <=k 次股票，求最大利润）

状态定义：`dp[i][k][j]` 表示到下标为` i`的这一天，还可以交易`k`次，持股状态为`j`时，拥有的最大现金数。

转移方程：

```java
dp[i][k][0] = Math.max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
dp[i][k][1] = Math.max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
```

```python
# 说明我可以一天买，一天卖，退化成122的贪心做法，可以交易无限次
if k >= (n // 2):
    sum_num = 0
    for i in range(n-1):
        if prices[i] < prices[i + 1]:
            sum_num += prices[i + 1] - prices[i]
    return sum_num

dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]
# print(dp)
# -1天，没有开始交易，所以持股也是不存在的状态
for m in range(k+1):
    dp[-1][m][1] = -float("inf")
    
# 一次都不交易，持有股票也是不存在的状态
for i in range(n):
    dp[i][0][1] = -float("inf")

for i in range(n):
    for m in range(1, k+1):# 最多只能买卖k次
        dp[i][m][0] = max(dp[i-1][m][0], dp[i-1][m][1]+prices[i])
        # [1]，从现金状态买入股票，转为持有股票状态
        # 买入一次，减去一次交易机会
        dp[i][m][1] = max(dp[i-1][m][1], dp[i-1][m-1][0]-prices[i])
return dp[-1][k][0]
```

# 易混淆题目整理

LC53.最大子数组和

LC300.最长递增子序列->LC673.最长递增子序列的个数

LC152.乘积最大子数组

LC718.

LC674.

# 丑数







# 区间DP

[【一文团灭区间DP】](https://leetcode-cn.com/problems/burst-balloons/solution/yi-wen-tuan-mie-qu-jian-dp-by-bnrzzvnepe-2k7b/)

思想就是随着操作的进行，判断的范围越来越小，所以小长度开始遍历，逐步化解更大范围的问题，有分治的思想。模版：

```python
def helper(self, ns: List[int]) :
    N = len(ns)
    dp = [[0] * N for _ in range(N+1)]
    for lens in range(N): # 长度从小到大
        for i in range(N-lens): # 以 i 为 开头
            j = i + lens           # 以 j 为 终点
            for k in range(i,j): # 以 k 为分割点，进行分治         
                // Todo 业务逻辑 
```

总结：长度固定（由小到大），在区间内枚举`[i,j]`，区间长度要与固定长度保持一直，然后，在`[i,j]`内寻找最佳分割点`k`。
