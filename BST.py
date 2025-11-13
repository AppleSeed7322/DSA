# Binary Search Tree Implementation
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or key == root.key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: Get inorder successor
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

if __name__ == "__main__":
    tree = BST()
    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display Inorder")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            tree.root = tree.insert(tree.root, val)

        elif choice == '2':
            val = int(input("Enter value to delete: "))
            tree.root = tree.delete(tree.root, val)

        elif choice == '3':
            val = int(input("Enter value to search: "))
            result = tree.search(tree.root, val)
            print(f"✅ {val} found in BST." if result else f"❌ {val} not found.")

        elif choice == '4':
            print("📋 BST in Inorder Traversal: ", end='')
            tree.inorder(tree.root)
            print()

        elif choice == '5':
            print("👋 Exiting program...")
            break

        else:
            print("⚠️ Invalid choice! Please enter a number from 1 to 5.")
