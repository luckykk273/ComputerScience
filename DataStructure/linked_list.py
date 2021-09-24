

class ListNode:
    def __init__(self, data, next_=None):  # Because next is the built-in name, so we add underscore after next;
        self.data = data
        assert next_ is None or isinstance(next_, ListNode), 'next_ parameter can only accept ListNode.'
        self.next = next_


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        length = 0

        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length

    def __str__(self):
        str_buff = ''
        current_node = self.head

        while current_node is not None:
            str_buff = str_buff + str(current_node.data) + '->'
            current_node = current_node.next

        str_buff += 'null'

        return str_buff

    def access(self, index):
        """
            Time complexity:
                Average: theta(n)
                Worst:   O(n)
        """
        assert self.head is not None, 'List is empty!'
        assert index > -1, 'Index must start from 0!'

        current_node = self.head  # virtual index 0
        while current_node.next is not None and index > 0:
            index -= 1
            current_node = current_node.next

        # Because we do not know if the index is greater than the singly linked list.
        return current_node if index == 0 else None

    def search(self, value):
        """
            Search the list node by value;

            Time complexity:
                Average: theta(n)
                Worst:   O(n)
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                # return current_node
                return True  # Return node or value not equal to -1 are both okay;

            current_node = current_node.next

        return False

    def insert(self, index, value):
        """
        Note that the pure insertion time is exactly O(1).
        But before we insert it, we have to search that position to insert.
        (The search time is O(n).)

        Time complexity:
            Average: theta(1)
            Worst:   O(1)
        """
        assert -1 < index < len(self), 'Out of bound!'
        assert self.head is not None, 'The list is null!'

        new_node = ListNode(value)
        current_node = self.head  # virtual index 0
        for _ in range(index-1):
            current_node = current_node.next

        if index == 0:  # Because index 0 means self.head, so here we handle it in other control flow.
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def append(self, value):
        """
            Always append the value to the tail of singly linked list;

            Time complexity:
                Average: theta(n)
                Worst:   O(n)
        """
        if self.head is None:
            self.head = ListNode(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = ListNode(value)

    def delete(self, index: int):
        """
            Note that the pure deletion time is exactly O(1).
            But before we delete it, we have to search that position to delete.
            (The search time is O(n).)

            Time complexity:
                Average: theta(1)
                Worst:   O(1)
        """
        assert -1 < index < len(self), 'Out of bound!'
        assert self.head is not None, 'The list is null!'

        current_node = self.head  # virtual index 0
        for _ in range(index - 1):
            current_node = current_node.next

        if index == 0:
            self.head = None if len(self) == 1 else self.head.next
        else:
            current_node.next = current_node.next.next


class DoublyListNode(ListNode):
    def __init__(self, data, next_=None, prev=None):
        super(DoublyListNode, self).__init__(data=data, next_=next_)
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        length = 0

        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length

    def __str__(self):
        str_buff = ''
        current_node = self.head

        while current_node.next is not None:
            str_buff = str_buff + str(current_node.data) + '<->'
            current_node = current_node.next

        str_buff = 'null<-' + str_buff + str(current_node.data) + '->null'

        return str_buff

    def access(self, index):
        """
            Time complexity:
                Average: theta(n)
                Worst:   O(n)
        """
        assert index > -1, 'Index must start from 0!'

        current_node = self.head  # virtual index 0
        while current_node.next is not None and index > 0:
            index -= 1
            current_node = current_node.next

        # Because we do not know if the index is greater than the singly linked list.
        return current_node if index == 0 else None

    def search(self, value):
        """
            Search the list node by value;

            Time complexity:
                Average: theta(n)
                Worst:   O(n)
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                # return current_node
                return True  # Return node or value not equal to -1 are both okay;

            current_node = current_node.next

        return False

    def insert(self, index, value):
        """
        Note that the pure insertion time is exactly O(1).
        But before we insert it, we have to search that position to insert.
        (The search time is O(n).)

        Time complexity:
            Average: theta(1)
            Worst:   O(1)
        """
        assert -1 < index < len(self), 'Out of bound!'
        assert self.head is not None, 'The list is null!'

        new_node = DoublyListNode(value)
        current_node = self.head  # virtual index 0
        for _ in range(index - 1):
            current_node = current_node.next

        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == len(self) - 1:
            current_node.next = new_node
            new_node.prev = current_node
        else:
            current_node.next.prev = new_node
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next = new_node

    def append(self, value):
        """
            Always append the value to the tail of doubly linked list;

            Time complexity:
                Average: theta(n)
                Worst:   O(n)
        """
        if self.head is None:
            self.head = DoublyListNode(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = DoublyListNode(data=value, next_=None, prev=current_node)

    def delete(self, index: int):
        """
            Note that the pure deletion time is exactly O(1).
            But before we delete it, we have to search that position to delete.
            (The search time is O(n).)

            Time complexity:
                Average: theta(1)
                Worst:   O(1)
        """
        assert -1 < index < len(self), 'Out of bound!'
        assert self.head is not None, 'The list is null!'

        current_node = self.head  # virtual index 0
        for _ in range(index - 1):
            current_node = current_node.next

        if index == 0:
            if len(self) == 1:
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
        elif index == len(self) - 1:
            current_node.next = None
        else:
            current_node.next.next.prev = current_node
            current_node.next = current_node.next.next


def singly_test():
    singly_linked_list = SinglyLinkedList()
    for i in range(5):
        singly_linked_list.append(value=i+1)
    print('Initialized singly linked list is:', singly_linked_list)
    singly_linked_list.insert(index=2, value=100)
    print('After insertion:', singly_linked_list)
    print('The value of the index 3 is:', singly_linked_list.access(index=3).data)
    print('The search result is:', singly_linked_list.search(value=77))
    singly_linked_list.delete(index=5)
    print('After deletion:', singly_linked_list)


def doubly_test():
    doubly_linked_list = DoublyLinkedList()
    for i in range(5):
        doubly_linked_list.append(value=i+1)
    print('Initialized doubly linked list is:', doubly_linked_list)
    doubly_linked_list.insert(index=0, value=100)
    print('After insertion:', doubly_linked_list)
    print('The value of the index 3 is:', doubly_linked_list.access(index=3).data)
    print('The search result is:', doubly_linked_list.search(value=77))
    doubly_linked_list.delete(index=5)
    print('After deletion:', doubly_linked_list)


if __name__ == '__main__':
    doubly_test()
