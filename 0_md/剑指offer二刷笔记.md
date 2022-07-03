剑指offer二刷笔记 

遗留的问题 **https://github.com/michelleweii/Leetcode**

- [ ] 14-1 剪绳子 middle
- [ ] 14-2 剪绳子2 middle
- [ ] 43 1～n 整数中 1 出现的次数 hard
- [ ] 44 数字序列中某一位的数字 middle 找规律
- [ ] 56-2 数组中数字出现的次数 II middle
- [ ] 60 n个骰子的点数 hard dp
- [ ] 62 圆圈中最后剩下的数字 easy 约瑟夫环
- [ ] 65 不用加减乘除做加法 easy 位运算

# 1. 剑指offer目录

## 1【哈希表】

#### 03 数组中重复的数字

```python
def findRepeatNumber(self, nums):
    n = len(nums)
    for i in range(n):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1
```

#### 39 数组中出现次数超过一半的数字

```python
def majorityElement(self, nums):
    if not nums:return nums
    n = len(nums)
    half = n//2
    hash_map = {}
    for x in nums:
        hash_map[x] = hash_map.get(x,0)+1
        if hash_map.get(x,0)>half:
            return x
# 摩尔投票法
def majorityElement1(self, nums):
    cnt = 0
    val = -1
    for x in nums:
        if not cnt:
            val=x
            cnt+=1
        else:
            if x==val:cnt+=1
            else:cnt-=1
    return val
```

#### 50 第一个只出现一次的字符

```python
def firstUniqChar(self, s: str):
    hashmap = {}
    for x in s:
        hashmap[x] = True if x not in hashmap else False
    for x in s:
        if hashmap[x]:return x
    return " "
```

#### 57-1 和为s的两个数字

```python
def twoSum(self, nums, target):
    if not nums:return []
    hashmap = {}
    for x in nums:
        # print(hashmap)
        if hashmap.get(x,0):return [x, hashmap[x]]
        hashmap[target-x] = x
    return []
```



## 2【双指针】/ 【排序】

#### 21 调整数组顺序使奇数在前（反向双指针）

```python
def exchange(self, nums):
    n = len(nums)
    i, j = 0, n-1
    while i<j:
        if i<n and nums[i]%2==1: i+=1
        if j>=0 and nums[j]%2==0: j-=1
        else: nums[i], nums[j] = nums[j], nums[i]
    return nums
```

#### **48 *最长不含重复字符的子字符串（同向双指针）**middle lc3

```python
def lengthOfLongestSubstring(self, s):
    if not s: return 0
    hashmap = {}
    i = 0
    res = -1
    for j in range(len(s)):
        # if s[j] not in hashmap:
        hashmap[s[j]]= hashmap.get(s[j],0)+1
        while i<j and hashmap[s[j]]>1:
            hashmap[s[i]] = hashmap.get(s[i],0)-1
            i += 1
        # print(i, j)
        res = max(res, j-i+1)
    return res
```

#### 40 *[最小的k个数 / 最大的k个数（快速排序，分治的思想）](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

```python
# 这代码是求『前』k个小的数（最小的k个数）。
# “最大的k个数”只用将arr[r]>=pivot的> and < 调换。
class Solution:
    def getLeastNumbers(self, arr, k):
        if k>= len(arr):return arr
        return self.partition(arr, 0, len(arr)-1, k)

    def partition(self, arr, left, right, k):
        if left>=right:return # 如果原地更改的话，就return即可；如果有新的变量接收，就要return一个具体的值
        pivot = arr[left]
        l,r = left,right
        while l<r:
            while l<r and arr[r]>=pivot:r-=1
            arr[l] = arr[r]
            # arr[l], arr[r] = arr[r], arr[l], 这样交换也是对的
            while l<r and arr[l]<=pivot:l+=1
            arr[r] = arr[l]
            # arr[r], arr[l] = arr[l], arr[r], 这样交换也是对的
        arr[l] = pivot
        # return l
        if k<l: self.partition(arr, left, l-1, k)  # 分治
        if k>l: self.partition(arr, l+1, right, k)  # 分治
        # print(arr) # 原地更改[1, 2, 3, 5, 6, 4]
        return arr[:k]

# [3,2,1,5,6,4], 2
# [1,2]
```

#### 40-0 快排模板

```python
def quick_sort(nums, left, right):
    # 当只传来一个元素
    if left>=right:return
    pivot = nums[left]
    i,j = left, right
    while i<j:
        while i<j and nums[j]>=pivot:j-=1 # #从后往前查找，直到找到一个比pivot更小的数
        nums[i] = nums[j] # #将更小的数放入左边
        while i<j and nums[i]<=pivot:i+=1 # #从前往后找，直到找到一个比pivot更大的数
        nums[j] = nums[i] # #将更大的数放入右边
    # 循环结束，i与j相等
    nums[i] = pivot # 待比较数据放入最终位置
    # return i # 回待比较数据最终位置
    quick_sort(nums, left, i-1) # 每次递归结束，右边都比pivot小
    quick_sort(nums, i+1, right) # 左边都比pivot大
    # print(nums) 原地更改
```

#### 40-1 堆排序模板

```python
class Solution:
    def sortArray(self, nums): #List[int]) -> List[int]:
        return self.heapSort(nums)

    # 堆排序
    def heapSort(self, nums):
        n = len(nums)-1
        # 将数组整理成堆（堆有序）
        # 从第一个非叶子节点开始构建初始堆
        # 只需要从 i=(len-1)/2 这个位置开始逐层上移
        for i in range(n//2, -1, -1):
            self.Sift(nums, i, n)
            
        # 进行n-1次循环完成堆排序
        # 循环不变量：区间 [0, i] 堆有序
        for i in range(n, 0, -1):
            # 换出根节点，将其放在最终位置（根节点和最后一个元素交换）
            nums[0], nums[i] = nums[i], nums[0]
            # 在减少了1个元素的无序序列中进行调整（剩余部分调整堆）
            # i-1:逐步减少堆有序的部分
            # 下标 0 位置下沉操作，使得区间 [0, i] 堆有序
            self.Sift(nums, 0, i-1)
        return nums

    def Sift(self, nums, low, high):
        """
        堆排序--建堆（大顶堆，升序）
        :param nums:
        :param low: 当前下沉元素的下标
        :param high: [0, high] 是 nums 的有效部分
        :return:
        """
        i = low
        j = 2*i + 1
        # temp存储父节点
        # temp = nums[i]
        # 与孩子节点做比较，建堆
        while (j <= high):
            # 找到最大的那个孩子
            if (j < high and nums[j] < nums[j + 1]):
                j += 1
            # 父亲和孩子交换
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                # 继续向下调整
                i = j
                j = 2*i + 1
            else:
                break
```

#### 51 [数组中的逆序对（归并排序）](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)

> 如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
>
> `nums=[7,5,6,4]`，共5个，即（7,5）、（7,6）、（7,4）、（5,4）、（6,4）。

```python
def reversePairs(self, nums):
    #self.res = 0
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
            res += mid-i+1 # 为什么是这样的？
            # “左子数组当前元素 > 右子数组当前元素” 时，意味着 「左子数组当前元素 至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」 。
            # 「左子数组当前元素 至 末尾元素」是递增的
    temp += nums[i:mid + 1]
    temp += nums[j:r + 1]

    # 把临时数组的元素再放回去，实现原地更改
    for k in range(r-l+1):
        nums[l+k] = temp[k]
    # k = l
    # for x in temp:
    #     nums[k] = x
    #     k+=1
    # print("temp", temp)
    # temp [5, 7]
	# temp [4, 6]
	# temp [4, 5, 6, 7]
    return res
```

#### 51-0 归并排序模板（递归）

```python
# [l, mid] + [mid+1, r]
def merge_sort2(nums, l, r):
    if l>=r: return
    mid = (l+r)//2
    merge_sort2(nums, l, mid)
    merge_sort2(nums, mid+1, r)
    left_p, right_p = l, mid+1
    res = [] # 临时数组，用于保存局部排序好的结果
    while left_p <= mid and right_p <= r:
        if nums[left_p]<nums[right_p]:
            res.append(nums[left_p])
            left_p += 1
        else:
            res.append(nums[right_p])
            right_p += 1
    res += nums[left_p:mid+1]
    res += nums[right_p:r+1]
    
    # 把临时数组里的元素再放回去，当前归并的区间
    for k in range(r-l+1):
        nums[l+k] = res[k]
    # print("nums", nums)
    # print("res", res)
    # print('-'*20)
    return nums # nums已经实现原地更改
```

#### 57-2 [和为s的连续正数序列(同向双指针)](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

```python
def findContinuousSequence(self, target):
    j = 1 # right 右端点
    s = 1 # 序列和
    res = []
    for i in range(1, target):
        # 当i固定时，right最远的点
        while s<target:
            j+=1
            s+=j
        # print(i,j, s)
        if s==target and j-i+1>1:
            path = []
            for k in range(i, j+1):
                path.append(k)
            res.append(path[:])
        s -= i
    return res
```



## 3【二分】

#### 二分模板

mid 在左边，当我们将区间 [l, r] 划分成 `[l, mid]` 和 `[mid + 1, r]` 时，其更新操作是 `r = mid` 或者 `l = mid + 1` ; 计算mid时不需要加1。

```c++
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }
    return l;
}
```

mid 在右边，当我们将区间 [l, r] 划分成 `[l, mid - 1]` 和` [mid, r]` 时，其更新操作是 `r = mid - 1` 或者 `l = mid` ; 此时为了防止死循环，计算mid时需要加1。

```c++
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
```

如何判定check()函数？都以`if`的视角。

```python
假设有一个总区间[right, left]，经由我们的 check 函数判断后，可分成两部分，
这边以o作 true，.....作 false 示意较好识别

如果我们的目标是下面这个v，那么就必须使用模板 1（r = mid）

..........vooooooooo    (False v True, v属于True那边, l = mid, 目标在右边, 向True靠近)

假设经由 check 划分后，整个区间的属性与目标v如下，则我们必须使用模板（l = mid + 1）

oooooooov........  (True v False, v属于True那边, l = mid + 1,目标在左边,向True靠近)

所以下次可以观察 check 属性再与模板1 or 2 互相搭配就不会写错啦
```

#### 04 [二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

```python
def findNumberIn2DArray(self, matrix, target):
    if not matrix or not matrix[0]:return False
    n = len(matrix) # n行
    m = len(matrix[0]) # m列
    i = 0
    j = m-1
    while i<n and j>=0:
        if matrix[i][j]==target:return True
        elif matrix[i][j]>target:j-=1
        else: i+=1
    return False
```

#### 11 *[旋转数组的最小值 OR 旋转数组的最大值](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

```python
# 输入：[3,4,5,1,2]
# 输出：1
def minArray(self, numbers):
    # numbers是原本是递增的
    n = len(numbers)-1
    while(n>0 and numbers[n]==numbers[0]): n-=1
    # 最后比第一个值大，则一定递增
    if numbers[n] >= numbers[0]:return numbers[0]
    l, r = 0, n
    while(l<r):
        mid = (l+r)//2
        if numbers[mid]<numbers[0]: r=mid
        else:
            l = mid+1
    return numbers[l]
```

#### 53 *[在排序数组中查找数字](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

```python
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
def search_hash(self, nums, target):
    if not nums:return 0
    hashmap = {}
    for x in nums:
        hashmap[x] = hashmap.get(x,0)+1
    return hashmap.get(target,0)

def search(self, nums, target):
    if not nums:return 0
    # 二分出左边界
    l,r = 0,len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[mid]<target:l=mid+1
        else: r = mid
    if nums[l] != target:return 0 # 重要!
    start = l

    l, r = 0, len(nums) - 1
    while l<r:
        mid = (l+r+1)//2
        if nums[mid]>target:r=mid-1
        else: l=mid
    if nums[l] != target:return 0 # 重要！
    end = l
    # print(start,end)
    return end-start+1
```

#### 53-2 [0~n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/)

```python
# 输入: [0,1,3]
# 输出: 2
def missingNumber1(self, nums):
    n = len(nums)+1
    s = (0+n)*(n-1)//2 # 求和
    for x in nums:
        s -= x
    return s

def missingNumber(self, nums):
    l,r = 0,len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[mid]==mid:l=mid+1
        else:r=mid
    return l

# 根据mid在左边、还是在右边，划分出模板1和模板的差别。
# 
```

## 4【链表】

> 特别声明：凡是可能将头节点删除的，都需要建立虚拟节点dummy。
> **删除重复节点 2个指针（dummy、p、q）**
>
> - p：重复节点前的第一个位置。p.next=q
> - q：不重复节点的第一个位置。
>
> **翻转链表 3个指针（prev、cur、tail）**
>
> - cur：当前操作节点。
> - prev：一开始为空，因为链表尾部为空，cur的上一个节点。
> - tail：cur节点的下一位，防止丢失。
>
> **删除链表 1个指针（p = dummy）**

#### 06 从尾到头打印链表 easy

```python
def reversePrint(self, head: ListNode) -> List[int]:
	res = []
  	while head:
     	res.append(head.val)
     	head = head.next
  	return res[::-1]
```

#### 18 [删除链表的节点 easy](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

```python
def deleteNode(self, head: ListNode, val: int) -> ListNode:
    if not head:return head
    dummy = ListNode(-1)
    dummy.next = head
    p = dummy
    while p.next:
        if p.next.val == val:
            p.next = p.next.next
            return dummy.next
        p = p.next
    return dummy.next
```

#### 22 [链表中倒数第k个节点 easy](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

```python
# 一次遍历解决问题
def removeNthFromEnd(self, head, n):
    if not head:return head
    dummy = ListNode(0)
    dummy.next = head
    p1 = p2 = dummy
    for i in range(n):
        p2 = p2.next # 后一个指针
        # print(i, p2.val) # 1 2
    while p2.next: # 停在最后一个节点
            p1 = p1.next # 前一个指针
            p2 = p2.next
    p1.next = p1.next.next
    return dummy.next

# 遍历两次
def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    p = head
    lens = 0
    while p:
        lens += 1
        p = p.next

    n = lens - k + 1
    p = head
    for i in range(1, n):
        p = p.next
    return p
```

#### **24 *反转链表** easy

```python
def reverseList(self, head):
    if not head or not head.next: return head
    # 反转链表需要3个节点
    prev = None
    cur = head
    while cur:
        tail = cur.next
        cur.next = prev
        prev = cur
        cur = tail
    # self.print_link(prev)
    return prev
```

#### 25 合并两个排序链表 easy

```python
def mergeTwoLists(self, l1, l2):
    head = ListNode(-1)
    p = head
    p1 = l1
    p2 = l2
    while p1 and p2:
        if p1.val <= p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next

    if p1:
        p.next = p1
    elif p2:
        p.next = p2

    self.printList(head.next)
    return head.next
```

#### 35 复杂链表的复制 middle

```python
def copyRandomList(self, head):
    if not head: return head
    cur = head
    # 1. 复制各节点，并构建拼接链表
    while cur:
        fake = Node(cur.val)
        fake.next = cur.next
        cur.next = fake
        cur = fake.next
        # 成z字

    # 2. 构建各新节点的 random 指向
    p = head
    while p:
        # 注意这里有random节点才改变
        if p.random:
            p.next.random = p.random.next
        p = p.next.next

    # 3. 拆分两链表
    pre = head # 指向旧链表
    cur = head.next # 指向新链表
    res = head.next # 指向新链表
    while cur.next:
        pre.next = pre.next.next # 删除旧与新的连接
        cur.next = cur.next.next
        pre = pre.next
        cur = cur.next
    # pre.next = None  # 单独处理原链表尾节点
    return res
```

#### 52 [两个链表的第一个公共节点 easy](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    pa, pb = headA, headB
    while pa!=pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa
```



## 5【树】

#### 07 重建二叉树

```python
class Solution:
    def __init__(self):
        self.hash_map = {}

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        # 快速在中序遍历中，找到某个值的下标
        for i, val in enumerate(inorder):
            self.hash_map[val] = i
        return self.dfs(0, len(preorder)-1, 0, len(inorder)-1)

    def dfs(self, pl, pr, il, ir):
        if pl>pr:return None # dfs一定要有循环的出口
        root = TreeNode(self.preorder[pl])
        k = self.hash_map[self.preorder[pl]]
        # 去前序遍历中找左子树，去中序遍历中找左子树
        root.left = self.dfs(pl+1, pl+k-il, il, k-1)
        # 去前序遍历中找右子树，去中序遍历中找右子树
        root.right = self.dfs(pl+k-il+1, pr,k+1, ir)
        return root
```

#### 26 [树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)

```python
class Solution(object):
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 空树不是任意一个树的子结构
        if not A or not B: return False
        if self.is_part(A, B): return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def is_part(self, p1, p2):
        if not p2: return True
        if not p1: return False
        if p1.val != p2.val: return False
        return self.is_part(p1.left, p2.left) and self.is_part(p1.right, p2.right)
```

#### 27 [二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)

```python
# 构建二叉树的镜像
class Solution(object):
    # 递归
    def mirrorTree(self, root):
        if not root: return root
        root.right = self.mirrorTree(root.right)
        root.left = self.mirrorTree(root.left)
        root.right, root.left = root.left, root.right
        return root

    # 遍历
    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if not root: return root
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root
```

#### 28 [对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)

```python
class Solution:
    def isSymmetric(self, root):
        # 如果是空树，则是对称二叉树
        if not root:return True
        return self.dfs(root.left, root.right)

    def dfs(self, p, q):
        # 如果有一边为空，则返回结果
        if not p or not q:
            return not p and not q
        if p.val != q.val: return False
        return self.dfs(p.left, q.right) and self.dfs(p.right, q.left)
```

#### **32-1 从上到下打印二叉树**

#### **32-3 *z字从上到下打印二叉树**

```python
class Solution(object):
    # [3,9,20,15,7]
    def levelOrder1(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            tmp = queue.pop(0)
            res.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return res

    # 每层单独保存，层次遍历
    # [[3], [9,20], [15,7]]
    def levelOrder2(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(cur_level[:])
        return res

    # 之字形遍历
    # [[3], [20,9], [15,7]]
    def levelOrder3(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        flag = 1
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(cur_level[::flag])
            flag *= -1
        return res
```

#### 33 [二叉搜索树后续遍历](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

```python
class Solution:
    # RecursionError: maximum recursion depth exceeded.
    # python的递归深度是有限制的，默认为1000
    def verifyPostorder1(self, postorder):
        self.postorder = postorder
        return self.dfs(0, len(postorder) - 1)

    def dfs(self, l, r):
        # 定义dfs的出口
        if l >= r: return True
        root = self.postorder[r] # 左右根
        k = l
        while k < r and self.postorder[k] < root: k += 1 # 找到第一个比根节点大的元素，即为右子树
        mid = k # m右子树开始点
        while self.postorder[k] > root: k += 1 # 遍历右子树是否满足性质，左子树因为找mid的时候自然成立
        return k == r and self.dfs(l, mid - 1) and self.dfs(mid, r - 1)
      # self.dfs(l, mid - 1) 递归左子树
      # self.dfs(mid, r - 1) 递归右子树
        
### 方法2
    def verifyPostorder(self, postorder):
        def dfs(l, r):
            if l >= r: return True
            k = l
            while postorder[k] < postorder[r]: k += 1
            m = k
            while postorder[k] > postorder[r]: k += 1
            return k == r and dfs(l, m - 1) and dfs(m, r - 1)

        return dfs(0, len(postorder) - 1)
```

#### 34 [二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

```python
# 清晰版
class Solution:
    def __init__(self):
        self.res, self.path = [],[]

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:return []
        self.path.append(root.val)
        self.dfs(root, target-root.val)
        return self.res

    def dfs(self, root, target):
        # 定义dfs出口
        if not root: return
        # self.path.append(root.val) 
        # target -= root.val # 这里没有办法回溯到，错误
        # 一定要是叶子节点，才算走到了末尾。并且target为0
        if not root.left and not root.right and target==0:
            self.res.append(self.path[:])

        if root.left: 
            self.path.append(root.left.val)   
            self.dfs(root.left, target-root.left.val)
            self.path.pop()

        if root.right:
            self.path.append(root.right.val)   
            self.dfs(root.right, target-root.right.val)
            self.path.pop()

# 简约版
# 注意path.pop()的位置
class Solution:
    def pathSum(self, root: TreeNode, target):
        res = []
        if not root:return res
        self.dfs(res, [], root, target)
        return res

    def dfs(self, res, path, root, target):
        # 定义dfs出口
        if not root: return
        path.append(root.val)
        target -= root.val
        # 一定要是叶子节点，才算走到了末尾。并且target为0
        if not root.left and not root.right and target==0:
            res.append(path[:])
        self.dfs(res, path, root.left, target)
        self.dfs(res, path, root.right, target)
        # 1_回溯算法
        path.pop()
```

#### 36 [二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)

> 中序遍历两个节点，一个pre，一个cur。cur执行真正的中序遍历逻辑，代码都不用改。每遍历到一个节点，将pre 和 cur 按照双向链表互联。pre和cur走一步。 最后将头结点(dummy.right)和尾节点(pre)连在一起。

```python
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
# 这个题不太会
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head # right、left可以修改的
        return self.head

    def dfs(self, cur):
        if not cur: return
        self.dfs(cur.left)  # 递归左子树
        if self.pre:  # 修改节点引用
            self.pre.right, cur.left = cur, self.pre # right、left可以修改的
        else:  # 记录头节点
            self.head = cur
        self.pre = cur  # 保存 cur
        self.dfs(cur.right)  # 递归右子树
```

#### 37 [序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)

```python
# LC297
# DFS
class Codec:
    # 选择前序遍历，是因为 根|左|右根∣左∣右 的打印顺序，在反序列化时更容易定位出根节点的值。
    # 遇到 null 节点也要翻译成特定符号，反序列化时才知道这里是 null
    def serialize(self, root):
        if not root: return 'x' # 遍历到 null 节点
        left = self.serialize(root.left)
        right  = self.serialize(root.right)
        return str(root.val)+','+str(left)+','+str(right) # 按  根,左,右  拼接字符串
        # 看图,前序遍历序列化 1,2,x,x,3,4,x,x,5,x,x

    def deserialize(self, data):
        nodelist = data.split(',')
        return self.build_tree(nodelist)

    def build_tree(self, data):
        root = data.pop(0)

        if root=='x': # 是X，返回null节点
            return None

        root = TreeNode(root)
        root.left = self.build_tree(data)
        root.right = self.build_tree(data)
        return root

# 层次遍历
class Codec:
    # 1,2,3,#,#,4,5
    def serialize(self, root): # 将树转为list(层次遍历)
        if not root:return "#"
        queue = [root]
        ans = []
        while queue:
            node = queue.pop(0)
            if not node:
                ans.append('#')
            else:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while ans and ans[-1] == '#':
            ans.pop()
        return ','.join(ans)

    def deserialize(self, data): # 还原树
        root_nums = data.split(',')
        if not root_nums or root_nums[0]=='#' or root_nums[0]=='':
            return None
        root = TreeNode(int(root_nums.pop(0)))
        is_left = True # 当前节点该连左子树or右子树
        cur_node = root # 当前节点
        tree_node = [] # 已经连接的节点，为了找到下一个最左节点
        while root_nums:
            num = root_nums.pop(0)
            if is_left:
                is_left = False
                if num != '#':
                    cur_node.left = TreeNode(int(num))
                    tree_node.append(cur_node.left)
            # 开始右节点
            else:
                is_left = True
                if num != '#':
                    cur_node.right = TreeNode(int(num))
                    tree_node.append(cur_node.right)
                cur_node = tree_node.pop(0)
        return root
```

#### 54 [二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

```python
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        self.k = k
        self.dfs(root)
        return self.res
    # 注意这里 k 需要是全局变量。
    #def dfs(self, root):
        #if not root:return
        # 右根左遍历
        #self.dfs(root.right)
        #if self.k==0:return
        #self.k-=1
        #if self.k==0:self.res=root.val
        #self.dfs(root.left)
        
    def dfs2022(self, root):
        if not root:return
        # 右根左遍历
        if root.right and self.k: self.dfs(root.right)
        # if self.k==0:return
        self.k -= 1
        if self.k==0:
            self.res=root.val # 注意这里res要赋值，不能直接return root
            # 但是，为什么这里不能直接return root.val呢？
            return
        if root.left and self.k: self.dfs(root.left)
```

#### 55-1 [二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)

```python
def maxDepth(self, root: TreeNode) -> int:
    if not root:return 0
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return max(left, right)+1
```

#### 55-2 [平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/)

```python
# LC110
class Solution:
    # 从下至上O(N)
    # 思路是对二叉树做先序遍历，从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isAvl(root) != -1
    def isAvl(self, root):
        if not root: return 0
        left = self.isAvl(root.left) # 左
        if left == -1: return -1
        right = self.isAvl(root.right) # 右
        if right == -1: return -1
        # 以当前节点为根节点的树的最大高度
        return max(left, right) + 1 if abs(left - right) < 2 else -1 # 根
  
  
  	# 从上到下nlogn
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    # 计算每个节点的深度
    def depth(self, root):
        # 定义dfs的出口
        if not root:return 0
        right = self.depth(root.right)
        left = self.depth(root.left)
        return max(right, left)+1
```

#### 68-1 [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root:return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
```

#### 68-2 *[二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return root
        if root==p or root==q:return root
        # 先序遍历
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:return root # 从底至顶回溯，当节点 p, q 在节点 root 的异侧时，节点 root 即为最近公共祖先，则向上返回 root 
        if left: return left
        return right
```



## 6【dp动态规划】

#### 10 斐波那契数列

```python
# 求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）
def fib(self, n):
    if n==0:return 0
    if n==1:return 1
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2])% 1000000007
    return dp[n]
```

#### 10 青蛙跳台阶问题

```python
def numWays(self, n: int):
    if n==0:return 1
    if n==1:return 1
    dp = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%1000000007
    return dp[n]
```

#### [14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)

```python
"""
middle 2022-05-03 一维动态规划
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/jian-zhi-offer-14-i-jian-sheng-zi-dong-t-c7ou/
解题思路
设数组dp记录0 ~ n 剪绳子的最大乘积
两层遍历：第一层i表示绳子的长度; 第二层j用来表示第一段减去的长度。要想求最大值，有两种情况：
- 剪绳子：剪绳子的话乘积就是 j * dp[i - j]， 减去第一段的长度 * 剩下长度的最大值【剩下(i - j)长度可以剪也可以不剪，剪】
        剪第一段，第二段不剪，直接 j * (i - j ) 当前的长度 * 剩下的长度【剩下(i - j)长度可以剪也可以不剪，不剪)】
- 不剪 dp[i]

状态定义：dp[i]表示长度为i的绳子剪成m段后的最大乘积。初始化dp[2] = 1。
第一段长度j可以取的区间为[2,i)。

因为剪1段对乘积无帮助，1*（n-1）还变小了。
"""
class Solution:
    def cuttingRope(self, n: int):# -> int:
        dp=[0]*(n+1) # 数组dp记录0~n 剪绳子的最大乘积
        dp[2]=1
        for i in range(3,n+1): # 遍历绳子的长度i
            for j in range(1,i//2+1): # 剪去的长度j
                dp[i]=max(dp[i], max(j*(i-j), j*dp[i-j]))

        return dp[n]
```

#### 19 正则表达式匹配

```python
def isMatch(self, s: str, p: str):
    n = len(s)
    m = len(p)
    dp = [[False for _ in range(m+1)] for _ in range(n+1)] # n行m列
    dp[0][0] = True # 空串和空模式串是匹配的， 空模式串和任意的
    for i in range(n+1):
        for j in range(m+1):
            if j == 0:
                dp[i][j] = i == 0
            else:
            # 非空正则分为两种情况 * 和 非*
                if p[j-1] != '*':
                    if i>0 and ((s[i-1]==p[j-1]) or p[j-1]=='.'):
                        dp[i][j] = dp[i-1][j-1]
                else:
                    # 不看
                    if j>=2:
                        dp[i][j] |= dp[i][j-2]
                    # 看
                    if i>=1 and j>=2 and ((s[i-1] == p[j-2]) or p[j-2]=='.'):
                        dp[i][j] |= dp[i-1][j]
    # print(dp)
    return dp[-1][-1]
```

#### 42 *[连续子数组最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

```python
class Solution:
    # dp[i] 以i结尾的连续子数组的最大和
    # 以某个数作为结尾，意思就是这个数一定会加上去，那么要看的就是这个数前面的部分要不要加上去。大于零就加，小于零就舍弃。
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        # print(max(dp))
        return max(dp)
```

#### 46 [把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

```python
# 状态定义：设动态规划列表dp，dp[i] 代表以 nums[x_i-1] 为结尾的数字的翻译方案数量。
class Solution:
    def translateNum(self, num):
        s = str(num)
        dp = [0 for _ in range(len(s)+1)]
        # print(len(s)) # 5
        # print(len(dp)) # 6
        dp[0] = 1 #
        dp[1] = 1 # 第 1 位数字,nums[0] 的翻译方法数量为 1
        for i in range(2, len(dp)):
            tmp = s[i-2:i]
            if int(tmp)<=25 and int(tmp)>=10:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        # print("dp", dp)
        return dp[len(s)]
```

#### 47 [礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)

```python
# 设 dp(i,j) 为从棋盘左上角走至单元格 (i,j) 的礼物最大累计价值
class Solution:
    def maxValue(self, grid):
        if not grid and not grid[0]:return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 初始化
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
```

#### 49 [丑数]()

```python
# dp[i] 代表第 i+1 个丑数
class Solution:
    def nthUglyNumber(self, n):
        dp = [1]*n
        a,b,c = 0,0,0
        for i in range(1,n):
            n2,n3,n5 = dp[a]*2,dp[b]*3,dp[c]*5
            dp[i] = min(n2,n3,n5)
            if dp[i]==n2:a+=1
            if dp[i]==n3:b+=1
            if dp[i]==n5:c+=1
        return dp[-1]
```

#### ~~60 n个骰子的点数 dp~~

#### 63 [股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)

```python
# dp[i] 为 第i天卖出的最大利润
# 扩展可以交易两次（买卖算一次交易）求最大值
class Solution:
    def maxProfit(self, prices):
        # 在价格最低的时候买入，差价最大的时候卖出
        if len(prices) < 2: return 0
        cost = prices[0] # 每日更新最低价格
        profit = 0 # 首日利润为0
        for price in prices:
            cost = min(cost, price) # 找到最低那天的价格
            profit = max(profit, price-cost)
        return profit
      
        #if not prices:return 0
        #dp = [0 for _ in range(len(prices))]
        #cost = prices[0]
        #for i in range(1, len(prices)):
        #    cost = min(cost, prices[i])
        #    dp[i] = max(dp[i-1], prices[i]-min(cost, prices[i]))
        #return max(dp)
```



## 7【栈 & 队列】

#### 09 [用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

```python
class CQueue:
    def __init__(self):
        self.stk1 = [] # 进栈
        self.stk2 = [] # 出栈

    # 队列尾部插入整数
    def appendTail(self, value):
        self.stk1.append(value)

    # 在队列头部删除整数
    def deleteHead(self):
        if self.stk2: return self.stk2.pop()
        if not self.stk1: return -1
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        return self.stk2.pop()
```

#### 30 [包含min函数的栈(单调栈)](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)

```python
# 单调递减栈
# LC155
class MinStack:
    def __init__(self):
        self.stk, self.min_stk = [], []

    # 注意这里，=也要包含进去
    def push(self, x: int) -> None:
        self.stk.append(x)
        # if not self.min_stk: self.min_stk.append(x)
        # else:
        #     if x<self.min_stk[-1]:
        #         self.min_stk.append(x)
        if not self.min_stk or self.min_stk[-1] >= x:
            self.min_stk.append(x)

    def pop(self) -> None:
        if self.stk.pop() == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def min(self) -> int:
        return self.min_stk[-1]
```

#### 31 [栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

```python
# 判断一个序列是否为合法的栈弹出序列
# 思路：每次入栈stk一个元素，判断入栈的元素是否和出栈元素相同，如果相同stk就出栈；
# 并将 出栈序列popped 的指针右移
# 最终判断stk是否为空
# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/mian-shi-ti-31-zhan-de-ya-ru-dan-chu-xu-lie-mo-n-2/
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stk = []
        i = 0 # 标记popped顺序
        for x in pushed:
            stk.append(x)
            while stk and stk[-1]==popped[i]:
                stk.pop()
                i += 1
        return not stk
```

#### 59 *[滑动窗口最大值（单调递减栈） LC239](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)

```python
# 单调递减栈
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:return []
        stk = []
        res = []
        for i in range(len(nums)):
            # 比当前元素小的数据都干掉
            while stk and nums[i]>nums[stk[-1]]:
                stk.pop()
			
            stk.append(i)
            
            # # 超过窗口范围，队首元素出队
            while stk and i-k>=stk[0]:
                stk.pop(0)

          	# 满足窗口大小，开始res开始加结果。
            # print(i, stk)
            if i+1>=k:
                res.append(nums[stk[0]])
        return res
```

#### 59-2 [队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)

```python
class MaxQueue:
    def __init__(self):
        self.q = []
        self.max_q = []

    def max_value(self) -> int:
        if not self.max_q:return -1
        return self.max_q[0]
    # return self.max_q.pop(0) 这样就探弹出去了

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.max_q and value>self.max_q[-1]: # 单调递减
            self.max_q.pop() # 注意这里是左边
        self.max_q.append(value)

    def pop_front(self) -> int:
        if not self.q:return -1
        tmp = self.q.pop(0)
        if self.max_q and tmp==self.max_q[0]:
            self.max_q.pop(0)
        return tmp
```



## 8【DFS & BFS】

> bfs是存在所有可行解。
> dfs是有没有True or False，回溯是一种dfs。
>
> bfs每个点只能访问一次，求所有解集，需要维护visited数据（判重数据）。
> bfs要维护队列。
>
> [四周扩散方向](https://blog.csdn.net/weixin_31866177/article/details/88760781)，以`matrix[0][0]`为原点，螺旋矩阵的走向记忆四周扩散方向。

#### 12 *[矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)

**dfs 存不存在某一个值**

```python
class Solution:
    def exist(self, board, word):
        if not board or not board[0]:return False
        if not word: return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(word, board, 0, i, j):return True
        return False

    def dfs(self, word, board, u, x, y):
        """
        :param word: 原始target单词
        :param board: 原始matrix数组
        :param u: 定位target，下标
        :param i: 定位matrix，下标
        :param j: 定位matrix，下标
        :return:
        """
        if board[x][y] != word[u]: return False
        if len(word)-1 == u: return True
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        tmp = board[x][y]
        board[x][y] = '*' # 防止重复标记。abcc，c如果又判断了一次自己，也会使得条件成立。
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if a>=0 and a<len(board) and b>=0 and b<len(board[0]):
                if self.dfs(word, board, u+1, a, b):return True
        board[x][y] = tmp
        return False
```

#### 13 *[机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

**bfs 所有可行解**

```python
class Solution:
    def get_sum(self, n):
        s = 0
        while n:
            s += n%10
            n //= 10
        return s

    def movingCount(self, m, n, k):
        if not m and not n: return 0
        res = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = []
        queue.append((0, 0))
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        while queue:
            tmp = queue.pop(0)
            if self.get_sum(tmp[0])+self.get_sum(tmp[1])>k or visited[tmp[0]][tmp[1]]:continue
            res += 1
            visited[tmp[0]][tmp[1]] = True
            for i in range(4):
                a = tmp[0]+dx[i]
                b = tmp[1]+dy[i]
                if a>=0 and a<m and b>=0 and b<n and not visited[a][b]:
                    queue.append((a,b))
        return res
```

#### 29 [顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

```python
# 螺旋矩阵
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return matrix
        m, n = len(matrix), len(matrix[0])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        x,y,d = 0,0,0
        res = []
        visited = [[False]*n for _ in range(m)]
        for i in range(n*m):
            res.append(matrix[x][y])
            visited[x][y] = True
            a = x+dx[d]
            b = y+dy[d]
            # 这个方向走不通了，开始换方向
            if a<0 or a>=m or b<0 or b>=n or visited[a][b]: 
                d = (d+1)%4
                a = x+dx[d]
                b = y+dy[d]
                    
            x,y = a,b
        return res
```

#### 38 *[字符串的排列 dfs回溯](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/dai-ma-sui-xiang-lu-jian-zhi-offer-38-zi-gwt6/)

```python
# LC47
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
## 考虑不通过set()实现去重
# "aab"，["aab","aba","aab","aba","baa","baa"]， ac: ["aba","aab","baa"]
# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/dai-ma-sui-xiang-lu-jian-zhi-offer-38-zi-gwt6/
# 强调的是去重一定要对元素经行排序，这样我们才方便通过相邻的节点来判断是否重复使用
class Solution:
    ######### 模板解法start ########
    def muban(self,s):
        self.res, self.path = [], []
        if not s:return self.res
        s = [x for x in s] # s = list(s)
        s.sort() # nlogn
        used = [0]*len(s)
        self.muban_dfs(s, used)
        return self.res

    def muban_dfs(self, s, used):
        if len(self.path)==len(s):
            self.res.append(''.join(self.path[:]))

        for i in range(len(s)):
            if i>0 and s[i-1]==s[i] and used[i-1]==0: continue # 树层上已经选过该字母充当首字母
            if used[i]==1: continue # 当前这个位置已经选过了
            # 如果同⼀树⽀nums[i]没使⽤过开始处理
            used[i]=1 # # 标记已访问过
            self.path.append(s[i])
            self.muban_dfs(s, used)
            used[i]=0
            self.path.pop()

# 通过set()去重O(1)，次优解法
class Solution:
    # ['acb', 'bca', 'cba', 'abc', 'bac', 'cab']
    def permutation(self, s: str):
        res = []
        if not s: return res
        self.dfs("", res, s)
        return list(set(res)) # 通过set去重

    def dfs(self, path, res, s):
        # 定义dfs出口
        if s == '': res.append(path)
        # 轮流当首字母
        for i in range(len(s)):
            self.dfs(path + s[i], res, s[:i] + s[i + 1:])
        return res
```



## 9【位运算】

> [性质1](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/)
>
> 根据 与运算 定义，设二进制数字 n，则有：
> 若 n \& 1 = 0，则 n 二进制 最右一位 为 0 （偶数）；
> 若 n \& 1 = 1 ，则 n 二进制 最右一位 为 1 （奇数）。
>
> []()

#### 15 [二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1 # 判断最右一位是否是1
            n >>= 1 # 最右位判断完了，删掉
        return res

    def hammingWeight(self, n):
        res = 0
        for i in range(32):
            res += n&1
            n = n>>1 # # n//=2
        return res
```

#### 16 [数值的整数次方（快速幂）](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/)

> 求x^n 等价于 求 (x^2)^(n//2)。

```python
# 快速幂O(logn)，快速幂实际上是二分思想的一种应用。
# 计算x的n次幂
def myPow_better(self, x: float, n: int) -> float:
    if x == 0: return 0
    res = 1
    if n < 0: x, n = 1 / x, -n
    while n:
        if n & 1: # n%2==1 # 如果n是奇数
            res *= x
        x *= x  # x=x^2
        n >>= 1 # n//=2
    return res

# # 一般乘法O(N)
def myPow(self, x: float, n: int) -> float:
    res = 1
    for i in range(1, abs(n)+1):
        res *= x
    if n < 0: # 注意是负数的时候
        res = 1 / res
    return res
```

#### 56-1 数组中数字出现的次数2次

```python
def singleNumbers(self, nums):
    n = 0
    for num in nums:         # 1. 遍历异或
        n ^= num
    # print(n) # 7
    # 获取x^y的首位1出现的位置
    # x 和 y 的此m二进制位一定不同
    m = 1 # 现在不同的位置是右边第一位
    while n&m ==0:           # 2. 循环左移，计算 m
        m <<= 1
    x,y=0,0
    for num in nums:          # 3. 遍历 nums 分组
        if num & m: x ^= num  # 4. 当 num & m != 0
        else: y ^= num        # 4. 当 num & m == 0
    return [x,y]
```

#### 56-2 数组中数字出现的次数3次

```python

```

#### 65 [不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)

> 利用异或、与运算。[好难python version](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/)   [nananan清晰讲解](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/jin-zhi-tao-wa-ru-he-yong-wei-yun-suan-wan-cheng-j/)

```python
# 思路：
# ^ 异或 ----相当于 无进位的求和
# & 与 ----相当于求每位的进位数
# 公式就是：（a^b) ^ ((a&b)<<1) 即：每次无进位求 + 每次得到的进位数
# 我们需要不断重复这个过程，直到进位数为0为止；
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff # -1
        a = a & x  # 获取负数的补码
        b = b & x
        while b != 0:
          # 【注意】：交换的先后顺序重要
            #a = (a ^ b) 
            #b = (a & b) << 1 & x
          #   int tempSum = a^b;
          #   int carrySum = (a&b)<<1;
          #   a = tempSum;
          #   b = carrySum;
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
#  ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变
#  若补码 a 为负数，需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。
```



## 10【其他】

#### 66 [构建乘积数组（模拟题）](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

```python
## 美团考
"""
思路：双向遍历
原数组：       [1       2       3       4]
左部分的乘积：   1       1      1*2    1*2*3
右部分的乘积： 2*3*4    3*4      4      1
结果：        1*2*3*4  1*3*4   1*2*4  1*2*3*1
----------------------------------------------------------------
当前位置的结果就是它左部分的乘积再乘以它右部分的乘积。因此需要进行两次遍历，第一次遍历用于求左部分的乘积，
第二次遍历在求右部分的乘积的同时，再将最后的计算结果一起求出来。
"""
def constructArr(self, a):
    if not a:return a
    p = 1
    b = [1 for _ in range(len(a))]
    # 计算当前元素左部分乘积
    for i in range(len(a)):
        b[i] = p
        p *= a[i]
    # print(b)
    p = 1
    # 计算当前元素右部分乘积
    for j in range(len(a)-1, -1, -1):
        # print(j)
        b[j] *= p
        p *= a[j]
    # print(b)
    return b
```

#### 45 [把数组排成最小的数（内置排序函数）](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

> 比较函数的定义是，传入两个待比较的元素 x, y，
>
> 如果 x 应该排在 y 的前面，返回 -1，
>
> 如果 x 应该排在 y 的后面，返回 1。
>
> 如果 x 和 y 相等，返回 0。

```python
# 字节题库
# 数字转字符串，字符串字典序排序
import functools
class Solution:
    """
    若拼接字符串 x+y>y+x ，则 x “大于” y ；
    反之，若 x+y<y+x ，则 x “小于” y ；
    比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
    """
    def sort_rule(self,x,y):
        a, b = x+y, y+x
        if a>b: return 1 # 如果 a 应该排在 b 的后面，返回 1。
        elif a<b:return -1
        else:
            return 0

    def minNumber(self, nums):
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(self.sort_rule))
        return ''.join(strs)
```

#### [14- II. 剪绳子 II](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/)（贪心）

> 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

因为要取模，不能用dp。

[题解](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/jian-zhi-offer-14-ii-jian-sheng-zi-iihua-r5op/)

[贪心证明](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/)



~~17 打印从1到最大的n位数（大数问题 模拟题）~~

20 表示数值的字符串（模拟题）

67 把字符串转成整数（模拟题）

41 数据流中的中位数 （堆）

43 1~n整数中1出现的次数hard（数位dp，递归，数学模拟）

44 数字序列中某一位的数字（找规律）

61 扑克牌中的顺子（）

62 圆圈中最后剩下的数字（约瑟夫环）

64 求1+2..+n（逻辑and or）

# 2. 记录

【2021-07-13】(看笔记之后做题，仍有问题) 3 10 11 

剑指 Offer 03 [数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof)

关于数值交换，踩坑 [交换列表中的两个值遇到的坑](https://blog.csdn.net/weixin_39544046/article/details/105972357)

剑指 Offer 11 [旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

剑指 Offer 10- II [青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

**由于 Python 中整形数字的大小限制 取决计算机的内存 （可理解为无限大），因此可不考虑大数越界问题。**

----

【2021-07-14 ~ 2021-07-15】
- 剑指 Offer 16 [数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/)

- 13 bfs 所有可行解

考察快速幂的概念

20 模拟题（不用二刷了）

[位运算相关题目](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/gong-shui-san-xie-yi-ti-si-jie-wei-shu-j-g9w6/)


位运算15、快速幂16

---

26、28

[剑指 Offer 28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/mian-shi-ti-28-dui-cheng-de-er-cha-shu-di-gui-qing/)

[二叉树对称性递归题目汇总](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/yi-pian-wen-zhang-dai-ni-chi-tou-dui-che-uhgs/)

13、16、18、29、31

> 14-20没做, 18想7月16日早上自己做一下

----

33、34、38 需要重做

35 error

剑指 Offer 39. 数组中出现次数超过一半的数字 | 摩尔投票法

----

40 最小的 k 个数 (必会!!!)

45 python自定义函数的定义

> 比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。

46 一维dp，需要重做

48 同向双指针，最长不含重复字符的子字符串，必回!!!

49 一维dp，需要重做

53 二分，需要重做

54 bst，需要重做

> 排序数组中的搜索问题，首先想到 二分法 解决。

55 二叉树的深度 once ok

58 once okk


---

辣鸡题目

20. 表示数值的字符串



​																																																				**于2021年7月**
