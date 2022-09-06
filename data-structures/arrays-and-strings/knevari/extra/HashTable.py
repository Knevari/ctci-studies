from hashlib import sha256
import queue

# Variables and methods starting with a single _
# are intended to be "private"


class QueueItem:
    def __init__(self, key=None, value=None, priority=1):
        self.key = key
        self.value = value
        self.priority = priority
        self._max_priority = 2 ** 5

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
        return self._heap[node_idx].key == key

    def _swapNodes(self, first_node_idx, second_node_idx):
        self._heap[first_node_idx], self._heap[second_node_idx] =\
            self._heap[second_node_idx], self._heap[first_node_idx]

    def _popLastElement(self):
        self._heap.pop(self.size - 1)

    def _findLargestSubtreeNode(self, tree_root_index):
        largest = tree_root_index

        left = self._getLeftChildIndex(tree_root_index)
        right = self._getRightChildIndex(tree_root_index)

        if left < self.size and self._getNodePriority(tree_root_index) < self._getNodePriority(left):
            largest = left

        if right < self.size and self._getNodePriority(largest) < self._getNodePriority(right):
            largest = right

        return largest

    def _heapify(self, idx):
        largest = self._findLargestSubtreeNode(idx)

        if largest != idx:
            self._swapNodes(largest, idx)
            self._heapify(largest)

    def _incrementSize(self):
        self.size += 1

    def _decrementSize(self):
        self.size -= 1

    def _appendToHeap(self, key, value):
        self._heap.append(QueueItem(key, value, self._starting_items_priority))

    def _recalculateNodesPositions(self):
        for idx in range((self.size // 2) - 1, -1, -1):
            self._heapify(idx)

    # Public Stuff
    def insert(self, key, value):
        if self.size == 0:
            self._appendToHeap(key, value)
        else:
            self._appendToHeap(key, value)
            self._recalculateNodesPositions()

        self._incrementSize()

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

    def is_empty(self):
        return self.size == 0

    def get_queue_as_list(self):
        return self._heap

    def __iter__(self):
        return iter(self._heap)

    def __repr__(self):
        return str(self._heap)


class HashTable:
    def __init__(self, initial_number_of_buckets=200, max_load_factor=0.6, increasing_factor=2):
        self._size = 0
        self._number_of_buckets = initial_number_of_buckets
        self._increasing_factor = increasing_factor
        self._max_load_factor = max_load_factor
        self._createBuckets()

    # Private Stuff
    def _createBuckets(self):
        self._buckets = [PriorityQueue()
                         for _ in range(self._number_of_buckets)]

    def _findBucketByKey(self, key):
        hash = self._hash(key)
        return self._buckets[hash]

    def _findItemInBucketByKey(self, bucket, key):
        for item in bucket:
            if item.key == key:
                return item

        return None

    def _findValueInBucketByKey(self, bucket, key):
        for item in bucket:
            if item.key == key:
                return item.value

        return None

    def _hash(self, value):
        data = repr(value).encode("utf-8")
        return int.from_bytes(sha256(data).digest(), "big") % self._number_of_buckets

    def _incrementSize(self):
        self._size += 1

    def _decrementSize(self):
        self._size -= 1

    def _increaseInternalNumberOfBuckets(self):
        self._number_of_buckets *= self._increasing_factor

    def _checkIfNeedsToReallocate(self):
        if self._getLoadFactor() > self._max_load_factor:
            self._increaseInternalNumberOfBuckets()
            self._reallocateBucketsInternalArray()

    def _reallocateBucketsInternalArray(self):
        old_buckets = self._buckets
        new_buckets = [PriorityQueue() for _ in range(self._number_of_buckets)]
        self._buckets = new_buckets

        for queue in old_buckets:
            if queue.is_empty():
                continue
            for item in queue.get_queue_as_list():
                bucket = self._findBucketByKey(item.key)
                bucket.insert(item.key, item.value)

    def _getLoadFactor(self):
        return self._size / self._number_of_buckets

    # Public Stuff
    def set(self, key, value):
        bucket = self._findBucketByKey(key)

        if self.has(key):
            bucket.update(key, value)
        else:
            bucket.insert(key, value)
            self._incrementSize()

        self._checkIfNeedsToReallocate()

    def get(self, key):
        bucket = self._findBucketByKey(key)
        item = self._findItemInBucketByKey(bucket, key)

        if item:
            item.increasePriority()
            return item.value

        return None

    def has(self, key):
        bucket = self._findBucketByKey(key)

        if self._findValueInBucketByKey(bucket, key) != None:
            return True

        return False

    def delete(self, key):
        bucket = self._findBucketByKey(key)
        bucket.remove(key)
        self._decrementSize()


def main():
    h = HashTable()

    h.set(1, 13)
    h.set(2, 14)
    h.set(3, 15)
    h.delete(2)

    print(h.has(2))  # False
    print(h.has(1))  # True
    print(h.get(1))  # 13

    h.set(2, 22)

    print(h.has(2))  # True
    print(h.get(2))  # 22

    print(h._getLoadFactor())

    h.set(9, 12)
    h.set(10, 12)
    h.set(24, 13)
    h.set(50, 22)

    print(h._getLoadFactor())
    # print(h._buckets)


if __name__ == "__main__":
    main()
