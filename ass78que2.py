# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeuing elements.
class queue:
    def __init__(self):
        self.queue = []

    def isempty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty!")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item

    def display(self):
        print("Queue contents:", self.queue)


q = queue()
n = int(input("Enter number of elements : "))
print(f"Enter {n} elements of queue.")
for i in range(n):
    data = int(input())
    q.enqueue(data)
while 1:
    print()
    print("1. enqueue at any position")
    print("2. dequeue at any position")
    print("3. Display ")
    print("0. Exit")
    choise = int(input("Enter choice : "))
    print()
    if choise == 1:
        data = int(input("Enter data which you want to enqueue : "))
        q.enqueue(data)
    elif choise == 2:
        q.dequeue()
    elif choise == 3:
        q.display()
    elif choise == 0:
        break
    else:
        print("Invalid choise!!!")