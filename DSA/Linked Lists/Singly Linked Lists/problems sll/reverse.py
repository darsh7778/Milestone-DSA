class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class singlyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            
            while curr.next is not None:
                curr = curr.next
            
            curr.next = new_node
    
    def traverse(self):
        if not self.head:
            print("linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()
            
    def reverse(self):
        temp = self.head
        prev = None
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
            
        self.head = prev
            
            
sll = singlyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.traverse()

sll.reverse()
sll.traverse()


                
        
        