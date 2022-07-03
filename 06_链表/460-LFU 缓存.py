"""
hard 2021-12-23 双向链表【字节常考】
（python+看图this）https://leetcode-cn.com/problems/lfu-cache/solution/chao-xiang-xi-tu-jie-dong-tu-yan-shi-460-lfuhuan-c/
https://leetcode-cn.com/problems/lfu-cache/solution/ha-xi-biao-shuang-xiang-lian-biao-java-by-liweiwei/
https://leetcode-cn.com/problems/lfu-cache/solution/pythonshuang-xiang-lian-biao-zi-dian-jian-dan-yi-d/
题目：最不经常使用（LFU）优先访问频率高的，访问频率相同则优先最近访问的LRU，get频率高且新，然后频率++；put删掉频率最低且最久没有访问的。
"""
# 说明：本题其实就是在「力扣」第 146 题：LRU缓存机制 的基础上，在删除策略里多考虑了一个维度（「访问次数」）的信息。
# 核心思想：先考虑访问次数，在访问次数相同的情况下，再考虑缓存的时间。
# 重点：双向链表删除某节点，只需要一个元素
# 维护2个hashmap

# 定义双向链表
# 「双向链表」的尾部存储较新访问的结点，头部是当前频次最旧的结点。
# 代码按照link1实现
################### 2021-01-04 关于minfreq的理解？ ##########################
# 我们在代码实现中还需要维护一个minFreq的变量，用来记录LFU缓存中频率最小的元素，在缓存满的时候，可以快速定位到最小频繁的链表，以达到 O(1) 时间复杂度删除一个元素。
# 具体做法是:
# 更新/查找的时候，将元素频率+1，之后如果minFreq不在频率哈希表中了，说明频率哈希表中已经没有元素了，那么minFreq需要+1，否则minFreq不变。
# （对一个旧元素访问，那么其频率++，比如从freqmap=3移到freqmap=4，然后freqmap=3的为空了，删除freqmap=3，minFreq=3自然也没了，由于原始minFreq所指位置的元素
# 频率++，移到freqmap=4，那么minFreq自然就是+1变成了4）
# 插入的时候，这个简单，因为新元素的频率都是1，所以只需要将minFreq改为1即可。
# （有新的元素了，所以min_freq必然是1，定位最小频率。）
############################################################################
# 双链表中的链表节点对象
class Node:
    def __init__(self, key=0, val=0, freq=0):
        """
        Args:
            key:对应输入的key
            value:对应输入的value
            freq:被访问的频率
            pre:指向前一个节点的指针
            next:指向后一个节点的指针
        """
        self.key = key
        self.val = val
        self.freq = freq
        # # 双向链表必有
        self.next = None
        self.prev = None

# 自定义的双向链表
class DoublyLinkedList:
    # 初始化双向链表
    def __init__(self):
        self.head = Node()  # 双向链表的头结点
        self.tail = Node()  # 双向链表的尾节点
        self.head.next = self.tail
        self.tail.prev = self.head

    # 更新node：更新频率+移到末尾「双向链表」的尾部存储较新访问的结点，头部是当前频次最旧的结点。
    # 新节点插入freqmap头部
    def insert_node_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # # 更新node：更新频率+移到末尾「双向链表」的尾部存储较新访问的结点，头部是当前频次最旧的结点。
    # 删除freqmap尾部节点
    def remove_node(self, node=None):
        if self.is_empty():
            return
        if not node:
            node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    # 双向链表是否为空
    # 判断链表是否为空，除了head和tail没有其他节点即为空链表
    # 链表空返回 True
    def is_empty(self):
        return self.head.next == self.tail


# 要维护一个minFreq的变量，用来记录 LFU缓存 中频率最小的元素，在缓存满的时候，可以快速定位到最小频繁的链表，以达到 O(1) 时间复杂度删除一个元素。
# 更新/查找的时候，将元素频率+1，之后如果minFreq不在频率哈希表中了，说明频率哈希表中已经没有元素了，那么minFreq需要+1，否则minFreq不变。
# 插入的时候，这个简单，因为新元素的频率都是1，所以只需要将minFreq改为1即可。
class LFUCache:
    # 初始化LFU缓存
    def __init__(self, capacity: int):
        self.capacity = capacity  # 缓存的最大容量
        # k:node_val; v:node
        self.kv_map = dict()  # key->Node 这种结构的字典
        # k:频率; v:是这个频率下的所有节点
        self.freq_map = dict()  # freq->LinkedList 这种结构的字典
        # 记录缓存中最低频率
        self.min_freq = 0  # 类变量，在capacity满的时候快速定位频率最少链表，快速删除遍历最少链表的尾部节点

    # freqmap中添加node
    # 根据节点的频率，插入到对应的LinkedList中，如果LinkedList不存在则创建
    # 存在该key直接添加 & 不存在该key创建key后添加
    def _add_node(self, node):
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].insert_node_to_head(node)

    # 更新节点——从freqmap=3的list移动到freqmap=4的list
    # 新node：类变量minfreq=1
    #         freqmap中添加该node
    # 旧node：
    #   从prev_freq删除node：
    #   在cur_freq添加该node：
    #   旧node的freq++
    def _update_node(self, node, is_new_node):
        if is_new_node:
            self.min_freq = 1
            self._add_node(node)
        else:
            self.freq_map[node.freq].remove_node(node)
            if self.freq_map[node.freq].is_empty():
                del self.freq_map[node.freq]
                """
                # 要维护一个minFreq的变量，用来记录 LFU缓存 中频率最小的元素，在缓存满的时候，可以快速定位到最小频繁的链表，以达到 O(1) 时间复杂度删除一个元素。
                # 更新/查找的时候，将元素频率+1，之后如果minFreq不在频率哈希表中了，说明频率哈希表中已经没有元素了，那么minFreq需要+1，否则minFreq不变。
                # 插入的时候，这个简单，因为新元素的频率都是1，所以只需要将minFreq改为1即可。
                """
                if node.freq == self.min_freq:
                    self.min_freq += 1  # 更新min_freq
            node.freq += 1  # 更新节点的访问频率
            self._add_node(node)

    # 首先判断是否在kvmap中，不存在直接返回-1
    # 在kvmap中，get到node，然后更新该node的频率，返回该node.val

    def get(self, key: int) -> int:
        """
        # 如果key存在，则返回对应的value，同时: 将元素的访问频率+1
        # 更新node：
        #       将元素从访问频率i的链表中移除，放到频率i+1的链表中
        #       如果频率i的链表为空，则从频率哈希表中移除这个链表
        """
        if key not in self.kv_map:
            return -1
        node = self.kv_map[key]
        self._update_node(node, False)
        return node.val

    # 首先判断是否在kvmap中，存在说明是旧节点，更新旧节点的val和频率
    # 不在kvmap中，说明是新节点：
    #   判断capacity是否满？
    #   满：
    #       利用minfreq快速定位最小频率所在的list，删除该list中尾部节点
    #       删除之后如果freqmap该list为空，freqmap & kvmap都删除
    #   不满：
    #       kvmap添加该node
    #       freqmap更新该node
    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            node = self.kv_map[key]
            node.val = value
            self._update_node(node, False)
        else:
            # 删除指定的节点，如果节点删除后，对应的双链表为空，则从__freqmap中删除这个链表
            if not self.capacity:
                return

            if len(self.kv_map) == self.capacity:
                node_to_remove = self.freq_map[self.min_freq].remove_node()  # 双向链表删除该节点
                if self.freq_map[self.min_freq].is_empty():
                    del self.freq_map[self.min_freq]
                del self.kv_map[node_to_remove.key]  # 删除的旧node，kvmap同步删除
            node = Node(key, value, 1)
            self.kv_map[key] = node
            self._update_node(node, True)  # 更新新增node（涉及min_freq、删除节点、节点进位移动）

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

