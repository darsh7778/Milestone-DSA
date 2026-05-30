class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = new_node

    def odd_even_list(self):
        if self.head is None or self.head.next is None:
            return

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

    def traverse(self):
        if not self.head:
            print("ll is empty")
        else:
            current = self.head

            while current:
                print(current.val, end=" ")
                current = current.next
            print()


# Driver Code
ll = SLL()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Before:")
ll.traverse()

ll.odd_even_list()

print("After:")
ll.traverse()