from hashlib import sha256

# Variables and methods starting with a single _
# are intended to be "private"


class QueueItem:
    def __init__(self, key=None, value=None, priority=1):
        self.key = key
        self.value = value
        self.priority = priority
        self._max_priority = 2 ** 6

    def increasePriority(self):
        self.priority = min(self._max_priority, self.priority + 1)

    def decreasePriority(self):
        self.priority = max(0, self.priority + 1)

    def __repr__(self):
        return "{} - {}".format(str(self.value), str(self.priority))


class PriorityQueue:
    def __init__(self):
        self._heap: list(QueueItem) = []
        self._starting_items_priority = 1
        self.size = 0

    # Private Stuff
    def _getLeftChildIndex(self, node_idx):
        return 2 * node_idx + 1

    def _getRightChildIndex(self, node_idx):
        return 2 * node_idx + 2

    def _getNodeKey(self, node_idx):
        return self._heap[node_idx].key

    def _getNodeValue(self, node_idx):
        return self._heap[node_idx].value

    def _getNodePriority(self, node_idx):
        return self._heap[node_idx].priority

    def _updateNodeKey(self, node_idx, key):
        self._heap[node_idx].key = key

    def _updateNodeValue(self, node_idx, value):
        self._heap[node_idx].value = value

    def _findNodeByKey(self, key):
        idx = 0

        for idx in range(self.size):
            if self._compareNodesKeys(idx, key):
                return idx

        return -1

    def _increaseNodePriority(self, node_idx):
        self._heap[node_idx].increasePriority()

    def _compareNodesKeys(self, node_idx, key):
        self._heap[node_idx].key == key

    def _swapNodes(self, first_node_idx, second_node_idx):
        self._heap[first_node_idx], self._heap[second_node_idx] =\
            self._heap[second_node_idx], self._heap[first_node_idx]

    def _popLastElement(self):
        self._heap.pop(self.size - 1)

    def _heapify(self, idx):
        largest = idx

        left = self._getLeftChildIndex(idx)
        right = self._getRightChildIndex(idx)

        if left < self.size and self._getNodePriority(idx) < self._getNodePriority(left):
            largest = left

        if right < self.size and self._getNodePriority(largest) < self._getNodePriority(right):
            largest = right

        if largest != idx:
            self._swapNodes(largest, idx)
            self._heapify(largest)

    def _incrementSize(self):
        self.size += 1

    def _decrementSize(self):
        self.size -= 1

    def _appendToHeap(self, key, value):
        self._heap.append(QueueItem(key, value, self._starting_items_priority))

    # Public Stuff
    def insert(self, key, value):
        if self.size == 0:
            self._appendToHeap(key, value)
        else:
            self._appendToHeap(key, value)
            self._recalculateNodesPositions()

        self._incrementSize()

    def _recalculateNodesPositions(self):
        for idx in range((self.size // 2) - 1, -1, -1):
            self._heapify(idx)

    def update(self, key, value):
        for idx in range(self.size):
            if self._compareNodesKeys(idx, key):
                self._updateNodeValue(idx, value)
                self._increaseNodePriority(idx)
                self._recalculateNodesPositions()
                return True

            return False

    def remove(self, key):
        idx = self._findNodeByKey(key)

        if idx != -1:
            self._swapNodes(idx, self.size - 1)
            self._popLastElement()
            self._decrementSize()
            self._recalculateNodesPositions()

    def __iter__(self):
        return iter(self._heap)

    def __repr__(self):
        return str(self._heap)


class HashTable:
    def __init__(self, initial_size=1, growing_limit=100, increasing_factor=2):
        self._size = 0
        self._capacity = initial_size
        self._increasing_factor = increasing_factor
        self._growing_limit = growing_limit
        self._createBuckets()

    # Private Stuff
    def _createBuckets(self):
        self._buckets = [PriorityQueue() for _ in range(self._capacity)]

    def _hash(self, value):
        data = repr(value).encode("utf-8")
        return int.from_bytes(sha256(data).digest(), "big") % self._capacity

    def _incrementSize(self):
        self._size += 1

    # Public Stuff
    def set(self, key, value):
        hash = self._hash(key)

        if self.has(key):
            self._buckets[hash].update(key, value)
        else:
            self._buckets[hash].insert(key, value)
            self._incrementSize()

    def get(self, key):
        hash = self._hash(key)

        bucket = self._buckets[hash]

        for item in bucket:
            if item.key == key:
                return item.value

        return None

    def has(self, key):
        hash = self._hash(key)

        bucket = self._buckets[hash]

        for item in bucket:
            if item.key == key:
                return True

        return False

    def delete(self, key):
        hash = self._hash(key)
        bucket = self._buckets[hash]
        bucket.remove(key)


def main():
    h = HashTable()
    h.set("a", "b")
    h.set("a", 13)
    h.set(1, 15)
    h.set(1, 16)
    h.set(1, 17)
    # h.delete(1)
    print(h._buckets)
    print(h._size)
    print(h.get("a"), h.get(1))


if __name__ == "__main__":
    main()
