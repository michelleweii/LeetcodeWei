"""
middle 单调栈
2021-07-19
"""
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
        while self.max_q and value>self.max_q[-1]:
            self.max_q.pop() # 注意这里是左边
        self.max_q.append(value)

    def pop_front(self) -> int:
        if not self.q:return -1
        tmp = self.q.pop(0)
        if self.max_q and tmp==self.max_q[0]:
            self.max_q.pop(0)
        return tmp


if __name__ == '__main__':
    obj = MaxQueue()
    nums = [1,3,1,5,1]
    for value in nums:
        param_1 = obj.max_value()
        print("param_1 ", param_1)
        obj.push_back(value)

    param_3 = obj.pop_front()
    print("param_3 ", param_3)
