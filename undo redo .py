text = ""
undo_stack = []
redo_stack = []

def insert(new):
    global text
    undo_stack.append(text)
    text += new
    redo_stack.clear()

def undo():
    global text
    if undo_stack:
        redo_stack.append(text)
        text = undo_stack.pop()
    else:
        print("Nothing to undo.")

def redo():
    global text
    if redo_stack:
        undo_stack.append(text)
        text = redo_stack.pop()
    else:
        print("Nothing to redo.")

def display():
    print("\n--- Editor State ---")
    print("Text:", repr(text))
    print("Undo stack:", undo_stack)
    print("Redo stack:", redo_stack)
    print("--------------------")

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Undo")
    print("4. Redo")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        insert(input("Enter the text: "))
    elif choice == "2":
        display()
    elif choice == "3":
        undo()
        display()
    elif choice == "4":
        redo()
        display()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
