class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleNodeList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            print('empty')
            return
        cur = self.head
        while cur:
            print(cur.item, end=' ')
            cur = cur.next
        print(' ')

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

    def add(self, val):
        """ 头部添加 """
        node = Node(val)
        cur = self.head
        node.next = cur
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
        pre = None
        cur = self.head
        while cur:
            if cur.item == item:
                '''头节点'''
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.head
        while cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


# ll = SingleNodeList()
# print(ll.is_empty())
# print(ll.length())
# ll.append(1)
# ll.append(12)
# ll.append(13)
# ll.append(14)
# ll.travel()
# print(ll.is_empty())
# print(ll.length())
# ll.add(5)
# ll.travel()
# ll.insert(0, 100)
# ll.travel()
# ll.insert(1, 110)
# ll.travel()
# ll.insert(100, 200)
# ll.travel()
# ll.remove(100)
# ll.travel()
# print(ll.search(5))
# print(ll.search(50))
