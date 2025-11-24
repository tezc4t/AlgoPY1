class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 

    # WRITE BINARY_TO_DECIMAL METHOD HERE #
    #                                     #
    #                                     #
    #                                     #
    #                                     #
    #######################################



    def binary_to_decimal(self):
        current = self.head
        decimal = 0
        while current is not None:
            decimal = (decimal * 2) + current.value 
            
            
            current = current.next
            
        return decimal


# Test case 1: Binary number 110 = Decimal number 6
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
print("Test case 1 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 6
    print("Test case 1 passed, returned:", result)
except AssertionError:
    print("Test case 1 failed, returned:", result)
print("-" * 40)

# Test case 2: Binary number 1000 = Decimal number 8
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
print("Test case 2 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 8
    print("Test case 2 passed, returned:", result)
except AssertionError:
    print("Test case 2 failed, returned:", result)
print("-" * 40)

# Test case 3: Binary number 0 = Decimal number 0
linked_list = LinkedList(0)
print("Test case 3 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 0
    print("Test case 3 passed, returned:", result)
except AssertionError:
    print("Test case 3 failed, returned:", result)
print("-" * 40)

# Test case 4: Binary number 1 = Decimal number 1
linked_list = LinkedList(1)
print("Test case 4 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 1
    print("Test case 4 passed, returned:", result)
except AssertionError:
    print("Test case 4 failed, returned:", result)
print("-" * 40)

# Test case 5: Binary number 1101 = Decimal number 13
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
print("Test case 5 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 13
    print("Test case 5 passed, returned:", result)
except AssertionError:
    print("Test case 5 failed, returned:", result)
print("-" * 40)

    
 
"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1 linked list:
    1 -> 1 -> 0
    Test case 1 passed, returned: 6
    ----------------------------------------
    Test case 2 linked list:
    1 -> 0 -> 0 -> 0
    Test case 2 passed, returned: 8
    ----------------------------------------
    Test case 3 linked list:
    0
    Test case 3 passed, returned: 0
    ----------------------------------------
    Test case 4 linked list:
    1
    Test case 4 passed, returned: 1
    ----------------------------------------
    Test case 5 linked list:
    1 -> 1 -> 0 -> 1
    Test case 5 passed, returned: 13
"""

