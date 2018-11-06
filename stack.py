class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def top(self):
        # 栈顶
        return self.item[-1] if not self.is_empty() else 'empty'

    def peek(self):
        # 栈底
        return self.item[0] if not self.is_empty() else 'empty'

    def push(self, val):
        self.item.append(val)

    def pop(self):
        return self.item.pop() if not self.is_empty() else 'empty'


s = Stack()
s.push(0)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.top())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
