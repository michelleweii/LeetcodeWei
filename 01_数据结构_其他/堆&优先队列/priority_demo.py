from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'eat'))
q.put((2, 'code'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)

if q:
    print('1')
"""
默认字典序升序 c<e
(2, 'code')
(2, 'eat')
(3, 'sleep')
"""