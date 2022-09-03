class ArrayList:
    def __init__(self, type, size):
        self.size = 0
        self.type = type
        self.capacity = size
        self._allocateNewArray()

    # Internal helpers and private functions
    def _increaseInternalCapacity(self):
        self.capacity *= 2
        self._allocateNewArray()

    def _increaseInternalCapacityIfNotEnoughSpace(self):
        if self.size + 1 > self.capacity:
            self._increaseInternalCapacity()

    def _increaseInternalCapacityWhileNotEnoughSpace(self, requiredSpace):
        while self.size + requiredSpace > self.capacity:
            self._increaseInternalCapacity()

    def _shiftElementsByAmount(self, amount):
        for idx in range(self.size-1, -1, -1):
            self.array[idx + amount] = self.array[idx]
            self.array[idx] = self.type()

    def _allocateEmptyArrayIfNone(self):
        if not hasattr(self, 'array'):
            self.array = []

    def _allocateNewArray(self):
        self._allocateEmptyArrayIfNone()

        # Create new array
        new_array = [self.type() for _ in range(self.capacity)]

        # Copy old values to new array
        for idx, value in enumerate(self.array):
            new_array[idx] = value

        # Update pointers
        self.array = new_array

    def _incrementSize(self):
        self.size += 1

    def _searchThroughArray(self, value):
        for idx in range(self.size):
            if value == self.array[idx]:
                return True
        return False

    def _validateValueType(self, value):
        if self.type != type(value):
            raise Exception(
                "'{}' cannot be added to ArrayList of type {}".format(value, self.type))

    def _shift(self, amount):
        self._increaseInternalCapacityWhileNotEnoughSpace(amount)
        self._shiftElementsByAmount(amount)

    def _insertAtFirstPosition(self, value):
        self._shift(1)
        self.array[0] = value

    # Public shit
    def is_empty(self):
        return self.size == 0

    def has(self, value):
        return self._searchThroughArray(value)

    def append(self, value):
        self._validateValueType(value)
        self._increaseInternalCapacityIfNotEnoughSpace()
        self._incrementSize()
        self.array[self.size-1] = value

    def prepend(self, value):
        if self.is_empty():
            return self.append(value)

        self._validateValueType(value)
        self._increaseInternalCapacityIfNotEnoughSpace()
        self._incrementSize()
        self._insertAtFirstPosition(value)

    def __str__(self):
        return str(self.array[:self.size])

    def __len__(self):
        return self.size

    def __iter__(self):
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration < self.size:
            next_val = self.array[self.iteration]
            self.iteration += 1
            return next_val
        else:
            raise StopIteration


def main():
    # Test my ArrayList
    arrList = ArrayList(int, 2)
    arrList.append(2)
    arrList.prepend(3)
    arrList.prepend(4)
    arrList.append(7)
    arrList.append(2)

    print("""\n
      - ArrayList

        Final Size: {}
        Final Capacity: {}
        Final Readable Values: {}
        Entire Thing: {}
        Was able to search for value: {}
    """.format(
        len(arrList),
        arrList.capacity,
        str(arrList),
        str(arrList.array),
        arrList.has(3)
    ))


if __name__ == "__main__":
    main()
