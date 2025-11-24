class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        pass

    def contains(self, value):
        pass


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""