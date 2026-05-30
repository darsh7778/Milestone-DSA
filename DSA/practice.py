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
            
    def insert_at(self, val, pos):
        new_node = Node(val)
        
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = None
            curr = self.head
            count = 0
            
            while curr.next and count < pos:
                prev = curr
                curr = curr.next
                count += 1
                
            prev.next = new_node
            new_node.next = curr
            
    def delete(self, val):
        temp = self.head
        
        if temp.next:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None

                while temp:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                    
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("node not found") 
                
    def traverse(self):
        if not self.head:
            print("ll is empty")
        else:
            current = self.head
            
            while current:
                print(current.val)
                current = current.next
                
    


sll = SLL()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

sll.insert_at(6, 2)

sll.delete(6)

sll.traverse()
        
        