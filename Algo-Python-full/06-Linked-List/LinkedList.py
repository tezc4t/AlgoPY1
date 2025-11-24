class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after



# Create a new linked list
print("=== Creating LinkedList ===")
my_linked_list = LinkedList(1)
my_linked_list.print_list()

# append() - Add node to end
print("\n=== append(2), append(3) ===")
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()

# prepend() - Add node to beginning
print("\n=== prepend(0) ===")
my_linked_list.prepend(0)
my_linked_list.print_list()

# pop() - Remove last node
print("\n=== pop() ===")
popped = my_linked_list.pop()
print(f"Popped value: {popped.value}")
my_linked_list.print_list()

# pop_first() - Remove first node
print("\n=== pop_first() ===")
popped_first = my_linked_list.pop_first()
print(f"Popped first value: {popped_first.value}")
my_linked_list.print_list()

# get() - Get node at index
print("\n=== get(1) ===")
node = my_linked_list.get(1)
print(f"Node at index 1: {node.value}")

# set_value() - Update value at index
print("\n=== set_value(0, 5) ===")
my_linked_list.set_value(0, 5)
my_linked_list.print_list()

# insert() - Insert at specific index
print("\n=== insert(1, 10) ===")
my_linked_list.insert(1, 10)
my_linked_list.print_list()

# remove() - Remove at specific index
print("\n=== remove(1) ===")
removed = my_linked_list.remove(1)
print(f"Removed value: {removed.value}")
my_linked_list.print_list()

# reverse() - Reverse the linked list
print("\n=== reverse() ===")
my_linked_list.reverse()
my_linked_list.print_list()

# Original test case
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()


print('\nLL after reverse():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1
    
"""