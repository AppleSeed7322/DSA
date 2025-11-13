queue = []

def add_event():
    event = input("Enter event to add: ")
    queue.append(event)
    print(f"Event '{event}' added.")

def process_event():
    if queue:
        print(f"Processing event: {queue.pop(0)}")
    else:
        print("No events to process.")

def display_events():
    if queue:
        print("Pending Events:")
        print('\n'.join(f"- {e}" for e in queue))
    else:
        print("No pending events.")

def cancel_event():
    if queue:
        event = input("Enter event to cancel: ")
        if event in queue:
            queue.remove(event)
            print(f"Event '{event}' canceled.")
        else:
            print("Event not found.")
    else:
        print("No events in queue.")

while True:
    print("\n-- Real-Time Event Processing --")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_event()
    elif choice == "2":
        process_event()
    elif choice == "3":
        display_events()
    elif choice == "4":
        cancel_event()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
