from hashlib import sha256
from queue import PriorityQueue

# Variables and methods starting with a single _
# are intended to be "private"


class QueueItem:
    def __init__(self, key=None, value=None, priority=1):
        self.key = key
        self.value = value
        self.priority = priority

    def increasePriority(self):
        self.priority += 1

    def decreasePriority(self):
        self.priority -= 1

    def __repr__(self):
        return "{} - {}".format(str(self.value), str(self.priority))


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._starting_items_priority = 1
        self.size = 0

    def _heapify(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self._heap[idx].priority < self._heap[left].priority:
            largest = left

        if right < self.size and self._heap[largest].priority < self._heap[right].priority:
            largest = right

        if largest != idx:
            self._heap[idx], self._heap[largest] = self._heap[largest], self._heap[idx]
            self._heapify(largest)

    def _incrementSize(self):
        self.size += 1

    def _decrementSize(self):
        self.size -= 1

    def insert(self, key, value):
        if self.size == 0:
            self._heap.append(
                QueueItem(key, value, self._starting_items_priority))
        else:
            print("key ", key, " value ", value)
            self._heap.append(
                QueueItem(key, value, self._starting_items_priority))
            for i in range((self.size // 2) - 1, -1, -1):
                self._heapify(i)

        self._incrementSize()

    def update(self, key, value):
        for idx in range(self.size):
            if self._heap[idx].key == key:
                self._heap[idx].value = value
                self._heap[idx].increasePriority()

                for i in range((self.size // 2) - 1, -1, -1):
                    self._heapify(i)
                return True

            return False

    def remove(self, key):
        idx = 0

        for idx in range(self.size):
            if key == self._heap[idx].key:
                break

        self._heap[idx], self._heap[self.size - 1] = \
            self._heap[self.size - 1], self._heap[idx]

        self._heap.pop(self.size - 1)

        for i in range((self.size // 2) - 1, -1, -1):
            self._heapify(i)

        self._decrementSize()

    def __iter__(self):
        return iter(self._heap)

    def __repr__(self):
        return str(self._heap)


class HashTable:
    def __init__(self, initial_size=1, growing_limit=100):
        self._size = 0
        self._capacity = initial_size
        self._increasing_factor = 2
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
    pass


if __name__ == "__main__":
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
