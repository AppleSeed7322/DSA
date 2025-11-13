# Simple Linear and Binary Search

def linear_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

def binary_search(lst, x):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Input
n = int(input("Enter number of customer IDs: "))
ids = [int(input(f"ID {i+1}: ")) for i in range(n)]
x = int(input("Enter ID to search: "))

# Linear search
i1 = linear_search(ids, x)
print("Linear Search:", "Found at index" if i1 != -1 else "Not found", i1 if i1 != -1 else "")

# Binary search (on sorted list)
ids.sort()
i2 = binary_search(ids, x)
print("Binary Search:", "Found at index" if i2 != -1 else "Not found", i2 if i2 != -1 else "")
