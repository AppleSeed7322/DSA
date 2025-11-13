# Simple Library Program

n = int(input("Enter number of library members: "))
books_list = []

for i in range(n):
    name = input(f"\nEnter member name {i+1}: ")
    b = int(input(f"How many books has {name} borrowed? "))
    books = [input(f"Enter book name {j+1}: ") for j in range(b)]
    books_list.append(books)

# Average books
average = sum(len(b) for b in books_list) / n

# Book frequency
book_count = {}
for books in books_list:
    for b in books:
        book_count[b] = book_count.get(b, 0) + 1

# Most and least borrowed
if book_count:
    max_val, min_val = max(book_count.values()), min(book_count.values())
    most = [b for b, c in book_count.items() if c == max_val]
    least = [b for b, c in book_count.items() if c == min_val]
else:
    most = least = []

# Members with no books
no_books = sum(1 for b in books_list if not b)

# Output
print("\n----- Library Report -----")
print("Average books borrowed:", round(average, 2))
print("Most borrowed book(s):", most)
print("Least borrowed book(s):", least)
print("Members who borrowed no books:", no_books)
