from singlenode import SingleNodeList


class Node:
    def __init__(self, item=None):
        self.item = item
        self.prev = None
        self.next = None


class DoubleNodeList(SingleNodeList):
    """ 继承单链表 """
    def __init__(self):
        self.head = None

    def append(self, val):
        """ 尾部添加 """
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def add(self, val):
        """ 头部添加 """
        node = Node(val)
        cur = self.head
        if cur:
            node.next = cur
            cur.prev = node
            self.head = node
        self.head = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            i = 1
            node = Node(item)
            cur = self.head
            while cur:
                if i == pos:
                    node.next = cur.next
                    node.next.prev = node
                    node.prev = cur.next
                    cur.next = node
                    break
                else:
                    cur = cur.next
                    i += 1

    def remove(self, item):
        cur = self.head
        while cur:
            if cur.item == item:
                '''头节点'''
                if cur == self.head:
                    self.head = cur.next
                    cur.next.prev = None
                # 中间节点
                elif cur.next:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                # 尾节点
                else:
                    cur.prev.next = None
                break
            else:
                cur = cur.next


dll = DoubleNodeList()
print(dll.is_empty())
print(dll.length())
dll.add(11)
dll.append(12)
dll.append(13)
dll.append(14)
dll.append(15)
dll.travel()
dll.remove(11)
dll.travel()
dll.remove(13)
dll.travel()
dll.remove(15)
dll.travel()
print(dll.is_empty())
print(dll.length())
dll.add(5)
dll.travel()
dll.insert(0, 100)
dll.travel()
dll.insert(1, 110)
dll.travel()
dll.insert(100, 200)
dll.travel()
print(dll.search(200))
print(dll.search(50))
