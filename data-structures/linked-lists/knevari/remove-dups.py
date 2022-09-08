from LinkedList import LinkedList


class Solution:
    def remove_dups(self, ll: LinkedList) -> LinkedList:
        """
        This algorithm requires 2 passes through the linked list,
        since we need to know at least the positions of each element to remove
        """
        if ll.is_empty():
            return ll

        found_dups = set()

        node = ll.head
        found_dups.add(node.value)

        while node.next != None:
            if node.next.value in found_dups:
                node.next = node.next.next
            else:
                found_dups.add(node.next.value)
                node = node.next

        return ll


def main():
    l1 = LinkedList()
    l1.insertMany(7, 7, 7, 8)

    l2 = LinkedList()
    l2.insertMany(1, 2, 3, 4, 2, 3, 2, 7)

    solution = Solution()
    solution.remove_dups(l1)
    solution.remove_dups(l2)

    print(l1)
    print(l2)


if __name__ == "__main__":
    main()
