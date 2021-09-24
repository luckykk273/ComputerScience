"""
Generally, people use array or linked list to implement queue;
So the time complexity will be determined by which data structure is used.
"""

from collections.abc import Iterable

from DataStructure.linked_list import SinglyLinkedList


class ArrayQueue:
    def __init__(self):
        self.queue = []  # We simply use built-in list as an array here;

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

    @property
    def is_empty(self):
        return len(self) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty:
            return None
        else:
            first_element = self.queue[0]
            self.queue = self.queue[1:]
            return first_element

    def peek(self):
        return None if self.is_empty else self.queue[0]


class LinkedListQueue:
    def __init__(self):
        """
        Here we use the SinglyLinkedList class defined by myself.
        Because of some assertions checking the bound, there are some error if you touch the bound.
        Feel free to change the assertions to the if-else condition to avoid error occurring.
        """
        self.queue = SinglyLinkedList()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

    def enqueue(self, data):
        if self.queue.head is None:
            self.queue.append(data)
        else:
            self.queue.insert(len(self.queue)-1, data)

    def dequeue(self):
        first_element = self.queue.access(len(self.queue)-1)
        self.queue.delete(len(self.queue)-1)
        return first_element.data


def array_queue_test():
    queue = ArrayQueue()
    print('Initial queue is:', queue)
    for i in range(4, 6):
        queue.enqueue(i)
        print('After enqueue:', queue)
    for i in range(len(queue)):
        print('The first-in element is:', queue.dequeue())
        print('After dequeue:', queue)


def linked_list_queue_test():
    queue = LinkedListQueue()
    print('Initial queue is:', queue)
    for i in range(4, 6):
        queue.enqueue(i)
        print('After enqueue:', queue)
    print('After enqueue:', queue)
    for i in range(len(queue)+1):
        print('The first-in element is:', queue.dequeue())
        print('After dequeue:', queue)


if __name__ == '__main__':
    array_queue_test()
    print('================')
    linked_list_queue_test()
