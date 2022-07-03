from collections import deque # 双端队列
# 双端队列不带排序功能
dQ = deque(['Eric','John','Smith'])
print(dQ[0]) # 查看第一个元素，不删除
print(dQ[-1]) # 查看最后一个元素，不删除
# deque(['Eric', 'John', 'Smith'])
dQ2 = deque([3,5,1,2])
print(dQ2)
# deque([3, 5, 1, 2])
dQ.append("Amy") # #在右侧插入新元素
print(dQ)
deque(['Eric', 'John', 'Smith', ['Amy']])
dQ.appendleft("Tom") # #在左侧插入新元素
print(dQ) # deque(['Tom', 'Eric', 'John', 'Smith', 'Amy'])
dQ.rotate(2) # 循环右移2次
print("循环右移2次后的队列",dQ)
dQ.popleft()
print("删除最左端元素后的队列",dQ)
# deque(['Amy', 'Tom', 'Eric', 'John'])
dQ.pop()
print("删除最右端元素后的队列",dQ)
# deque(['Amy', 'Tom', 'Eric'])