class ListPriQueueValueError(ValueError):
    pass

class Pri_Queue(object):
    def __init__(self, elems=[]):
        self._elems = list(elems)
        self._elems.sort(reverse=True)

    def is_empty(self):
        return self._elems is []

    def peek(self):
        if self.is_empty():
            raise ListPriQueueValueError("in pop")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise ListPriQueueValueError("in pop")
        return self._elems.pop()

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] < e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

# 优先队列总是会弹出当前元素中优先级最高的。当插入元素时，将其插入到满足当前优先级顺序的位置. 优先队列是一种重要的缓存结构。
# 当用列表来实现优先队列时，可以考虑利用元素在列表中的先后顺序来表示优先级关系。为了在O(1)时间内弹出优先级最高的元素，
# 所以应该将优先级最高的元素放在列表的表尾。
# 在以下的实现中，值较小的元素具有更高的优先级。



if __name__ == "__main__":
    # temp = Pri_Queue(['a', 'b', 'g', 'd'])
    # temp.enqueue('f')
    # print(temp._elems) # ['g', 'f', 'd', 'b', 'a']
    # print(temp.peek()) # a
    # temp.dequeue()
    # print(temp._elems) # ['g', 'f', 'd', 'b']

    # API使用
    from queue import PriorityQueue
    # 默认是小的在顶端，所以是小顶堆
    q = PriorityQueue()
    # #队列判空
    print(q.empty()) # True
    # #向队列中添加元素
    q.put((1,'aa'))
    q.put((0,'bb'))
    q.put((100,'cc'))
    q.put((50,'dd'))
    # #队列大小
    print(q.qsize()) # 4
    # 从队列中获取元素
    for _ in range(q.qsize()):
        print(q.get()) # get()的时候是，每个元素真实的出了队列
        # (0, 'bb')
        # (1, 'aa')
        # (50, 'dd')
        # (100, 'cc')
    print(q.empty()) # True
    q.put((98,'ss'))
    print(q.get()) # (98, 'ss')

    from heapq import heappush, heappop
    # heap = []
    # # 实现小顶堆
    # # 向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质
    # heappush(heap,(1,'aa'))
    # heappush(heap,(0,'bb'))
    # heappush(heap,(100,'cc'))
    # heappush(heap,(50,'dd'))
    # print(heap) # [(0, 'bb'), (1, 'aa'), (100, 'cc'), (50, 'dd')]
    # #从堆中删除元素，返回值是堆中最小
    # print(heappop(heap)) # (0, 'bb')
    # print(heap) # [(1, 'aa'), (50, 'dd'), (100, 'cc')],维护了堆的性质
    # print(heappop(heap)) # (1, 'aa')
    # print(heappop(heap)) # (50, 'dd')
    #
    # # 实现大顶！d=====(￣▽￣*)b
    # heapBIG = []
    # heappush(heapBIG,(-1,'aa'))
    # heappush(heapBIG,(-0,'bb'))
    # heappush(heapBIG,(-100,'cc'))
    # heappush(heapBIG,(-50,'dd'))
    # print(heapBIG) # [(-100, 'cc'), (-50, 'dd'), (-1, 'aa'), (0, 'bb')]
    # #从堆中删除元素，返回值是堆中最大
    # print(heappop(heapBIG)) # (-100, 'cc')
    # print(heapBIG) # [(-50, 'dd'), (0, 'bb'), (-1, 'aa')]
    # print(heappop(heapBIG)) # (-50, 'dd')
    # print(heappop(heapBIG)) # (-1, 'aa')



    import heapq
    heap = []
    # #向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质
    heapq.heappush(heap,(1,'aa'))
    heapq.heappush(heap,(0,'bb'))
    heapq.heappush(heap,(100,'cc'))
    heapq.heappush(heap,(50,'dd'))
    print(heap) # [(0, 'bb'), (1, 'aa'), (100, 'cc'), (50, 'dd')]
    # heapq把列表x转换成堆
    heapq.heapify(heap)
    print(heap) # [(0, 'bb'), (1, 'aa'), (100, 'cc'), (50, 'dd')]
    # print(heapq.nsmallest(heapq)) # TypeError: nsmallest() missing 1 required positional argument: 'iterable'
    # 从可迭代的迭代器中返回最大的n个数，可以指定比较的key
    print(heapq.nlargest(2,range(5))) # [4, 3]
    # 从可迭代的迭代器中返回最小的n个数，可以指定比较的key
    print(heapq.nsmallest(2,range(5))) # [0, 1]
    # 从堆中删除元素，返回值是堆中最小
    print(heapq.heappop(heap)) # (0, 'bb')
    print(heap) # [(1, 'aa'), (50, 'dd'), (100, 'cc')]






