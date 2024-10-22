class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        target_node = self.search(key)
        if not target_node:
            return
        if target_node.prev:
            target_node.prev.next = target_node.next
        else:
            self.head = target_node.next
        if target_node.next:
            target_node.next.prev = target_node.prev
        else:
            self.tail = target_node.prev

    def display(self):
        current = self.head
        while current:
            print(f"[{current.key}: {current.value}]", end=" ")
            current = current.next
        print()

class HashMap:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.load_threshold = 0.75
        self.shrink_threshold = 0.25
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]

    # Multiplicative hash function
    def compute_hash(self, key):
        multiplier = 0.618033  # Golden ratio minus 1
        fractional = (key * multiplier) % 1
        return int(self.capacity * fractional) % self.capacity

    def insert(self, key, value):
        bucket_index = self.compute_hash(key)
        existing_node = self.buckets[bucket_index].search(key)
        if existing_node:
            existing_node.value = value  # Update value if key exists
        else:
            self.buckets[bucket_index].append(key, value)
            self.size += 1
            # Resize if load factor exceeds the threshold
            if self.size / self.capacity > self.load_threshold:
                self.resize(self.capacity * 2)

    def retrieve(self, key):
        bucket_index = self.compute_hash(key)
        target_node = self.buckets[bucket_index].search(key)
        if target_node:
            return target_node.value
        else:
            raise KeyError("Key not found in the hash table.")

    def remove(self, key):
        bucket_index = self.compute_hash(key)
        self.buckets[bucket_index].delete(key)
        self.size -= 1
        # Shrink if size falls below the shrink threshold
        if self.capacity > 4 and self.size / self.capacity < self.shrink_threshold:
            self.resize(self.capacity // 2)

    def resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def show(self):
        for idx, bucket in enumerate(self.buckets):
            print(f"Bucket {idx}: ", end="")
            bucket.display()

def main_menu():
    hash_map = HashMap()
    while True:
        print("\nHash Map Operations:")
        print("1. Add/Update Entry")
        print("2. Get Value by Key")
        print("3. Delete Key")
        print("4. Display Hash Map")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            key = int(input("Enter key to add/update: "))
            value = int(input("Enter value: "))
            hash_map.insert(key, value)
            print(f"Entry ({key}, {value}) added/updated.")
        
        elif choice == '2':
            key = int(input("Enter key to retrieve value: "))
            try:
                value = hash_map.retrieve(key)
                print(f"Value associated with key {key}: {value}")
            except KeyError:
                print("Error: Key not found.")
        
        elif choice == '3':
            key = int(input("Enter key to delete: "))
            hash_map.remove(key)
            print(f"Key {key} deleted.")
        
        elif choice == '4':
            print("Hash Map:")
            hash_map.show()
        
        elif choice == '5':
            print("Exiting program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()