from LinkedList import LinkedList


class Solution:
    def partition(self, ll: LinkedList, partition: int) -> LinkedList:
        if ll.is_empty():
            return ll

        pl = LinkedList()

        n = ll.head

        while n != None:
            if n.value < partition:
                pl.insert_head(n.value)
            else:
                pl.insert(n.value)

            n = n.next

        return pl


def main():
    l1 = LinkedList()
    l1.insert_many(11, 1, 12, 2, 13, 3, 4, 5, 6)

    l2 = LinkedList()
    l2.insert_many(6, 2, 1, 2, 3, 4, 5)

    solution = Solution()

    l1 = solution.partition(l1, 3)
    l2 = solution.partition(l2, 2)

    print(l1)
    print(l2)


if __name__ == "__main__":
    main()
