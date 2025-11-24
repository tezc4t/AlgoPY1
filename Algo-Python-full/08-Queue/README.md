Queue: Constructor
Create a Queue class that represents a first-in, first-out (FIFO) data structure using a linked list implementation.

The Queue class should contain the following components:

A Node class, which serves as the building block for the linked list. The Node class should have an **init** method that initializes the following attributes:

value: The value of the node.

next: A reference to the next node in the list, initialized to None.

The Queue class should have an **init** method that initializes the queue with a single node, using the given value. The **init** method should perform the following tasks:

Create a new instance of the Node class using the provided value.

Set the first attribute of the Queue class to point to the new node.

Set the last attribute of the Queue class to point to the same node.

Initialize a length attribute for the Queue class, which represents the current number of nodes in the queue, and set it to 1.
