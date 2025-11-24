Merge
Write a function called merge that merges two sorted lists of integers into a single sorted list.

The function should perform the following tasks:

Accept two parameters, list1 and list2, which represent the two sorted lists of integers.

Initialize an empty list called combined, and two index variables, i and j, both initialized to 0.

While both i and j are within the bounds of their respective lists, perform the following steps:

Compare the elements at position i in list1 and position j in list2.

If the element in list1 is smaller, append it to combined and increment i.

Otherwise, append the element from list2 to combined and increment j.

After one of the lists has been fully traversed, append any remaining elements from list1 and list2 to combined.

Return the merged list combined.
