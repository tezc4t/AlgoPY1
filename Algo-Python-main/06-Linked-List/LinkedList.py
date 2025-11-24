

# Create a new linked list
print("=== Creating LinkedList ===")
my_linked_list = LinkedList(1)
my_linked_list.print_list()

# append() - Add node to end
print("\n=== append(2), append(3) ===")
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()

# # prepend() - Add node to beginning
# print("\n=== prepend(0) ===")
# my_linked_list.prepend(0)
# my_linked_list.print_list()

# # pop() - Remove last node
# print("\n=== pop() ===")
# popped = my_linked_list.pop()
# print(f"Popped value: {popped.value}")
# my_linked_list.print_list()

# # pop_first() - Remove first node
# print("\n=== pop_first() ===")
# popped_first = my_linked_list.pop_first()
# print(f"Popped first value: {popped_first.value}")
# my_linked_list.print_list()

# # get() - Get node at index
# print("\n=== get(1) ===")
# node = my_linked_list.get(1)
# print(f"Node at index 1: {node.value}")

## set_value() - Update value at index
# print("\n=== set_value(0, 5) ===")
# my_linked_list.set_value(0, 5)
# my_linked_list.print_list()

# # insert() - Insert at specific index
# print("\n=== insert(1, 10) ===")
# my_linked_list.insert(1, 10)
# my_linked_list.print_list()

# # remove() - Remove at specific index
# print("\n=== remove(1) ===")
# removed = my_linked_list.remove(1)
# print(f"Removed value: {removed.value}")
# my_linked_list.print_list()

# # reverse() - Reverse the linked list
# print("\n=== reverse() ===")
# my_linked_list.reverse()
# my_linked_list.print_list()

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