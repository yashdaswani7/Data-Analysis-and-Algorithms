class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity
        self.top = -1

    def push(self, value):
        if self.top == self.capacity - 1:
            print("Stack overflow!")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack underflow!")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            print("Stack is empty!")
            return None
        return self.stack[self.top]

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            print("Queue overflow!")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue underflow!")
            return None
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def front_element(self):
        if self.size == 0:
            print("Queue is empty!")
            return None
        return self.queue[self.front]

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:

# Stack operations
stack = Stack(5)
stack.push(10)
stack.push(20)
print("Popped from stack:", stack.pop())  # Output: 20

# Queue operations
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
print("Dequeued from queue:", queue.dequeue())  # Output: 10

# Singly Linked List operations
linked_list = SinglyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.display()  # Output: 10 -> 20 -> None
