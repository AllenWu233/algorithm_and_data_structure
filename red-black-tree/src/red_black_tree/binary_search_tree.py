class Node:
    def __init__(self, key=None, data=None, left=None, right=None, p=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.p = p


class BSTree:
    def __init__(self, key_list=[]):
        self.root = None
        if key_list:
            for key in key_list:
                self.insert(key)

    def _search_rec(self, x, k):
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self._search_rec(x.left, k)
        return self._search_rec(x.right, k)

    def search_rec(self, k):
        """Recursive tree search"""
        return self._search_rec(self.root, k)

    def search(self, k):
        """Iterative tree search"""
        x = self.root
        while x and x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def min(self, x=None):
        """Return the node with minium value of the tree/subtree"""
        if x is None:
            x = self.root
        while x and x.left:
            x = x.left
        return x

    def max(self, x=None):
        """Return the node with maximum value of the tree/subtree"""
        if x is None:
            x = self.root
        while x and x.right:
            x = x.right
        return x

    def successor(self, x):
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

    def predecessor(self, x):
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

    def insert_node(self, z):
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

    def insert(self, v, data=None):
        """Create a node with key and data, insert it in the tree"""
        self.insert_node(Node(key=v, data=data))

    def _transparent(self, u, v):
        """Replace a subtree rooted at u with a subtree rooted at v"""
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if u:
            v.p = u.p

    def delete_node(self, z):
        """Delete given node"""
        if z.left is None:
            self._transparent(z, z.right)
        elif z.right is None:
            self._transparent(z, z.left)
        else:
            y = self.min(z.right)
            if y is None:
                return
            if y.p != z:
                self._transparent(y, y.right)
                y.right = z.right
                y.right.p = y
            self._transparent(z, y)
            y.left = z.left
            y.left.p = y

    def print_node(self, x, print_data=False, end="\n"):
        if x is None:
            print(None, end=end)
        else:
            if print_data is True:
                print(x.key, end=" ")
                print(x.data, end=end)
            else:
                print(x.key, end=end)

    def _print_tree(self, x, print_data, end):
        if x is None:
            return
        self._print_tree(x.left, print_data, end)
        self.print_node(x, print_data, end=end)
        self._print_tree(x.right, print_data, end)

    def print_tree(self, print_data=False, end=" "):
        """Inorder tree walk"""
        self._print_tree(self.root, print_data, end=end)
        if end == " ":
            print()

    def bfs(self):
        if self.root is None:
            return
        queue = [(0, self.root)]
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
    a = BSTree([5, 1, 3, 0, 7, 8, 6, 10, 15, 14, 17, 19, 20, 22])

    a.print_tree(print_data=True, end="\n")
    print()

    a.print_tree()
    print()

    a.print_node(a.search(7), print_data=True)
    a.print_node(a.search_rec(7), print_data=True)
    print()

    print("Min:", a.min().key)
    print("Max:", a.max().key)

    a.bfs()
