from DataStructure.queue import ArrayQueue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if node is None:
            return

        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=' ')

    def level_order(self):
        if self.root is None:
            return

        queue = ArrayQueue()
        queue.enqueue(self.root)
        while not queue.is_empty:
            current_node = queue.dequeue()
            print(current_node.data, end=' ')

            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)

    def traversal(self, node, order=''):
        if order == 'preorder':
            self.preorder(node)
        elif order == 'inorder':
            self.inorder(node)
        elif order == 'postorder':
            self.postorder(node)
        elif order == 'level-order':
            self.level_order()


class BinaryTreeArray:
    def __init__(self, height):
        self.tree = [None]*(2**height)

    def __len__(self):
        return len(self.tree)

    def __str__(self):
        return str(self.tree)

    def __setitem__(self, key, value):
        self.tree[key] = value

    def get_parent(self, index):
        return self.tree[index//2]

    def get_left(self, index):
        return self.tree[index*2]

    def get_right(self, index):
        return self.tree[index*2+1]


def binary_tree_test():
    binary_tree = BinaryTree()
    binary_tree.root = TreeNode(1)
    binary_tree.root.left = TreeNode(2)
    binary_tree.root.right = TreeNode(3)
    binary_tree.root.left.left = TreeNode(4)
    binary_tree.root.left.right = TreeNode(5)
    binary_tree.root.right.left = TreeNode(6)
    binary_tree.root.right.right = TreeNode(7)

    print('Preorder:', end=' ')
    binary_tree.preorder(binary_tree.root)
    print()
    print('Inorder:', end=' ')
    binary_tree.inorder(binary_tree.root)
    print()
    print('Postorder:', end=' ')
    binary_tree.postorder(binary_tree.root)
    print()
    print('Level-order:', end=' ')
    binary_tree.level_order()
    print()


def binary_tree_array_test():
    binary_tree_array = BinaryTreeArray(3)
    for i in range(1, 8):
        binary_tree_array[i] = i

    print(binary_tree_array)


if __name__ == '__main__':
    binary_tree_test()
    print('=======================')
    binary_tree_array_test()

