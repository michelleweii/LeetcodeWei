"""
easy 2022-05-30
https://leetcode.cn/problems/implement-queue-using-stacks/solution/yong-zhan-shi-xian-dui-lie-by-leetcode-s-xnb6/
"""
class MyQueue:

    def __init__(self):
        self.stk1,self.stk2=[],[] # 输入栈，输出栈

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        if not self.stk2:
            self.turn()
        return self.stk2.pop()


    def peek(self) -> int:
        if not self.stk2:
            self.turn()
        return self.stk2[-1]

    def empty(self) -> bool:
        return not self.stk1 and not self.stk2

    def turn(self):
        while self.stk1:
            self.stk2.append(self.stk1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()