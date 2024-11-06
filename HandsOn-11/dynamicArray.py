class DynamicArray:
    def __init__(self, initial_capacity=2):
        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * self._capacity

    def _resize(self):
        # Double the capacity
        self._capacity *= 2
        new_data = [None] * self._capacity

        # Copy elements to the new array
        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data

    def add(self, value):
        if self._size == self._capacity:  # If the array is full, resize it
            self._resize()
        self._data[self._size] = value
        self._size += 1

    def get(self, index):
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError("Index out of range")

    def get_size(self):
        return self._size

    def get_capacity(self):
        return self._capacity

    def __str__(self):
        # String representation of the array's current elements
        return str([self._data[i] for i in range(self._size)])


if __name__ == "__main__":
    arr = DynamicArray()

    # Adding elements to the dynamic array
    for i in range(10):
        arr.add(i)
        print(f"Added {i}, Size: {arr.get_size()}, Capacity: {arr.get_capacity()}")

    # Retrieving elements from the array
    for i in range(arr.get_size()):
        print(f"Element at index {i}: {arr.get(i)}")

    # Attempting to access an out-of-bounds index
    try:
        print(f"Element at index 20: {arr.get(20)}")
    except IndexError as e:
        print(e)
