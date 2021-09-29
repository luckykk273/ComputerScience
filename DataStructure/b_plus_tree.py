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
            del level_list[0]
            if node.is_leaf:
                for idx, item in enumerate(node.keys):
                    str_buff += str(item.values) + '\n'

                if not flag:
                    flag = 1
            else:
                for idx, item in enumerate(node.keys):
                    str_buff += str(item.values) + '\n'

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
                    new_value = parent_node.values[mid]
                    if mid == 0:
                        parent_node.values = parent_node.values[: mid+1]
                    else:
                        parent_node.values = parent_node.values[:mid]

                    parent_node.keys = parent_node.keys[: mid+1]
                    for key in parent_node.keys:
                        key.parent = parent_node
                    for key in new_parent_node.keys:
                        key.parent = new_parent_node

                    self._insert_in_parent(parent_node, new_value, new_parent_node)

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
                if value == values[i]:
                    current_node = current_node.keys[i + 1]
                    break
                elif value < values[i]:  # If the value is smaller, then go to the left child node
                    current_node = current_node.keys[i]
                    break
                elif i == len(current_node.values) - 1:
                    current_node = current_node.keys[i + 1]
                    break

        return current_node

    def search(self, key, value):
        leaf = self._search(value)
        for idx, item in enumerate(leaf.values):
            if item == value:
                if key in leaf.keys[idx]:
                    return True
                else:
                    return False

        return False

    def _delete_entry(self, node, key, value):
        if not node.is_leaf:
            for idx, item in enumerate(node.keys):
                if item == key:
                    node.keys.pop(idx)
                    break
            for idx, item in enumerate(node.values):
                if item == value:
                    node.values.pop(idx)
                    break

        if node == self.root and len(node.keys) == 1:
            self.root = node.keys[0]
            node.keys[0].parent = None
            del node
            return
        elif (len(node.keys) < int(ceil(node.order/2)) and not node.is_leaf) or \
                (len(node.values) < int(ceil((node.order-1)/2)) and node.is_leaf):
            is_predecessor = False
            parent_node = node.parent
            prev_node = None
            next_node = None
            prev_value = -1
            post_value = -1
            for idx, item in enumerate(parent_node.keys):
                if item == node:
                    if idx > 0:
                        prev_node = parent_node.keys[idx-1]
                        prev_value = parent_node.values[idx-1]
                    if idx < len(parent_node.keys) - 1:
                        next_node = parent_node.keys[idx+1]
                        post_value = parent_node.values[idx]

            if prev_node is None:
                new_node = next_node
                new_value = post_value
            elif next_node is None:
                is_predecessor = True
                new_node = prev_node
                new_value = prev_value
            else:
                if len(node.values) + len(next_node.values) < node.order:
                    new_node = next_node
                    new_value = post_value
                else:
                    is_predecessor = True
                    new_node = prev_node
                    new_value = prev_value

            if len(node.values) + len(new_node.values) < node.order:
                if not is_predecessor:
                    node, new_node = new_node, node

                new_node.keys += node.keys

                if not node.is_leaf:
                    new_node.values.append(new_value)
                else:
                    new_node.next_key = node.next_key

                new_node.values += node.values

                if not new_node.is_leaf:
                    for key in new_node.keys:
                        key.parent = new_node

                self._delete_entry(node.parent, node, new_value)
                del node
            else:
                if is_predecessor:
                    if not node.is_leaf:
                        new_node_pop_key = new_node.keys.pop(-1)
                        new_node_pop_value = new_node.values.pop(-1)
                        node.keys = [new_node_pop_key] + node.keys
                        node.values = [new_value] + node.values
                        parent_node = node.parent
                        for idx, item in enumerate(parent_node.values):
                            if item == new_value:
                                parent_node.values[idx] = new_node_pop_value
                                break
                    else:
                        new_node_pop_key = new_node.keys.pop(-1)
                        new_node_pop_value = new_node.values.pop(-1)
                        node.keys = [new_node_pop_key] + node.keys
                        node.values = [new_node_pop_value] + node.values
                        parent_node = node.parent
                        for idx, item in enumerate(parent_node.values):
                            if item == new_value:
                                parent_node.values[idx] = new_node_pop_value
                                break
                else:
                    new_node_pop_key = new_node.keys.pop(0)
                    new_node_pop_value = new_node.values.pop(0)
                    if not node.is_leaf:
                        node.keys = node.keys + [new_node_pop_key]
                        node.values = node.values + [new_value]
                        parent_node = node.parent
                        for idx, item in enumerate(parent_node.values):
                            if item == new_value:
                                parent_node.values[idx] = new_node_pop_value
                                break
                    else:
                        node.keys = node.keys + [new_node_pop_key]
                        node.values = node.values + [new_node_pop_value]
                        parent_node = node.parent
                        for idx, item in enumerate(parent_node.values):
                            if item == new_value:
                                parent_node.values[idx] = new_node.values[0]
                                break

                if not new_node.is_leaf:
                    for key in new_node.keys:
                        key.parent = new_node

                if not node.is_leaf:
                    for key in node.keys:
                        key.parent = node

                if not parent_node.is_leaf:
                    for key in parent_node.keys:
                        key.parent = parent_node

    def delete(self, key, value):
        node = self._search(value)
        for idx, item in enumerate(node.values):
            if item == value:
                if key in node.keys[idx]:
                    if len(node.keys[idx]) > 1:
                        node.keys[idx].pop(node.keys[idx].index(key))
                    elif node == self.root:
                        node.values.pop(idx)
                        node.keys.pop(idx)
                    else:
                        node.keys[idx].pop(node.keys[idx].index(key))
                        del node.keys[idx]
                        node.values.pop(node.values.index(value))
                        self._delete_entry(node, key, value)
                else:
                    return


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
    print(b_plus_tree)
    print(b_plus_tree.search('21', '15'))
    b_plus_tree.delete('33', '5')
    print(b_plus_tree)
