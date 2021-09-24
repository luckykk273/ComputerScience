import random


class ListNode:
    def __init__(self, data=None, level=0):
        self.data = data
        self.next = [None]*level  # Store the node pointers which point to the next node in every level;


class SkipList:
    def __init__(self):
        self.head = ListNode()
        self.length = 0
        self.max_level = 0

    def __len__(self):
        length = 0
        dummy = self.head

        while dummy.next[0] is not None:
            length += 1
            dummy = dummy.next[0]

        return length

    def __str__(self):
        str_buff = ''
        for level in range(len(self.head.next)-1, -1, -1):
            dummy = self.head
            while dummy.next[level] is not None:
                str_buff += str(dummy.next[level].data)
                dummy = dummy.next[level]
            str_buff += '\n'

        return str_buff

    @staticmethod
    def random_level():
        level = 1
        while random.random() < 0.5:
            level += 1

        return level

    def update_list(self, data):
        """
            Find out the greatest element which is smaller than the data in every level;
            Save into update list for the convenience of insertion and deletion;
        """
        update = [None]*self.max_level
        dummy = self.head

        for i in reversed(range(self.max_level)):
            while dummy.next[i] is not None and dummy.next[i].data < data:
                dummy = dummy.next[i]

            update[i] = dummy

        return update

    def search(self, data, update=None):
        if update is None:
            update = self.update_list(data)

        candidate = update[0].next[0] if len(update) > 0 else None
        return candidate.data if (candidate is not None) and (candidate.data == data) else None

    def insert(self, data):
        new_node = ListNode(data, self.random_level())

        self.max_level = max(self.max_level, len(new_node.next))
        while len(self.head.next) < len(new_node.next):
            self.head.next.append(None)

        update = self.update_list(data)
        if self.search(data, update) is None:
            for i in range(len(new_node.next)):
                new_node.next[i] = update[i].next[i]
                update[i].next[i] = new_node

    def delete(self, data):
        update = self.update_list(data)
        target_node = self.search(data, update)
        if target_node is not None:
            for i in reversed(range(len(target_node.next))):
                update[i].next[i] = target_node.next[i]
                if self.head.next[i] is None:
                    self.max_level -= 1


if __name__ == '__main__':
    skip_list = SkipList()
    skip_list.insert(1)
    print(skip_list)
    skip_list.insert(6)
    print(skip_list)
    skip_list.insert(3)
    print(skip_list)
