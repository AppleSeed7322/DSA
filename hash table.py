def hash_func(k, m):
    return k % m

def insert(table, val):
    m = len(table)
    key = hash_func(val, m)
    for i in range(m):
        idx = (key + i) % m
        if table[idx] is None:
            table[idx] = val
            print(f"✅ Inserted {val} at index {idx}")
            return
        elif table[idx] == val:
            print("⚠️ Value already exists.")
            return
    print("❌ Table is full — cannot insert more values.")

def search(table, k):
    m = len(table)
    key = hash_func(k, m)
    for i in range(m):
        idx = (key + i) % m
        if table[idx] is None:
            print("🔍 Key not found.")
            return
        elif table[idx] == k:
            print(f"🔎 Key {k} found at index {idx}")
            return
    print("🔍 Key not found.")

def delete(table, k):
    m = len(table)
    key = hash_func(k, m)
    for i in range(m):
        idx = (key + i) % m
        if table[idx] is None:
            print("⚠️ Key not found.")
            return
        elif table[idx] == k:
            table[idx] = None
            print(f"🗑️ Key {k} deleted from index {idx}")
            return
    print("⚠️ Key not found.")

def display(table):
    print("\n📋 Hash Table:")
    for i, v in enumerate(table):
        print(f"Index {i}: {v}")
    print("----------------------")

# Main loop
size = int(input("Enter size of hash table: "))
table = [None] * size

while True:
    print("\nHash Table Operations:")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your option (1-5): ")

    if choice == "1":
        val = int(input("Enter value to insert: "))
        insert(table, val)
    elif choice == "2":
        k = int(input("Enter key to search: "))
        search(table, k)
    elif choice == "3":
        k = int(input("Enter key to delete: "))
        delete(table, k)
    elif choice == "4":
        display(table)
    elif choice == "5":
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice. Please try again.")
