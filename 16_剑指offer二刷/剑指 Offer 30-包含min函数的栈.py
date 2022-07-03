"""
easy 单调栈
2021-07-15
"""
class MinStack:
    def __init__(self):
        self.stk, self.min_stk = [], []

    # 注意这里，=也要包含进去
    def push(self, x: int) -> None:
        self.stk.append(x)
        # if not self.min_stk: self.min_stk.append(x)
        # else:
        #     if x<self.min_stk[-1]:
        #         self.min_stk.append(x)
        if not self.min_stk or self.min_stk[-1] >= x:
            self.min_stk.append(x)

    def pop(self) -> None:
        if self.stk.pop() == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def min(self) -> int:
        return self.min_stk[-1]


if __name__ == '__main__':
    nums = [-2, 0, -3, 10]
    obj = MinStack()
    for x in nums:
        obj.push(x)
    param_3 = obj.top()
    print(param_3)
    obj.pop()
    param_4 = obj.min()
    print(param_4)