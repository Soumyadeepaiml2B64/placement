class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display() 


# delete a node
def delete(self, key):
    current = self.head
    if current.data == key:
        self.head = current.next
        current = None
        return
    while current.data != key:
        prev = current
        current = current.next
    if not current:
        return  
    prev.next = current.next
    current = None

LinkedList.delete = delete
ll.delete(20)
ll.display()


    

    