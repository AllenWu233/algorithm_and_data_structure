from binary_search_tree import Node, BSTree
from enum import Enum
from copy import deepcopy


class Color(Enum):
    RED = 0
    BLACK = 1


class RBTreeNode(Node):
    def __init__(
        self,
        color: Color,
        key: int,
        data: list[int] | None = None,
    ):
        super().__init__(key, data)
        self.color = color


class RBTree(BSTree):
    def __init__(self, key_list=[]):
        self._nil = RBTreeNode(
            color=Color.BLACK, key=0, data=None
        )  # Sentinel, an empty node, key value dose not make sence
        # super().__init__(key_list)
        self.root = deepcopy(self._nil)
        self.root.left = self._nil
        self.root.right = self._nil
        self.root.p = self._nil
        if key_list:
            for key in key_list:
                self.insert(key)

    def _is_nil(self, x: RBTreeNode) -> bool:
        return (
            x.key == self._nil.key
            and x.left == self._nil.left
            and x.right == self._nil.right
            and x.data == self._nil.data
            and x.color == self._nil.color
        )

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

    def insert(self, v, data=None):
        """Create a node with key and data, insert it in the tree"""
        self.insert_node(RBTreeNode(color=Color.RED, key=v, data=data))

    def insert_node(self, z):
        y = self._nil
        x = self.root
        while not self._is_nil(x):
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self._nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self._nil
        z.right = self._nil
        z.color = Color.RED
        self._insert_fixup(z)  # Fix color

    def _insert_fixup(self, z):
        while z.p.color == Color.RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == Color.RED:
                    z.p.color = Color.BLACK  # Case 1
                    y.color = Color.BLACK  # Case 1
                    z.p.p.color = Color.RED  # Case 1
                    z = z.p.p  # Case 1
                elif z == z.p.right:
                    z = z.p  # Case 2
                    self._left_rotation(z)  # Case 2
                z.p.color = Color.BLACK  # Case 3
                z.p.p.color = Color.RED  # Case 3
                self._right_rotation(z.p.p)
            else:
                if z.p == z.p.p.right:
                    y = z.p.p.left
                    if y.color == Color.RED:
                        z.p.color = Color.BLACK  # Case 1
                        y.color = Color.BLACK  # Case 1
                        z.p.p.color = Color.RED  # Case 1
                        z = z.p.p  # Case 1
                    elif z == z.p.left:
                        z = z.p  # Case 2
                        self._right_rotation(z)  # Case 2
                    else:
                        z.p.color = Color.BLACK  # Case 3
                        z.p.p.color = Color.RED  # Case 3
                        self._left_rotation(z.p.p)
        self.root.color = Color.BLACK

    def delete_node(self, z):
        pass

    def _transplant(self, u, v):
        pass

    def print_node(self, x: Node | None, print_data: bool = False, end: str = "\n"):
        if x is None:
            print(None, end=end)
        else:
            if print_data is True:
                print(x.key, end=" ")
                print(x.data, end=end)
            else:
                print(x.key, end=end)

    def print_tree(
        self, x: Node | None = None, print_data: bool = False, end: str = " "
    ):
        """Inorder tree walk"""
        if x is None:
            x = self.root
        self._print_tree(x, print_data, end=end)
        if end == " ":
            print()

    def _print_tree(self, x: Node | None, print_data: bool, end: str):
        if self._is_nil(x):
            return
        self._print_tree(x.left, print_data, end)
        self.print_node(x, print_data, end=end)
        self._print_tree(x.right, print_data, end)


if __name__ == "__main__":
    rbnode = RBTreeNode(color=Color.RED, key=5)
    print(rbnode.color)
    print(rbnode.data)

    rbtree = RBTree([5, 1, 3, 2, 7, 8, 6, 10, 15, 14, 17, 19, 20, 22])
    rbtree.print_tree()
    rbtree.bfs()

    # a = RBTree([2, 1, 4, 3, 5])
    # a.bfs()
    # print(a.root.left.left)
    # a._left_rotation(a.root)
    # a.bfs()
    # a._right_rotation(a.root)
    # a.bfs()
