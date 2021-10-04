class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None:
            return ''
        else:
            return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return ''

        left_buff = self._inorder(node.left)
        in_buff = str(node.data) + ' '
        right_buff = self._inorder(node.right)

        return left_buff + in_buff + right_buff

    def _height(self, node, h):
        if node is None:
            return h

        left_h = self._height(node.left, h+1)
        right_h = self._height(node.right, h+1)

        return max(left_h, right_h)

    @property
    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)

        if node.data < data:
            node.right = self._insert(node.right, data)
        elif node.data > data:
            node.left = self._insert(node.left, data)
        else:
            return node

        return node

    def insert(self, data):
        if self.root is None:  # Check if the BST is initialized(because None is immutable)
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)  # Use another function _insert() because of the purpose of recursion;

    def _search(self, node, data):
        if node is not None:
            if node.data < data:
                return self._search(node.right, data)
            elif node.data > data:
                return self._search(node.left, data)
            else:
                return True

        return False

    def search(self, data):
        if self.root is None:
            return False
        else:
            return self._search(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node

        if node.data < data:
            node.right = self._delete(node.right, data)
            return node
        elif node.data > data:
            node.left = self._delete(node.left, data)
            return node

        # Situation 1: the node to be deleted is leaf node(no child node)
        if node.left is None and node.right is None:
            return None

        # Situation 2: the node to be deleted has only one children
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # Situation 3: the node to be deleted has two children
        # Use the successor(or predecessor) to replace the node to be deleted.
        successor_parent = node
        successor = node.right
        while successor.left is not None:  # Find out the minimum value in the right subtree;
            successor_parent = successor
            successor = successor.left

        if successor_parent != node:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

        node.data = successor.data

        return node

    def delete(self, data):
        if self.root is None:
            return None
        else:
            self._delete(self.root, data)


def initialize_bst(size=5, max_num=100):
    tree = BinarySearchTree()
    from random import randint
    for _ in range(size):
        r = randint(0, max_num)
        tree.insert(r)

    return tree


if __name__ == '__main__':
    # bst = initialize_bst()
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    print(bst)
    print(bst.height)
    bst.insert(9999)
    bst.insert(9991)
    print(bst)
    print(bst.search(9999))
    print(bst.search(99999))
    bst.delete(9999)
    bst.delete(9991)
    bst.delete(20)
    print(bst)
