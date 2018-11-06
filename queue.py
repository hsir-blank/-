class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def enqueue(self, val):
        self.item.insert(0, val)
        # self.item.append(val)  # 看队列的进出来选择其中一种

    def dequeue(self):
        return self.item.pop() if not self.is_empty() else 'empty'
        # self.item.pop(0)  # 同上


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
