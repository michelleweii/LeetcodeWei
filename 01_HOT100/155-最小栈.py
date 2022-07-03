"""
easy 2021-12-12 单调栈
v1.0 2021/01/12
思路：维护单调递减栈, # 如果是单调递增栈，最小值再min_stk[0]
"""
class MinStack:
    def __init__(self):
        self.min_stk = []
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk or val<=self.min_stk[-1]: # 单调递减栈
            self.min_stk.append(val)

    def pop(self) -> None:
        if self.stk.pop() == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1] # 最小值在栈顶

if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    tmp = [-3,0,0,-2]
    for x in tmp:
        obj.push(x)
        obj.pop()
        param_3 = obj.top()
        param_4 = obj.getMin()
