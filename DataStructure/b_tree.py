
class TreeNode:
    def __init__(self, is_leaf=False):
        """
            keys:
                - Store an array of keys(keys[0], keys[1], ..., keys[2b-1])
                    - If there are k children, the number of keys is exactly k-1(keys[0], keys[1], ..., keys[k-2])
                    - The remained 2b-(k-1) elements are set to None
                - Contain between b-1 and 2b-1 keys(because the number of keys is one less than the number of children)
                - For any node in B-tree, that store k-1 keys, the keys are arranged in an ascending order.
                  (keys[0] < keys[1] < ... < keys[k-2])
            children:
                - Every non-root internal node has at least b children and at most 2b children
        """

        self.is_leaf = is_leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, b):
        self.root = TreeNode(True)
        # Every non-root internal node has at least b children and at most 2b children;
        self.b = b

    def _level_order(self, node, level=0):
        curr_buff = 'Level ' + str(level) + ' --> ' + str(len(node.keys)) + ': '
        for key in node.keys:
            curr_buff += str(key) + ' '
        curr_buff += '\n'

        child_buff = ''
        if node.children:
            for child in node.children:
                curr_buff += self._level_order(child, level+1)

        return curr_buff + child_buff

    def __str__(self):
        if not self.root.keys:
            return ''
        else:
            return self._level_order(self.root, 0)

    def _split(self, node: TreeNode, index):
        """
        Split the child of node from index;
        :param node: Parent node of the node to be split
        :param index: Index value of the child
        """
        # First get the node we want to split;
        split_node = node.children[index]

        # New a node: because the split node and the new node are at the same level(height),
        # just pass the is_leaf of the split node;
        new_node = TreeNode(split_node.is_leaf)

        # Insert the new node to the position+1
        node.children.insert(index+1, new_node)

        # Move the medium keys to the parent node
        node.keys.insert(index, split_node.keys[self.b-1])

        # Left nodes contain the left half keys; Right node contains the right half keys
        # There are totally 2b-1 keys, and the medium key(key at position b-1) is moved to the parent node.
        # So There are 2b-2 keys left;
        new_node.keys = split_node.keys[self.b: 2*self.b-1]  # Right node contains the keys from b to 2b-2
        split_node.keys = split_node.keys[0: self.b-1]  # Left node contains the keys from 0 to b-2

        # If split node is not leaf, we also have to reassign child pointers
        if not split_node.is_leaf:
            new_node.children = split_node.children[self.b: 2*self.b]  # Right node contains the children from b to 2b-1
            split_node.children = split_node.children[0: self.b-1]  # Left node contains the children from 0 to b-2

    def _insert_non_full(self, node: TreeNode, key):
        """
        Insert a key to a non-full node;
        :param node: the node you want to insert
        :param key: the key to be inserted
        """
        length = len(node.keys) - 1
        if node.is_leaf:
            node.keys.append(None)
            while length > -1 and key < node.keys[length]:
                node.keys[length+1] = node.keys[length]  # Move the keys one index to right
                length -= 1

            node.keys[length+1] = key
        else:
            # First move to the position to insert;
            while length > -1 and key < node.keys[length]:
                length -= 1

            # Check if the node is full;
            length += 1
            if len(node.children[length].keys) == 2 * self.b - 1:
                self._split(node, length)  # If the node is full, we have to split the node
                if key > node.keys[length]:
                    length += 1

            # Then insert the key to the child node at the correct position
            self._insert_non_full(node.children[length], key)

    def insert(self, key):
        root = self.root

        if len(root.keys) == 2 * self.b - 1:  # Check if a node is full
            # Assign a new node to the root and insert the former root to the children of the new node `temp` at index 0
            temp = TreeNode()
            self.root = temp
            temp.children.insert(0, root)

            # Split the child(former root)
            self._split(temp, 0)

            # Now the node will be not full, so just insert it
            self._insert_non_full(temp, key)
        else:
            self._insert_non_full(root, key)

    def _search(self, key, node):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node, i
        elif node.is_leaf:
            return None
        else:
            return self._search(key, node.children[i])

    def search(self, key):
        return self._search(key, self.root)

    def _delete_predecessor(self, node: TreeNode):
        if node.is_leaf:
            return node.keys.pop()

        length = len(node.keys) - 1
        if len(node.children[length].keys) >= self.b:
            self._delete_sibling(node, length+1, length)
        else:
            self._delete_merge(node, length, length+1)
        self._delete_predecessor(node.children[length])

    def _delete_successor(self, node: TreeNode):
        if node.is_leaf:
            return node.keys.pop(0)

        if len(node.children[1].keys) >= self.b:
            self._delete_sibling(node, 0, 1)
        else:
            self._delete_merge(node, 0, 1)

        self._delete_successor(node.children[0])

    def _delete_internal_node(self, node, key, index):
        b = self.b
        if node.is_leaf:
            if node.keys[index] == key:
                node.keys.pop(index)
                return
            return

        if len(node.children[index].keys) >= b:
            node.keys[index] = self._delete_predecessor(node.children[index])
            return
        elif len(node.children[index+1].keys) >= b:
            node.keys[index] = self._delete_successor(node.children[index+1])
            return
        else:
            self._delete_merge(node, index, index+1)
            self._delete_internal_node(node.children[index], key, b - 1)

    @staticmethod
    def _delete_sibling(node, i, j):
        child_node = node.children[i]
        if i < j:
            right_sibling_node = node.children[j]
            child_node.keys.append(node.keys[i])  # Move the element to the child node
            node.keys[i] = right_sibling_node.keys[0]  # Move the element of the right sibling child node to its parent
            if len(right_sibling_node.children) > 0:
                child_node.children.append(right_sibling_node.children[0])  # Move the child node of the right sibling node to the child node
                right_sibling_node.children.pop(0)  # Remove the child node of the right sibling node
            right_sibling_node.keys.pop(0)  # Remove the element of the right sibling node
        else:
            left_sibling_node = node.children[j]
            child_node.keys.insert(0, node.keys[i-1])
            if len(left_sibling_node.children) > 0:
                child_node.children.insert(0, left_sibling_node.children.pop())

    def _delete_merge(self, node, i, j):
        child_node = node.children[i]
        if i < j:
            right_sibling_node = node.children[j]
            child_node.keys.append(node.keys[i])
            for k in range(len(right_sibling_node.keys)):  # Append all keys and children from right sibling node to child node
                child_node.keys.append(k)
                if len(right_sibling_node.children) > 0:
                    child_node.children.append(right_sibling_node.children[k])

            if len(right_sibling_node.children) > 0:
                child_node.children.append(right_sibling_node.children.pop())

            new_node = child_node
            node.keys.pop(i)
            node.children.pop(j)
        else:
            left_sibling_node = node.children[j]
            left_sibling_node.keys.append(node.keys[j])
            for k in range(len(child_node.keys)):
                left_sibling_node.keys.append(child_node.keys[i])
                if len(left_sibling_node.children) > 0:
                    left_sibling_node.children.append(child_node.children[i])

            if len(left_sibling_node.children) > 0:
                left_sibling_node.children.append(child_node.children.pop())

            new_node = left_sibling_node
            node.keys.pop(j)
            node.children.pop(i)

        if node == self.root and len(node.keys) == 0:
            self.root = new_node

    def delete(self, node, key):
        b = self.b
        i = 0
        while i < len(node.keys) and key > node.keys[i]:  # Find out the node we want to delete;
            i += 1

        if node.is_leaf:  # If the node is the leaf;
            if i < len(node.keys) and key == node.keys[i]:
                node.keys.pop(i)
                return
            return

        if i < len(node.keys) and key == node.keys[i]:  # If the node is the internal node and contain the key
            return self._delete_internal_node(node, key, i)
        elif len(node.children[i].keys) >= b:  # If the size of the children is greater than the order, recursively call the delete function with its children
            self.delete(node.children[i], key)
        else:
            if i != 0 and (i + 2) < len(node.children):  # The index has been moved
                if len(node.children[i-1].keys) >= b:
                    BTree._delete_sibling(node, i, i-1)
                elif len(node.children[i+1].keys) >= b:
                    BTree._delete_sibling(node, i, i-1)
                else:
                    self._delete_merge(node, i, i+1)
            elif i == 0:  # The index hasn't been moved(just at the beginning)
                if len(node.children[i+1].keys) >= b:
                    BTree._delete_sibling(node, i, i+1)
                else:
                    self._delete_merge(node, i, i+1)
            elif i + 1 == len(node.children):
                if len(node.children[i-1].keys) >= b:
                    BTree._delete_sibling(node, i, i-1)
                else:
                    self._delete_merge(node, i, i-1)

            self.delete(node.children[i], key)


if __name__ == '__main__':
    b_tree = BTree(3)
    for i in range(10):
        b_tree.insert(i)

    print(b_tree)
    print(b_tree.search(5))

    b_tree.delete(b_tree.root, 5)

    print(b_tree)
    print(b_tree.search(5))
