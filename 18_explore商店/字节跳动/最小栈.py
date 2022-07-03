
# 在常数时间内检索到最小元素的栈
# 栈：先进后出
class MinStack:

    def __init__(self):
        self.stk, self.min_stk = [], []


    def push(self, val: int) -> None:
        # 单调递减栈
        self.stk.append(val)
        # 如果最小栈是空的
        # 新来的数<=辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进去）
        if not self.min_stk or val<=self.min_stk[-1]: # 单调递减
            self.min_stk.append(val)


    def pop(self) -> None:
        if self.stk:
            val = self.stk.pop()
            if val==self.min_stk[-1]:
                self.min_stk.pop()


    def top(self) -> int:
        return self.stk[-1]


    def getMin(self) -> int:
        return self.min_stk[-1] # 右端，栈顶元素永远是最小的（如果是栈是上升趋势，不符合）


if __name__ == '__main__':

    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(4)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()