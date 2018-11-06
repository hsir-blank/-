class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCircleList:
    """ 单向循环链表 """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            print('empty')
            return
        cur = self.head
        while cur.next != self.head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)

    def append(self, val):
        """ 尾部添加 """
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def add(self, val):
        """ 头部添加 """
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node
            self.head = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            i = 1
            node = Node(item)
            pre = self.head
            while pre:
                if i == pos:
                    node.next = pre.next
                    pre.next = node
                    break
                else:
                    pre = pre.next
                    i += 1

    def remove(self, item):
        if self.is_empty():
            return
        pre = None
        cur = self.head
        while cur.next != self.head:
            if cur.item == item:
                # 删除头节点
                if cur == self.head:
                    tail = self.head
                    while tail.next != cur:
                        tail = tail.next
                    self.head = cur.next
                    tail.next = self.head
                # 删除中间节点
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        # 尾节点
        if cur != self.head:
            pre.next = self.head
        # 尾节点与头节点相同，说明只有一个节点
        else:
            self.head = None

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.head
        while cur.next != self.head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        if cur.item == item:
            return True
        return False


ll = SingleCircleList()
print(ll.is_empty())
print(ll.length())
# ll.add(11)
# ll.travel()
# ll.add(12)
# ll.add(13)
# ll.append(14)
# ll.travel()
# print(ll.is_empty())
# print(ll.length())
# ll.remove(14)
# ll.travel()
# ll.insert(0, 100)
# ll.travel()
# ll.insert(1, 110)
# ll.travel()
ll.insert(100, 200)
ll.travel()
ll.remove(200)
ll.travel()
print(ll.search(5))
print(ll.search(100))
