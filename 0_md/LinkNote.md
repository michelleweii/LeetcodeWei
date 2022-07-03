# 链表

掌握中点、反转链表、头插法。（LC234、LC143考察点LC206反转链表+LC876链表中点）

头插法；链表在插入的时候进行反转，比如节点1,2,3，头插结果为3,2,1。
```python
dummy = ListNode(-1)
cur = ListNode(sum)
# 链表在插入的时候如何进行反转？头插法
cur.next = dummy.next
dummy.next = cur
```

## 链表环相关

[环长度、有环，环入口](https://codeantenna.com/a/MZ4dtjeB6r#4__100)

1. **LC141 判断是否为环形链表？**

结论：快慢指针，若有环fast=n*slow，则相遇时fast=slow, return True; else False.

```python
class Solution(object):
    def hasCycle(self, head):
        slow = head # 慢指针
        fast = head # 快指针
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

2. **LC142 若为环形链表，求环入口点？**

结论：**<u>快慢指针</u> 相遇点到环入口的距离=链表起始点到环入口的距离。**

1）快慢指针先求出相遇点；

2）一个指针从head开始，一个指针从相遇点开始，再次相遇时则为环入口。

根据f=2s（快指针每次2步，路程刚好2倍），f=s+nb (相遇时，刚好多走了n圈), =>推出：s = nb。
从head结点走到入环点需要走：a+nb, 而slow已经走了nb，那么slow再走a步就是入环点了。

```python
# 2022/02/28更新
"""
假设a是head至环入口长度，b是环长度，假设fast一共走了K=a+nb;
有 f=2s, f=s+nb (相遇时，刚好多走了n圈), =>推出：s = nb。
=》fast = a+s，相遇时，s再走a即到达入口。
=》slow如何再走a? fast回到起始点head，走a，slow也走a，即两者再次相遇是环入口位置。
"""
class Solution(object):
    # 方法二：
    # 掌握推导过程
    def detectCycle(self, head):
        slow, fast = head, head
        while True:
            if not (fast and fast.next): return # 如果链表不存在环
            slow = slow.next
            fast = fast.next.next
            if slow==fast:break # 停在了相遇节点

        fast = head # 再从head出发，走a个节点
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return fast
```

3. **求环的长度？**

结论：快慢指针第一次相遇（超一圈）时开始计数，计数器累加，第二次相遇时停止计数。
第二次相遇的时候快指针比慢指针正好又多走了一圈，也就是多走的距离等于环长。
需要快满指针，第一次相遇的 flag，第二次相遇的 flag，count计数器。



4. **LC160 判断两个链表是不是相交？求交点(Y型)？**

是否相交？
性质：如果两个链表相交，那么这两个链表的尾节点一定相同。

求交点？
结论：a+c+b=b+c+a。
pa,pb谁先到达末尾，则从另一方head再次遍历，如果pa和pb相交就返回交点。





## 求链表中点

方法1

```python
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

方法2

```python
# LC109
slow, fast = head, head
pre = head
while fast and fast.next:
     pre = slow
     slow, fast = slow.next, fast.next.next
mid = slow
# 拆分左右链表
pre.next = None # 左子树断开
```



扩展

1. LC234.回文链表
   - 如何求回文链表，链表中点+翻转链表，逐个对比。

​		



## LRU&LFU缓存机制

> - LRU(Least Recently Used) 最近最少使用算法，它是根据时间维度来选择将要淘汰的元素，即删除掉最长时间没被访问的元素。
>
> - LFU(Least Frequently Used) 最近最不常用算法，它是根据频率维度来选择将要淘汰的元素，即删除访问频率最低的元素。如果两个元素的访问频率相同，则淘汰最久没被访问的元素。
>
>   也就是说LFU淘汰的时候会选择两个维度，先比较频率，选择访问频率最小的元素；如果频率相同，则按时间维度淘汰掉最久远的那个元素。

LC146.LRU总结（LRU (最近最少使用) 缓存淘汰机制）

> 维护一个双向链表，链表头部存旧元素，链表尾部存新元素；
> 更新/添加/访问——>移到链表尾部；超过capacity需要删除元素；
> hashmap便于快速定位是否存在某值节点，O(1)时间复杂度。
> def mode_to_tail: 通过key在hashmap中找到node，在原位置删除，将其移到链表尾部；
> def get: 访问这个元素，如果在hashmap中，将其移到链表尾部，返回值；不在hashmap则返回-1；
> def put: 添加元素，
>    - case1: 已经在hashmap中，更新value值，移到末尾；
>         - case2: 不在hashmap中，
>         -  case2.1. 超过capacity, 移除链表头部元素（hashmap+doublelinked），创建新node，添加到末尾；
>         -  case2.2. 没有超过capacity, 创建node，添加到末尾；



LC460.LFU总结（LFU (最近最不常用) 缓存淘汰机制）

- LRU的实现是一个哈希表加上一个双链表；

- LFU需要用两个哈希表(kv hashmap+频率hashmap)再加上N个双链表才能实现；(头放新元素，尾放旧元素）

  两个hashmap的关系是，k-v哈希表中key1指向一个Node，这个Node的频率为1，位于频率哈希表中key=1下面的双链表中(处于第一个节点)。



minfreq 记录LFU缓存中频率最小的元素，快速定位到最小freq的链表。
？ 待明确这个变量到底是加在哪里的？minfreq是LRU类变量。不是双向链表的变量。
一个node包含k,v,freq。node组成双向链表。

```python
def get: 访问元素，
- case1. key不在hashmap则返回-1；
- case2. 如果key存在，则返回对应的value，同时:将元素的访问频率+1。
    - case2.1. 将元素从访问频率i的链表中移除，放到频率i+1的链表中，如果频率i+1不存在，则要创建key。
    - case2.2. 如果频率i的链表为空，则从频率哈希表中移除这个链表。

def put: 添加元素，
- case1: 已经在hashmap中（类似访问元素），
    - case1.1. 将元素从访问频率i的链表中移除，放到频率i+1的链表中；
    - case1.2. 如果频率i的链表为空，则从频率哈希表中移除这个链表;
- case2: 不在hashmap中，
    - case2.1. 超过capacity,
        # 通过minfreq找到双向链表，在其中先删除最久未被的元素(头部元素)，kvhashmap也要删，再插入新元素（尾部元素）；
        # 新元素的freq++，如果频率哈希表中不存在对应的链表需要创建；
    - case2.2. 没有超过capacity,
        # 新元素的freq++，如果频率哈希表中不存在对应的链表需要创建；
```



