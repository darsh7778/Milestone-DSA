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
            
    def middle(self):
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next 
        
        return slow                   
            

            
            
sll = singlyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.traverse()

sll.middle()
sll.traverse()


                
        
        