class Node(object):
    """节点类"""
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child



class Tree(object):
    def __init__(self):
        self.root = Node()


    def rec_pre_order(self, node=None):
        """递归实现前序遍历"""
        if node:
            print(node.data, end=" ")
            self.rec_pre_order(node.left_child)
            self.rec_pre_order(node.right_child)


    def pre_order(self):
        """非递归实现前序遍历"""
        if self.root:
            ls = [self.root]
        while ls:
            node = ls.pop()
            print(node.data, end=" ")
            if node.right_child:
                ls.append(node.right_child)
            if node.left_child:
                ls.append(node.left_child)


    def pre_order2(self):
        """非递归实现前序遍历"""
        stack = []
        node = self.root
        while node or stack:
            while node:
                print(node.data, end=" ")
                stack.append(node)
                node = node.left_child
            if stack:
                node = stack.pop()
                node = node.right_child


    def rec_in_order(self, node):
        """递归实现中序遍历"""
        if node:
            self.rec_in_order(node.left_child)
            print(node.data, end=" ")
            self.rec_in_order(node.right_child)


    def in_order(self):
        """非递归实现中序遍历"""
        ls = []
        node = self.root
        while node or len(ls):
            while node:
                ls.append(node)
                node = node.left_child
            if len(ls):
                node = ls.pop()
                print(node.data, end=" ")
                node = node.right_child


    def in_order2(self):
        """非递归实现中序遍历"""
        stack = []
        node = self.root
        while node:
            while node:
                if node.right_child:
                    stack.append(node.right_child)
                stack.append(node)
                node = node.left_child
            node = stack.pop()
            while stack and (not node.right_child):
                print(node.data, end=" ")
                node = stack.pop()
            print(node.data, end=" ")
            if stack:
                node = stack.pop()
            else:
                node = None


    def rec_post_order(self, node):
        """递归实现后序遍历"""
        if node:
            self.rec_post_order(node.left_child)
            self.rec_post_order(node.right_child)
            print(node.data, end=" ")


    def post_order(self, node):
        """非递归实现后序遍历"""
        q = node
        ls = []
        while node:
            while node.left_child:
                ls.append(node)
                node = node.left_child

            while node and (node.right_child is None or node.right_child == q):
                print(node.data, end=" ")
                q = node
                if not ls:
                    return
                node = ls.pop()
            ls.append(node)
            node = node.right_child


    def get_depth(self):
        """计算树的深度，递归树的左右节点,取值大的深度"""
        def _depth(node):
            if not node:
                return 0
            else:
                left_depth = _depth(node.left_child)
                right_depth = _depth(node.right_child)
                if left_depth > right_depth:
                    return left_depth + 1 
                else:
                    return right_depth + 1

        return _depth(self.root)


    def get_leaves(self, node):
        """递归输出所有叶子节点"""
        if node:
            if not node.left_child and not node.right_child:
                print(node.data, end=" ")
            else:
                self.get_leaves(node.left_child)
                self.get_leaves(node.right_child)


if __name__ == '__main__':
    tree = Tree()
    tree.root = Node('A')
    tree.root.left_child = Node('B')
    tree.root.right_child = Node('C')
    tree.root.left_child.left_child = Node('D')
    tree.root.left_child.right_child = Node('E')
    tree.root.left_child.right_child.right_child = Node('F')
    tree.root.left_child.left_child.right_child = Node('G')

    print("""
                 A
                 |
           -------------
           |           |      
           B           C
           |   
     -------------
     |           | 
     D           E 
     |           |
  -------     -------
  |     |     |     |
(None)  G   (None)  F
""")
    
    print("#先序遍历")
    print("递归：")
    tree.rec_pre_order(tree.root)
    print("\n非递归1：")
    tree.pre_order()
    print("\n非递归2：")
    tree.pre_order2()

    print("\n\n#中序遍历")
    print("递归：")
    tree.rec_in_order(tree.root)
    print("\n非递归1：")
    tree.in_order()
    print("\n非递归2：")
    tree.in_order2()


    print("\n\n#后序遍历")
    print("递归：")
    tree.rec_post_order(tree.root)
    print("\n非递归：")
    tree.post_order(tree.root)

    print("\n\n二叉树的深度为：", tree.get_depth())

    print("\n叶子节点：", end="")
    tree.get_leaves(tree.root)