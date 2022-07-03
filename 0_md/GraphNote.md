# DFS

2022/01/20为止，我理解的dfs好像就 **回溯** 和 **四周扩散遍历** 2种题型。

## 回溯模板

[回溯模板](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E5%9B%9E%E6%BA%AF%E6%B3%95%E6%A8%A1%E6%9D%BF)

**回溯算法中函数返回值一般为void。**

```c++
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }
		// for循环，横向遍历
    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归，纵向遍历
        回溯，撤销处理结果
    }
}
//for循环就是遍历集合区间，可以理解一个节点有多少个孩子，这个for循环就执行多少次。
```



**图的回溯for循环里有start_index概念，在LC257.二叉树的所有路径中，树的回溯没有start_index概念，只有node节点的概念。**

**图的回溯记得传参+start_index!!!**

int型变量startIndex，这个参数用来记录本层递归的中，集合从哪里开始遍历（集合就是[1,...,n] ）。

**每次从集合中选取元素，可选择的范围随着选择的进行而收缩，调整可选择的范围，就是要靠startIndex**。



组合和排序的区别？

**组合是不强调元素顺序的，排列是强调元素顺序**。记住组合无序，排列有序。


全排列就是回溯, 求最短路径也是DFS。

LC17求不同集合之间的组合，而LC77&LC216是求同一个集合中的组合!

dfs 剪枝是直接return，
for循环 剪枝是continue。

需要明确是递归函数的返回值，还是for循环的返回值（剪枝）。（每次都错）



组合问题中，需要明确题目要求。
有start_index。
candidates是否是无重复的，如果是则需要.sort(), 并利用used[]进行去重(根据题目)。
candidates中元素是否是可以被无限制选取的，如果是start_index=i，如果不是start_index=i+1，i+1可以实现去重。
解集不能包含重复的子集start_index+1。


LC40 结果集中不能有重复元素
```python
# 要对同一树层使用过的元素进行跳过
# 【核心】
if i>start_index and candidates[i] == candidates[i-1]:continue
```
切割问题就可以使用回溯搜索法把所有可能性搜出来。
startIndex，因为切割过的地方，不能重复切割，和组合问题也是保持一致的。


LC90 used标记去重法 vs LC491 对比学习！
used初始化为0，当同个元素使用则used[i]=1,
for下一个元素，如果nums[i]==nums[i-1], 如果used[i-1]=1，代表是树枝遍历，nums[i]可以用；
如果used[i-1]=0，代表树层遍历，nums[i]不能用。


排列问题
 1. 排列问题中，[1,2]与[2,1]是不同的，所以pick过1之后，在下一颗树里还是可以继续pick，需要used数据，用于标记已经选择过的元素。（需要used数组记录path里都放了哪些元素了）
 2. start_index用于控制余量元素，即[1,2,3]选了1以后，控制选2,3和下标。
 3. 因为选过的元素还可以继续选择，所以排列问题中不需要start_index。
 4. 每层for循环都是从0开始，而不是从start_index开始。
 5. 第一个for循环的含义，pick每个元素当一次首元素。

> 因为排列问题，每次都要从头开始搜索，例如元素1在[1,2]中已经使用过了，但是在[2,1]中还要再使用一次1。
>
> 而used数组，其实就是记录此时path里都有哪些元素使用了，一个排列里一个元素只能使用一次。
> 
> 排列问题只要叶子节点，所以到叶子了才res.append。
>
> 


数组 vs. 字符串的回溯

e.g. LC40 vs. LC

剑指offer38同LC47全排列

回溯2个状态：LC89, LC784

##【遍历】模板题

[四周扩散图例](https://www.acwing.com/solution/content/15338/)

DFS遍历模板 LC54, LC79, LC130, LC733

BFS遍历模板 LC200




LC210

- 拓扑排序检查有向图是否有环
- 并查集检查无向图是否有环

邻接表：通过结点的索引，我们能够得到这个结点的后继结点；
入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。






- 未做题

LC51, LC52,  





# BFS

[BFS套路代码](https://leetcode-cn.com/problems/perfect-squares/solution/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/)

1. BFS 算法组成的 3 元素：队列，入队出队的节点，已访问的集合。

   - 队列：先入先出的容器；
   - 节点：最好写成单独的类，比如本例写成 (value,step) 元组。也可写成 (value,visited)，看自己喜好和题目；
   - 已访问集合：为了避免队列中插入重复的值

2. BFS算法组成的套路：

   - 初始化三元素：

   ```python
   Node = node(n) 
   queue = [Node] 
   visited = set([Node.value])
   ```

   - 操作队列 —— 弹出队首节点：
     `vertex = queue.pop(0)`

   - 操作弹出的节点 —— 根据业务生成子节点（一个或多个）：
     `[node(vertex.value - n*n, Node.step+1) for n in range(1,int(vertex.value**.5)+1)]`

   - 判断这些节点 —— 符合业务条件，则return，不符合业务条件，且不在已访问集合，则追加到队尾，并加入已访问集合：

   ```
   if i==0:                   
       return new_vertex.step
   elif i not in visited:
       queue.append(new_vertex)
       visited.add(i) 
   ```

   - 若以上遍历完成仍未return，下面操作返回未找到代码：`return -1`。



> 关于时间复杂度
>
> visited用<u>列表，not in 是线性复杂度O(n)</u>，用set是O(1)。