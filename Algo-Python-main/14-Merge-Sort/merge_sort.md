Merge Sort
Write a function called merge_sort that sorts a list of integers using the merge sort algorithm.

The function should perform the following tasks:

Accept a parameter, my_list, which represents the list of integers to be sorted.

If the length of my_list is 1, return my_list as it is already sorted.

Calculate the middle index of the list using integer division by 2 and store it in the variable mid_index.

Recursively call the merge_sort function on the left and right halves of the list, created by slicing my_list using mid_index. Store the sorted left half in the variable left and the sorted right half in the variable right.

Call the previously implemented merge function to combine the sorted left and right halves into a single sorted list.

Return the sorted list.
