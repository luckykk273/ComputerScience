from math import ceil


class TreeNode:
    def __init__(self, order):
        self.order = order
        self.values = []
        self.keys = []
        self.next_key = None
        self.parent = None
        self.is_leaf = False


class BPlusTree:
    def __init__(self, order):
        self.root = TreeNode(order)
        self.root.is_leaf = True

    def __str__(self):
        node_list = [self.root]
        level_list = [0]
        flag = 0
        str_buff = ''

        while node_list:
            node = node_list.pop(0)
            level = level_list.pop(0)
            if node.is_leaf:
                for k, v in enumerate(node.keys):
                    str_buff += str(v.values) + '\n'

                if not flag:
                    flag = 1
            else:
                for k, v in enumerate(node.keys):
                    str_buff += str(v.values) + '\n'

        return str_buff

    @staticmethod
    def _insert_at_leaf(leaf: TreeNode, key, value):
        if leaf.values:
            values = leaf.values
            for i in range(len(values)):
                if value == values[i]:
                    leaf.keys[i].append(key)
                    break
                elif value < values[i]:
                    leaf.values = leaf.values[:i] + [value] + leaf.values[i:]
                    leaf.keys = leaf.keys[:i] + [[key]] + leaf.keys[i:]
                    break
                elif i == len(values) - 1:
                    leaf.values.append(value)
                    leaf.keys.append([key])
                    break
        else:
            leaf.values = [value]
            leaf.keys = [[key]]

    def _insert_in_parent(self, old_node, value, new_node):
        if old_node == self.root:
            new_root = TreeNode(old_node.order)
            new_root.values = [value]
            new_root.keys = [old_node, new_node]
            self.root = new_root
            old_node.parent = new_root
            new_node.parent = new_root
            return

        parent_node = old_node.parent
        for i in range(len(parent_node.keys)):
            if parent_node.keys[i] == old_node:
                parent_node.values = parent_node.values[: i] + [value] + parent_node.values[i:]
                parent_node.keys = parent_node.keys[: i+1] + [new_node] + parent_node.keys[i+1:]

                if len(parent_node.keys) > parent_node.order:
                    new_parent_node = TreeNode(parent_node.order)
                    new_parent_node.parent = parent_node.parent
                    mid = int(ceil(parent_node.order/2)) - 1
                    new_parent_node.values = parent_node.values[mid+1:]
                    new_parent_node.keys = parent_node.keys[mid+1:]
                    if mid == 0:
                        parent_node.values = parent_node.values[: mid+1]
                    else:
                        parent_node.values = parent_node.values[:mid]

                    parent_node.keys = parent_node.keys[: mid+1]
                    for j in parent_node.keys:
                        j.parent = parent_node
                    for j in new_parent_node.keys:
                        j.parent = new_parent_node

                    self._insert_in_parent(parent_node, parent_node.values[mid], new_parent_node)

    def insert(self, key, value):
        value = str(value)
        old_node = self._search(value)
        BPlusTree._insert_at_leaf(old_node, key, value)

        if len(old_node.values) == old_node.order:  # If the leaf is full
            # New a leaf node
            new_node = TreeNode(old_node.order)
            new_node.is_leaf = True
            new_node.parent = old_node.parent

            # Split the old node and assign the [mid+1, last] keys and values to new node
            mid = int(ceil(old_node.order/2)) - 1
            new_node.values = old_node.values[mid+1:]
            new_node.keys = old_node.keys[mid+1:]
            new_node.next_key = old_node.next_key

            # The old node only keeps [0, mid+1) keys and values
            old_node.values = old_node.values[: mid+1]
            old_node.keys = old_node.keys[: mid+1]
            old_node.next_key = new_node  # Because the new node is right after the old node, the old node will point to the new node

            self._insert_in_parent(old_node, new_node.values[0], new_node)

    def _search(self, value):
        current_node = self.root  # Start from the root node
        while not current_node.is_leaf:  # Because the data are store in the leaf node, we have to iterate the tree until we meet the leaf node
            values = current_node.values
            for i in range(len(values)):
                # If we find the value, go to the right child node;
                # Or if the value we search is greater than all value in this node, so go to the right most child node
                if value == values[i] or i == len(current_node.values)-1:
                    current_node = current_node.keys[i+1]
                    break
                elif value < values[i]:  # If the value is smaller, then go to the left child node
                    current_node = current_node.keys[i]
                    break

        return current_node

    def search(self, key, value):
        leaf = self._search(value)
        for k, v in enumerate(leaf.values):
            if v == value:
                if key in leaf.keys[k]:
                    return True
                else:
                    return False

        return False


def initialize_tree(order):
    b_plus_tree = BPlusTree(order)
    b_plus_tree.insert('33', '5')
    b_plus_tree.insert('21', '15')
    b_plus_tree.insert('31', '25')
    b_plus_tree.insert('41', '35')
    b_plus_tree.insert('10', '45')

    return b_plus_tree


if __name__ == '__main__':
    b_plus_tree = initialize_tree(3)
    print(b_plus_tree.search('21', '15'))
    print(b_plus_tree)
