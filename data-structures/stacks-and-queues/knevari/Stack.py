class Stack:
    def __init__(self):
        self.__stack = []

    def peek(self):
        return self.__stack[-1]

    def push(self, *values):
        self.__stack.extend(values)

    def pop(self):
        return self.__stack.pop()

    def is_empty(self):
        return len(self.__stack) == 0

    def __str__(self):
        return str(self.__stack)
