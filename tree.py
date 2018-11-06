class Node:
    def __init__(self, val=None):
        self.item = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def travel(self):
        # 广度遍历
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    def pre_travel(self, node):
        """ 前序遍历 """
        if node is None:
            return
        print(node.item, end=' ')
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def mid_travel(self, node):
        """ 中序遍历 """
        if node is None:
            return
        self.mid_travel(node.left)
        print(node.item, end=' ')
        self.mid_travel(node.right)

    def last_travel(self, node):
        """ 后续遍历 """
        if node is None:
            return
        self.last_travel(node.left)
        self.last_travel(node.right)
        print(node.item, end=' ')


t = Tree()
t.add(0)
t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(5)
t.add(6)
t.add(7)
t.add(8)
t.add(9)
t.travel()
print(' ')
t.pre_travel(t.root)
print(' ')
t.mid_travel(t.root)
print(' ')
t.last_travel(t.root)
