class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append function
    def append(self, data):
        new_node = Node(data)
        curr = self.head

        if not self.head:
            self.head = new_node
            return

        while curr.next:
            curr = curr.next

        curr.next = new_node

    # Detect cycle starting node
    def detectCycle(self):
        slow = fast = self.head

        # Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Loop found
            if slow == fast:

                # Move slow to head
                slow = self.head

                # Find starting node
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None


# Create linked list
sll = SinglyLinkedList()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

# Creating loop manually
# 5 -> 3
third_node = sll.head.next.next

last = sll.head
while last.next:
    last = last.next

last.next = third_node

# Detect cycle
cycle_node = sll.detectCycle()

if cycle_node:
    print("Cycle starts at node:", cycle_node.data)
else:
    print("No cycle found")