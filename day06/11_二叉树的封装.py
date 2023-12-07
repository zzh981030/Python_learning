"""
二叉树:
    https://www.cnblogs.com/polly333/p/4740355.html
"""

class Node(object):
    """节点类"""
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    """封装二叉树"""
    def __init__(self, root):
        self.root = root

    def pre_travel(self, root):
        """先序遍历: 根左右"""
        if (root != None):
            print(root.val)
            self.pre_travel(root.left)
            self.pre_travel(root.right)


    def in_travel(self, root):
        """中序遍历: 左根右"""
        if (root != None):
            self.in_travel(root.left)
            print(root.val)
            self.in_travel(root.right)

    def last_travel(self, root):
        """后序遍历: 左右根"""
        if (root != None):
            self.last_travel(root.left)
            self.last_travel(root.right)
            print(root.val)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)

    bt = BinaryTree(root=node1)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    node5.left = node10


    # 先序遍历
    bt.pre_travel(node1)



