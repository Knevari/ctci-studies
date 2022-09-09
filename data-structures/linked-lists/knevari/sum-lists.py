from LinkedList import LinkedList


class Solution:
    def sum_lists(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        if l1.is_empty():
            return l2

        if l2.is_empty():
            return l1

        n1 = l1.head
        n2 = l2.head

        result = LinkedList()
        carry = 0

        while n1 != None and n2 != None:
            v1 = n1.value
            v2 = n2.value

            print(v1, v2)

            s = v1 + v2 + carry
            digit = s % 10
            carry = s // 10

            result.insert(digit)

            n1 = n1.next
            n2 = n2.next

        while n1 != None:
            result.insert(n1.value + carry)
            carry = 0
            n1 = n1.next

        while n2 != None:
            result.insert(n2.value + carry)
            carry = 0
            n2 = n2.next

        return result


def main():
    solution = Solution()

    n1 = LinkedList()
    n2 = LinkedList()
    n1.insert_many(0, 0, 0, 1)
    n2.insert_many(0, 0, 0, 0, 0, 0, 2)

    print(solution.sum_lists(n1, n2))


if __name__ == "__main__":
    main()

617 + 295

12
