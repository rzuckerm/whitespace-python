from .error import StackEmptyError, StackIndexError


class Stack:
    def __init__(self, name=None):
        self.name = name
        self._elements = []

    def empty(self):
        return not self._elements

    def push(self, x):
        self._elements.append(x)

    def pop(self):
        if self.empty():
            raise StackEmptyError(self.name)

        return self._elements.pop()

    def top(self):
        if self.empty():
            raise StackEmptyError(self.name)

        return self._elements[-1]

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, key):
        if key < 0:
            raise StackIndexError(self.name)

        idx = len(self) - key - 1
        if idx < 0:
            raise StackIndexError(self.name)

        return self._elements[idx]
