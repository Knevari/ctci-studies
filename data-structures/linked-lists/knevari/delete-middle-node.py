from LinkedList import LinkedList, Node


class Solution:
    def delete_middle_node(self, node: Node) -> None:
        while node and node.next != None:
            node.value = node.next.value
            node.next = node.next.next
            node = node.next


def main():
    l1 = LinkedList()
    l1.insertMany(1, 5, 9, 12)

    l2 = LinkedList()
    l2.insertMany(6, 2, 1, 2, 3, 4, 5)

    solution = Solution()

    n1 = l1.head.next.next
    n2 = l2.head.next.next.next

    solution.delete_middle_node(n1)
    solution.delete_middle_node(n2)

    print(l1)
    print(l2)


if __name__ == "__main__":
    main()
