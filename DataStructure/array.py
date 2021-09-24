from collections.abc import Iterable


class Array:
    def __init__(self, init):
        if isinstance(init, Iterable):
            self.elements = list(init)
        else:
            raise TypeError('Try to initialize Array with non-iterable object.')

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)

    def access(self, index):
        """
            Time complexity:
                Average: theta(1)
                Worst:   O(1)
        """
        assert -1 < index < len(self), 'Out of bound!'

        return self.elements[index]

    def search(self, value):
        """
            Time complexity:
                Average: theta(n)
                Worst:   O(n)
        """
        for i in range(len(self.elements)):
            if self.elements[i] == value:
                return i

        return -1  # if not found;

    def insert(self, index, value):
        """
        Time complexity:
            Average: theta(n)
            Worst:   O(n)
        """
        assert -1 < index < len(self), 'Out of bound!'

        self.elements.append(0)
        for i in range(len(self.elements)-1, index, -1):
            self.elements[i] = self.elements[i-1]

        self.elements[index] = value

    def delete(self, index):
        """
        Time complexity:
            Average: theta(n)
            Worst:   O(n)
        """
        assert -1 < index < len(self), 'Out of bound!'

        for i in range(index, len(self.elements)-1):
            self.elements[i] = self.elements[i+1]

        self.elements = self.elements[:-1]


if __name__ == '__main__':
    array = Array([1, 2, 3, 4, 5])
    print('The value of index 3 is:', array.access(index=3))
    print('The index of value 3 is:', array.search(value=3))
    array.insert(index=3, value=100)
    print('After insert value 100 to index 3:', array)
    array.delete(index=3)
    print('After delete the value of index 3:', array)
