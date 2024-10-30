class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        result = self._search_recursive(self.root, key)
        if result:
            print(f"{key} found in BST.")
        else:
            print(f"{key} not found in BST.")

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        if self.root is None:
            print(f"{key} not found in BST.")
            return self.root
        self.root, deleted = self._delete_recursive(self.root, key)
        if deleted:
            print(f"{key} deleted.")
        else:
            print(f"{key} not found in BST.")

    def _delete_recursive(self, node, key):
        if node is None:
            return node, False

        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted

        if node.left is None:
            return node.right, True
        elif node.right is None:
            return node.left, True

        temp = self._min_value_node(node.right)
        node.key = temp.key
        node.right, _ = self._delete_recursive(node.right, temp.key)
        return node, True

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
        return result


def bst_program():
    bst = BinarySearchTree()
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter value to insert: "))
            bst.insert(key)
            print(f"{key} inserted.")
        elif choice == 2:
            key = int(input("Enter value to delete: "))
            bst.delete(key)
        elif choice == 3:
            key = int(input("Enter value to search: "))
            bst.search(key)
        elif choice == 4:
            print("In-order Traversal:", bst.inorder())
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

bst_program()
