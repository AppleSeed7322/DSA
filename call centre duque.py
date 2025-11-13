from collections import deque
import random
import time

class CallCenter:
    def __init__(self):
        self.queue = deque()

    def add_call(self, name):
        self.queue.append(name)
        print(f"📞 Call from {name} added.")

    def attend_call(self):
        if self.queue:
            print(f"✅ Attending call from {self.queue.popleft()} (finished).")
        else:
            print("⚠️ No calls to attend.")

    def show_queue(self):
        if self.queue:
            print("📋 Queue:", " -> ".join(self.queue))
        else:
            print("📭 Queue is empty.")

    def is_empty(self):
        return not self.queue


# Simulation
call_center = CallCenter()
customers = ["A", "B", "C", "D", "E", "F"]

# Add random incoming calls
for _ in range(5):
    call_center.add_call(random.choice(customers))
    time.sleep(0.5)

print("\n--- Attending Calls ---\n")

# Process all calls in the queue
while not call_center.is_empty():
    call_center.show_queue()
    call_center.attend_call()
    time.sleep(1)

print("\n🎉 All calls have been attended!")
