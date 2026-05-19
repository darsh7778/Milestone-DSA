class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class singlyLL:

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

    def traverse(self):

        if not self.head:
            print("sll is empty")

        else:
            curr = self.head

            while curr:
                print(curr.val, end="")
                curr = curr.next

    def remove_duplicates(self):

        temp = self.head

        while temp and temp.next:

            if temp.val == temp.next.val:
                temp.next = temp.next.next
                
            else:
                temp = temp.next


n = int(input())
values = list(map(int, input().split()))

sll = singlyLL()

for value in values:
    sll.append(value)

sll.remove_duplicates()
sll.traverse()