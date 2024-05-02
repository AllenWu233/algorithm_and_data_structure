from binary_search_tree import Node, BSTree
from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class RBTreeNode(Node):
    def __init__(self, color, key=None, data=None, left=None, right=None, p=None):
        super().__init__(key, data, left, right, p)
        self.color = color


class RBTree(BSTree):
    def __init__(self, key_list=[]):
        super().__init__(key_list)
        self._nil = RBTreeNode(color=Color.BLACK)  # Sentinel, a empty node

    def _left_rotation(self, x):
        y = x.right  # Set y
        x.right = y.left  # Turn y's left subtree into x's right subtree
        if y.left != self._nil:
            y.left.p = x
        y.p = x.p  # Link x's parent to y
        if x.p == self._nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def _right_rotation(self, y):
        x = y.left  # Set x
        y.left = x.right  # Turn x's right subtree into y's left subtree
        if x.right != self._nil:
            x.right.p = y
        x.p = y.p  # Link y's parent to x
        if y.p == self._nil:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def _insert_fixup(self, z):
        pass

    def insert_node(self, z):
        self._insert_fixup(z)

    def _transplant(self, u, v):
        pass

    def delete_node(self, z):
        pass


if __name__ == "__main__":
    rbnode = RBTreeNode(color=Color.RED)
    print(rbnode.color)
    print(rbnode.data)

    rbtree = RBTree([5, 1, 3, 0, 7, 8, 6, 10, 15, 14, 17, 19, 20, 22])
    rbtree.print_tree()

    a = RBTree([1])
    a.root.left = a._nil
    print(a.root.left.color)
    print(a.root.left == a._nil)
