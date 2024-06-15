from typing import Literal


class Node:
    def __init__(
        self,
        key: int,
        data: list[int] | None = None,
    ):
        self.key = key
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.p: Node | None = None


class BSTree:
    def __init__(self, key_list: list[int] | None = None):
        if key_list is None:
            key_list = []
        self.root: Node | None = None
        if key_list:
            for key in key_list:
                self.insert(key)
        self._nil = Node(key=0)  # An empty node, key value dose not make sence

    def search_rec(self, k: int) -> Node | None:
        """Recursive tree search"""
        return self._search_rec(self.root, k)

    def _search_rec(self, x: Node | None, k: int) -> Node | None:
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self._search_rec(x.left, k)
        return self._search_rec(x.right, k)

    def search(self, k: int) -> Node | None:
        """Iterative tree search"""
        x = self.root
        while x and x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def min(self, x: Node | None = None) -> Node | None:
        """Return the node with minium value of the tree/subtree"""
        if x is None:
            x = self.root
        while x and x.left:
            x = x.left
        return x

    def max(self, x: Node | None = None) -> Node | None:
        """Return the node with maximum value of the tree/subtree"""
        if x is None:
            x = self.root
        while x and x.right:
            x = x.right
        return x

    def successor(self, x: Node) -> Node | None:
        """Return the successor node"""
        if x is None:
            return None
        if x.right:
            return self.min(x.right)
        y = x.p
        while y and x == y.right:
            x = y
            y = y.p
        return y

    def predecessor(self, x: Node) -> Node | None:
        """Return the predecessor node"""
        if x is None:
            return None
        if x.left:
            return self.max(x.left)
        y = x.p
        while y and x == y.left:
            x = y
            y = y.p
        return y

    def insert(self, v: int, data: list[int] | None = None):
        """Create a node with key and data, insert it in the tree"""
        self.insert_node(Node(key=v, data=data))

    def insert_node(self, z: Node):
        """Insert a node in the binary search tree"""
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def _trans_plant(self, u: Node | None, v: Node | None):
        """Replace a subtree rooted at u with a subtree rooted at v"""
        if u is None or v is None:
            return
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if u:
            v.p = u.p

    def _delete_node(self, z: Node | None):
        """Delete given node"""
        if z is None:
            return
        if z.left is None:
            self._trans_plant(z, z.right)
        elif z.right is None:
            self._trans_plant(z, z.left)
        else:
            y = self.min(z.right)
            if y is None:
                return
            if y.p != z:
                self._trans_plant(y, y.right)
                y.right = z.right
                y.right.p = y
            self._trans_plant(z, y)
            y.left = z.left
            y.left.p = y

    def delete(self, key: int):
        self._delete_node(self.search(key))

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
        if x is None:
            return
        self._print_tree(x.left, print_data, end)
        self.print_node(x, print_data, end=end)
        self._print_tree(x.right, print_data, end)

    def bfs(self, x: Node | None = None):
        if x is None:
            if self.root is None:
                return
            x = self.root

        queue: list[tuple[Literal[0], Node | None]] = [(0, x)]
        cnt = -1
        while queue:
            t = queue.pop(0)
            if t[0] == cnt:
                print(t[1].key, end=" ")
            else:
                print(f"\n[{t[0]}] {t[1].key}", end=" ")
                cnt = t[0]
            if t[1].left:
                queue.append((t[0] + 1, t[1].left))
            if t[1].right:
                queue.append((t[0] + 1, t[1].right))
        print()


if __name__ == "__main__":
    bstree = BSTree([5, 1, 3, 0, 7, 8, 6, 10, 15, 14, 17, 19, 20, 22])

    bstree.print_tree(print_data=True, end="\n")
    print()

    bstree.print_tree()
    print()

    bstree.print_node(bstree.search(7), print_data=True)
    bstree.print_node(bstree.search_rec(7), print_data=True)
    print()

    print("Min:", bstree.min().key)
    print("Max:", bstree.max().key)

    bstree.bfs()

    b = Node(1)
