class TreeNode:
    def __init__(self, data, color=1):
        self.data = data
        self.color = color  # 1: red(default); 0: black
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        """
        A red–black tree is a special type of binary search tree which each node stores an extra bit representing color.
            1. Each node is either red or black.
            2. All NIL nodes are considered black.
            3. A red node does not have a red child.
            4. Every path from a given node to any of its descendant NIL nodes goes through the same number of black nodes.
            5. The root color is black.
               (The root can always be changed from red to black, this rule has little effect on analysis)
        """
        self.NIL = TreeNode(data=None, color=0)  # NIL nodes are always black;
        self.root = self.NIL
    
    def __str__(self):
        return self._print(self.root, '', True)

    def _print(self, node, indent, last):
        in_buff = ''
        if node != self.NIL:
            in_buff += indent
            if last:
                in_buff += 'R----'
                indent += '     '
            else:
                in_buff += 'L----'
                indent += '|    '

            s_color = 'RED' if node.color == 1 else 'BLACK'
            in_buff += str(node.data) + '(' + s_color + ')' + '\n'
            left_buff = self._print(node.left, indent, False)
            right_buff = self._print(node.right, indent, True)
            return in_buff + left_buff + right_buff
        else:
            return ''

    @staticmethod
    def get_grandparent(node):
        if node is None or node.parent is None:
            return None
        else:
            return node.parent.parent

    @staticmethod
    def get_uncle(node):
        if node.parent == RedBlackTree.get_grandparent(node).right:
            return RedBlackTree.get_grandparent(node).left
        else:
            return RedBlackTree.get_grandparent(node).right

    def _left_rotate(self, node):
        right = node.right
        node.right = right.left
        if right.left != self.NIL:
            right.left.parent = node

        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right

        right.left = node
        node.parent = right

    def _right_rotate(self, node):
        left = node.left
        node.left = left.right
        if left.right != self.NIL:
            left.right.parent = node

        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left

        left.right = node
        node.parent = left

    def _fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == RedBlackTree.get_grandparent(node).right:
                uncle = RedBlackTree.get_grandparent(node).left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    RedBlackTree.get_grandparent(node).color = 1
                    node = RedBlackTree.get_grandparent(node)
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)

                    node.parent.color = 0
                    RedBlackTree.get_grandparent(node).color = 1
                    self._left_rotate(RedBlackTree.get_grandparent(node))
            else:
                uncle = RedBlackTree.get_grandparent(node).right
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    RedBlackTree.get_grandparent(node).color = 1
                    node = RedBlackTree.get_grandparent(node)
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)

                    node.parent.color = 0
                    RedBlackTree.get_grandparent(node).color = 1
                    self._right_rotate(RedBlackTree.get_grandparent(node))

            if node == self.root:
                break

        self.root.color = 0

    def insert(self, key):
        node = TreeNode(key)
        node.left = self.NIL  # For the reason of memory saving, we point all NIL node to the same memory address;
        node.right = self.NIL

        root = self.root
        temp = None

        # Goto the right position we want to insert;
        while root != self.NIL:
            temp = root
            if node.data < root.data:
                root = root.left
            else:
                root = root.right

        # Insert the node;
        node.parent = temp
        if temp is None:  # Means self.root equals to self.NIL
            self.root = node
        elif node.data < temp.data:
            temp.left = node
        else:
            temp.right = node

        # If the new inserted node has no parent, it is the root node and thus set its color to black;
        if node.parent is None:
            node.color = 0
            return

        # If the new inserted node has no grandparent,
        # we don't have to fix anything that may break the properties of RBT;
        if RedBlackTree.get_grandparent(node) is None:
            return

        self._fix_insert(node)

    def _search(self, node, key):
        if node == self.NIL or key == node.data:
            return node

        if key < node.data:
            return self._search(node.left, key)

        return self._search(node.right, key)

    def search(self, key):
        return self._search(self.root, key)


if __name__ == '__main__':
    rbt = RedBlackTree()

    rbt.insert(55)
    rbt.insert(40)
    rbt.insert(65)
    rbt.insert(60)
    rbt.insert(75)
    rbt.insert(57)

    print(rbt)
