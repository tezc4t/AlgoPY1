BST: Insert
Implement the insert method for the BinarySearchTree class that inserts a new node with a given value into the binary search tree.

The method should perform the following tasks:

Create a new instance of the Node class using the provided value.

If the binary search tree is empty (i.e., self.root is None), set the root attribute of the BinarySearchTree class to point to the new node and return True.

If the binary search tree is not empty, initialize a temporary variable temp to point to the root node, and then perform the following steps in a loop until the new node is inserted:

If the value of the new node is equal to the value of the current node (stored in temp), return False, indicating that duplicate values are not allowed in the tree.

If the value of the new node is less than the value of the current node, check if the left child of the current node is None:

If it is, set the left child of the current node to the new node and return True.

If it is not, update temp to point to the left child and continue the loop.

If the value of the new node is greater than the value of the current node, check if the right child of the current node is None:

If it is, set the right child of the current node to the new node and return True.

If it is not, update temp to point to the right child and continue the loop.
