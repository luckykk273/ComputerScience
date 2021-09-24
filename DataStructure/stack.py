"""
Generally, people use array or linked list to implement stack;
So the time complexity will be determined by which data structure is used.
"""

from collections.abc import Iterable

from DataStructure.linked_list import SinglyLinkedList


class ArrayStack:
    def __init__(self, init):
        self.stack = []  # We simply use built-in list as an array here;
        if isinstance(init, Iterable):
            self.stack = list(init)
        else:
            raise TypeError('Try to initialize Array with non-iterable object.')

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    @property
    def is_empty(self):
        return len(self) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty:
            return None
        else:
            last_element = self.stack[-1]
            self.stack = self.stack[:-1]
            return last_element


class LinkedListStack:
    def __init__(self):
        """
        Here we use the SinglyLinkedList class defined by myself.
        Because of some assertions checking the bound, there are some error if you touch the bound.
        Feel free to change the assertions to the if-else condition to avoid error occurring.
        """
        self.stack = SinglyLinkedList()

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if self.stack.head is None:
            self.stack.append(data)
        else:
            self.stack.insert(0, data)

    def pop(self):
        last_element = self.stack.access(0)
        self.stack.delete(0)
        return last_element.data


def array_stack_test():
    stack = ArrayStack([1, 2, 3])
    print('Initial stack is:', stack)
    for i in range(4, 6):
        stack.push(i)
        print('After pushing:', stack)
    for i in range(len(stack)):
        print('The last-in element is:', stack.pop())
        print('After popping:', stack)


def linked_list_stack_test():
    stack = LinkedListStack()
    print('Initial stack is:', stack)
    for i in range(4, 6):
        stack.push(i)
    print('After pushing:', stack)
    for i in range(len(stack)+1):
        print('The last-in element is:', stack.pop())
        print('After popping:', stack)


if __name__ == '__main__':
    array_stack_test()
    print('================')
    linked_list_stack_test()
