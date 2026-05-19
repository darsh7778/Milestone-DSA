class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append function
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node

    # Traverse function
    def traverse(self):
        if not self.head:
            print("linked list is empty")
        else:
            curr = self.head
            while curr:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    # Detect loop
    def detect_loop(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Loop found
            if slow == fast:
                return True

        return False


# Create linked list
sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

# Traverse before creating loop
print("Linked List:", end=" ")
sll.traverse()

# Create loop manually
# 50 -> 30
third_node = sll.head.next.next

last = sll.head
while last.next:
    last = last.next

last.next = third_node

# Detect loop
if sll.detect_loop():
    print("Loop detected")
else:
    print("No loop found")