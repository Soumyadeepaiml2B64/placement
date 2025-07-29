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
ll.append(40)
ll.append(50)
ll.append(60)
ll.append(70)
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


    
#insertioninmiddle
def insert_in_middle(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    old = self.head
    new = self.head
    prev = None
    while new and new.next:
        prev = old
        old = old.next
        new = new.next.next
    new_node.next = old
    if prev:
        prev.next = new_node
    else:
        self.head = new_node

#LinkedList.insert_in_middle = insert_in_middle
#ll.insert_in_middle(15)
#ll.display()
def print_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if slow:
        print("Middle element:", slow.data)

#LinkedList.print_middle = print_middle
#ll.print_middle()

def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev

LinkedList.reverse = reverse
ll.reverse()
ll.display()

def from_last(self):
    n = int(input("Enter n: "))
    main_ptr = self.head
    ref_ptr = self.head
    count = 0
    while count < n:
        if not ref_ptr:
            print(f"List has fewer than {n} elements.")
            return
        ref_ptr = ref_ptr.next
        count += 1
    while ref_ptr:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
    if main_ptr:
        print(f"{n}th element from the last is: {main_ptr.data}")
    else:
        print("Element not found.")


LinkedList.from_last = from_last
ll.from_last()
    