from LinkedList import LinkedList


class Solution:
    def kth_to_last(self, ll: LinkedList, k: int) -> LinkedList:
        if ll.is_empty():
            return -1

        n2 = ll.head
        while k - 1 > 0:
            n2 = n2.next

            if n2 == None:
                return -1

            k -= 1

        n1 = ll.head

        while n2.next != None:
            n1 = n1.next
            n2 = n2.next

        return n1.value


def main():
    l1 = LinkedList()
    l1.insertMany(7, 2, 7, 8)

    l2 = LinkedList()
    l2.insertMany(1, 2, 3, 4, 5, 6, 7, 8)

    solution = Solution()
    print(solution.kth_to_last(l1, 3))  # 2
    print(solution.kth_to_last(l2, 3))  # 6


if __name__ == "__main__":
    main()
