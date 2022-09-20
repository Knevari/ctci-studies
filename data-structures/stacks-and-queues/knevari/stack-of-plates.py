class Stack:
    def __init__(self, max_size=5):
        self.__stack = []
        self.__size = 0
        self.__max_size = max_size

    def get_size(self):
        return self.__size

    def get_max_size(self):
        return self.__max_size

    def peek(self):
        if self.__size > 0:
            return self.__stack[-1]

        return None

    def push(self, value):
        self.__stack.append(value)
        self.__size += 1

    def pop(self):
        element = self.__stack.pop()
        self.__size -= 1
        return element

    def is_empty(self):
        return self.__size == 0

    def __str__(self):
        return str(self.__stack)


class StackOfPlates:
    def __init__(self):
        self.__stacks = [Stack()]
        self.__last_stack = 0

    def __get_stack(self, idx):
        return self.__stacks[idx]

    def __get_last_stack(self):
        return self.__get_stack(self.__last_stack)

    def __create_new_stack(self):
        self.__stacks.append(Stack())
        self.__last_stack += 1

    def __remove_stack(self, idx):
        self.__stacks.pop(idx)
        self.__last_stack -= 1

    def __has_exceeded_capacity(self):
        return self.__last_stack > 0

    def __create_stack_if_max(self):
        stack = self.__get_last_stack()
        if stack.get_size() == stack.get_max_size():
            self.__create_new_stack()

    def peek(self):
        stack = self.__get_last_stack()
        return stack.peek()

    def push(self, value):
        self.__create_stack_if_max()
        stack = self.__get_last_stack()
        stack.push(value)

    def pop_at(self, idx):
        if self.is_empty():
            return None

        stack = self.__get_stack(idx)
        element = stack.pop()

        if stack.is_empty() and not self.is_empty():
            self.__remove_stack(idx)

        return element

    def pop(self):
        return self.pop_at(self.__last_stack)

    def is_empty(self):
        stack = self.__get_last_stack()
        return stack.is_empty() and not self.__has_exceeded_capacity()

    def print_stacks(self):
        for idx, stack in enumerate(self.__stacks):
            print(idx, " - ", str(stack))


def main():
    stack = StackOfPlates()

    # First Stack
    stack.push(2)
    stack.push(3)
    stack.push(7)
    stack.push(10)
    stack.push(20)

    # Second Stack
    stack.push(9)
    stack.push(4)
    stack.push(2)
    stack.push(3)
    stack.push(2)

    # Third Stack
    stack.push(1)
    stack.push(4)
    stack.push(12)
    stack.push(24)
    stack.push(5)

    # Unfilled Fourth Stack
    stack.push(8)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop_at(0))
    print(stack.pop_at(0))
    print(stack.pop())
    print(stack.pop())

    print()

    stack.print_stacks()


if __name__ == "__main__":
    main()
