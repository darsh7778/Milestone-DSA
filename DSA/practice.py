class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
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
            print("linked list is empty")
        else:
            current = self.head
            
            while current:
                print(current.val, end=" ")
                current = current.next
            print()
            
    def insert(self, val, position):
        new_node = Node(val)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            curr = self.head
            prev = None
            count = 0
            
            while curr is not None and count < position:
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
        

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()

sll.insert(45, 4)
sll.traverse()

sll.delete(30)
sll.traverse()