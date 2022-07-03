# 回溯总结

-   组合问题 有start_index
-  分割问题 有start_index
-  子集问题 有start_index

-  排列问题 无start_index



- 如果原数组有重复数字，且要求解集不重复，需要使用used标记。
- 如果题目没有要求不能使用sort，那么用used就用sort()。例如LC491[递增子序列](https://leetcode-cn.com/problems/increasing-subsequences/)就不能sort()。
- <u>***全排列必有used***</u>，因为第一轮选2之后，第二轮要标记选过的位置，否则同一个位置的元素被重复选。一般来说，全排列才出现used，其他的问题视情况而定。
- 如果要求数组里使用过的数字不能再使用，需要有sort()。

## 组合、分割、子集

> start_index的核心
> 例如2，3，5，在第一层，
> 选2，余3&5
> 选3，余5
> 选5，余空
> 这是`for i in range(start_index,n-1)`的逻辑
> ***<u>因为组合问题里 [2,3]和 [3,2]是一样的***</u>

[LC40 组合总和](https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html#%E5%9B%9E%E6%BA%AF%E4%B8%89%E9%83%A8%E6%9B%B2) candidates 中的每个数字在每个组合中只能使用一次。 解集不能包含重复的组合。

1. 每个数字在每个组合中只能使用一次：

​		i+1表明一个数字只能使用一次。

```python
# i+1表明一个数字只能使用一次，这样下次递归的循环就从i+1开始了
self.dfs(candidates,target,sums,i+1) # 再向下一层
```

2. 解集不能包含重复的组合：

sort()之后，同一层相同的元素跳过。

```python
# 要对同一树层使用过的元素进行跳过
# 【核心】
if i>start_index and candidates[i] == candidates[i-1]:continue
# 这一步的处理也可以使用used，但是这样更方便。
```



## 排列

> **<u>*因为 [1,2] 和 [2,1]是不同的，所以不需要 start_index。*</u>**
>
> 例如2，3，5，在第一层，
> 选2，余3&5
> 选3，余2&5
> 选5，余2&3
> 每个数字轮流当首字母

[LC47 全排列](https://programmercarl.com/0047.%E5%85%A8%E6%8E%92%E5%88%97II.html#%E6%80%9D%E8%B7%AF) 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

全排列必有used，因为第一轮选2之后，第二轮要标记选过的位置，否则同一个位置的元素被重复选。

```python
for i in range(len(nums)):
    # 如果树层里重复取值，跳过
    #      // used[i - 1] == 1，说明同⼀树⽀nums[i - 1]使⽤过
    #      // used[i - 1] == 0，说明同⼀树层nums[i - 1]使⽤过
    #      // 如果同⼀树层nums[i - 1]使⽤过则直接跳过
    if i>0 and nums[i]==nums[i-1] and used[i-1]==0:  # i>0对len(nums)==1的很重要
        continue
    # 剪枝(如果当前的元素已经被用过，continue)
    # 排列问题特有的部分，因为没有start_index来标记元素是否访问
    if used[i]==1:
        continue
```

