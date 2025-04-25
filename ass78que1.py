# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.
# Node class representing an element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        print("Linked list : ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data, pos=None):
        newnode = Node(data)
        if self.head is None or pos == 0:
            newnode.next = self.head
            self.head = newnode
            return

        current = self.head
        count = 0

        if pos is not None:
            while current and count < pos - 1:
                current = current.next
                count += 1
        else:
            while current.next:
                current = current.next
        if current is None:
            print("Position out of bounds. Inserting at the end.")
            self.insert(data)
        else:
            newnode.next = current.next
            current.next = newnode

    def delete(self, pos=None):
        if self.head is None:
            print("Linked list is empty.")
            return

        if pos is not None:
            if pos == 0:
                self.head = self.head.next
                return
            current = self.head
            count = 0
            while current and count < pos - 1:
                current = current.next
                count += 1
            if current is None or current.next is None:
                print("Position out of bounds.")
                return
            current.next = current.next.next
            return

        self.head = self.head.next


ll = linkedlist()
n = int(input("Enter number of nodes : "))
print(f"Enter {n} elements of linked list.")
for i in range(n):
    data = int(input())
    ll.insert(data)
while 1:
    print()
    print("1. Insert node at any position")
    print("2. Delete node at any position")
    print("3. Display ")
    print("0. Exit")
    choise = int(input("Enter choice : "))
    print()
    if choise == 1:
        data = int(input("Enter data which you want to insert : "))
        pos = int(input("Enter position at which you want to insert : "))
        ll.insert(data, pos)
    elif choise == 2:
        pos = int(input("Enter position at which you want to delete : "))
        ll.delete(pos)
    elif choise == 3:
        ll.display()
    elif choise == 0:
        break
    else:
        print("Invalid choise!!!")
