from queue import PriorityQueue # 优先队列
# 创建优先队列
pQ = PriorityQueue() #
pQ.put(3)
pQ.put(100)
pQ.put(78)
print(pQ)
# <queue.PriorityQueue object at 0x10f3df7b8>
print(pQ.queue)
# [3, 100, 78]
pQ.put(1)
pQ.put(2)
print("优先队列：",pQ.queue)
# 优先队列： [1, 2, 78, 100, 3]
pQ.get() # #返回并删除优先级最低的元素
print("删除后剩余元素",pQ.queue)
pQ.get()
print("删除后剩余元素",pQ.queue)
pQ.get()
print("删除后剩余元素",pQ.queue)
pQ.get()
print("删除后剩余元素",pQ.queue)
pQ.get() #  #查看优先级队列中的所有元素
print("全部被删除后",pQ.queue)

"""
# 返回队列中数值最小的元素
[3, 100, 78]
优先队列： [1, 2, 78, 100, 3]
删除后剩余元素 [2, 3, 78, 100]
删除后剩余元素 [3, 100, 78]
删除后剩余元素 [78, 100]
删除后剩余元素 [100]
全部被删除后 []
"""
