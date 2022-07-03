"""
easy 栈 easy
2021-07-13
"""
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


if __name__ == '__main__':
    value = 3
    obj = CQueue()
    obj.appendTail(value)
    param_2 = obj.deleteHead()
    print(param_2)
