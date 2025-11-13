# Hash Table Implementation using Chaining

size = 10
hash_table = [[] for _ in range(size)]

def hash_func(key):
    return key % size

def insert(key, value):
    bucket = hash_table[hash_func(key)]
    for pair in bucket:
        if pair[0] == key:
            pair[1] = value
            print(f"✅ Key {key} updated with value '{value}'.")
            return
    bucket.append([key, value])
    print(f"✅ Inserted ({key}, '{value}') successfully.")

def delete(key):
    bucket = hash_table[hash_func(key)]
    for pair in bucket:
        if pair[0] == key:
            bucket.remove(pair)
            print(f"🗑️ Key {key} deleted successfully.")
            return
    print("❌ Key not found.")

def search(key):
    bucket = hash_table[hash_func(key)]
    for pair in bucket:
        if pair[0] == key:
            return pair[1]
    return None

def display():
    print("\n📊 Hash Table Contents:")
    for i, bucket in enumerate(hash_table):
        print(f"Index {i}: {bucket}")

# Menu-driven Program
while True:
    print("\n--- Hash Table Operations ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Search")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter the key: "))
        value = input("Enter the value: ")
        insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 3:
        display()

    elif choice == 4:
        key = int(input("Enter key to search: "))
        value = search(key)
        if value is not None:
            print(f"🔍 Key found! Value: '{value}'")
        else:
            print("❌ Key not found.")

    elif choice == 5:
        print("👋 Exiting program...")
        break

    else:
        print("⚠️ Invalid choice! Please try again.")
