class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
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

    @staticmethod
    def get_height(node):
        if node is None:
            return 0

        return node.height

    @staticmethod
    def get_balance_factor(node):
        if node is None:
            return 0

        return AVLTree.get_height(node.left) - AVLTree.get_height(node.right)

    @staticmethod
    def left_rotate(node):
        temp = node.right
        node.right = temp.left
        temp.left = node

        node.height = max(AVLTree.get_height(node.left), AVLTree.get_height(node.right)) + 1
        temp.height = max(AVLTree.get_height(temp.left), AVLTree.get_height(temp.right)) + 1

        return temp

    @staticmethod
    def right_rotate(node):
        temp = node.left
        node.left = temp.right
        temp.right = node

        temp.height = max(AVLTree.get_height(temp.left), AVLTree.get_height(temp.right)) + 1
        node.height = max(AVLTree.get_height(node.left), AVLTree.get_height(node.right)) + 1

        return temp

    def _insert(self, node, data):
        # First: Insert the node as the BST performs;
        if node is None:
            return TreeNode(data)

        if node.data < data:
            node.right = self._insert(node.right, data)
        elif node.data > data:
            node.left = self._insert(node.left, data)
        else:
            return node

        # Second: Update the height of the ancestor;
        node.height = max(AVLTree.get_height(node.left), AVLTree.get_height(node.right)) + 1

        # Third: Get the balance factor;
        bf = AVLTree.get_balance_factor(node)

        # Forth: Rotate if the node is unbalanced;
        if bf > 1:
            if node.left.data > data:  # LL
                return self.right_rotate(node)
            elif node.left.data < data:  # LR
                node.left = self.left_rotate(node.left)  # Make it LL;
                return self.right_rotate(node)
        elif bf < -1:
            if node.right.data < data:  # RR
                return self.left_rotate(node)
            elif node.right.data > data:  # RL
                node.right = self.right_rotate(node.right)  # Make it RR;
                return self.left_rotate(node)

        return node

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root = self._insert(self.root, data)

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

        # Second: Update the height of the ancestor;
        node.height = max(AVLTree.get_height(node.left), AVLTree.get_height(node.right)) + 1

        # Third: Get the balance factor;
        bf = AVLTree.get_balance_factor(node)

        # Forth: Rotate if the node is unbalanced;
        if bf > 1:
            if node.left.data > data:  # LL
                return self.right_rotate(node)
            elif node.left.data < data:  # LR
                node.left = self.left_rotate(node.left)  # Make it LL;
                return self.right_rotate(node)
        elif bf < -1:
            if node.right.data < data:  # RR
                return self.left_rotate(node)
            elif node.right.data > data:  # RL
                node.right = self.right_rotate(node.right)  # Make it RR;
                return self.left_rotate(node)

        return node

    def delete(self, data):
        if self.root is None:
            return None
        else:
            self._delete(self.root, data)


if __name__ == '__main__':
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)
    print(avl_tree)
    avl_tree.delete(50)
    avl_tree.delete(20)
    print(avl_tree)

