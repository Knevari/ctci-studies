# I wrote this while drunk, sorry in advance..
class Node:
    def __init__(self, value, next=None) -> None:
        self.value: any = value
        self.next: Node = next


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    # Private methods
    def _insertNewHead(self, node):
        self.head = node
        self.tail = node

    def _headEqualsTail(self):
        return self.head == self.tail

    def _insertNewTail(self, node: Node):
        if self._headEqualsTail():
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def _deleteHead(self):
        if self._headEqualsTail():
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def _updateReferenceToNextNode(self, node: Node):
        node.next = node.next.next

    def _createStringRepresentation(self):
        s = []
        for val in self:
            s.append(val)
        return ", ".join(s)

    # Public methods
    def is_empty(self):
        return self.head == None and self.tail == None

    def insert(self, value: any):
        new_node = Node(value)

        if self.is_empty():
            return self._insertNewHead(new_node)

        self._insertNewTail(new_node)

    def delete(self, value):
        if self.head.value == value:
            self._deleteHead()

        node = self.head

        while node.next != None:
            if node.next.value == value:
                self._updateReferenceToNextNode(node)
                return
            else:
                node = node.next

    # Magic Methods
    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node != None:
            result = self.current_node.value
            self.current_node = self.current_node.next
            return result
        else:
            raise StopIteration

    def __str__(self):
        return self._createStringRepresentation()


def main():
    l = LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.delete(5)

    for val in l:
        print(val)


if __name__ == "__main__":
    main()
