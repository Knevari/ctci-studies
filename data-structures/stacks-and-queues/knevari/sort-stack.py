from Stack import Stack


class Solution:
    def sort_stack(self, stack: Stack) -> None:
        if stack.is_empty():
            return

        temp = Stack()

        while not stack.is_empty():
            curr = stack.pop()

            while not temp.is_empty() and temp.peek() > curr:
                stack.push(temp.pop())

            temp.push(curr)

        while not temp.is_empty():
            stack.push(temp.pop())


def main():
    solution = Solution()

    ss = Stack()
    ss.push(36, 49, 72, 1, 12, 2)

    print(ss)
    solution.sort_stack(ss)
    print(ss)


if __name__ == "__main__":
    main()
