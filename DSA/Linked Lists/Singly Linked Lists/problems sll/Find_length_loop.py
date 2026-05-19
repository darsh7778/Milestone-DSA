class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findLoopLength(head):
    slow = fast = head

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Cycle found
        if slow == fast:

            count = 1
            slow = slow.next

            # Count loop length
            while slow != fast:
                count += 1
                slow = slow.next

            return count

    return 0


# Create linked list
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Connect nodes
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Create loop
fifth.next = third

# Function call
print("Loop Length:", findLoopLength(head))