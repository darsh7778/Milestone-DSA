class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        #if self.head is None:
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()
    
    def insert_at(self, val, position):
        new_node = Node(val)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count+=1
                
            prev_node.next = new_node
            new_node.next = current
        
                
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

sll.traverse()

sll.insert_at(35, 3)
sll.traverse()
        