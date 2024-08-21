        
from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order 
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains
    
    Returns a sorted linked list
    Runs in 0(kn log n) time 
    """
    
    if linked_list.size() == 1: 
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes 0(k log n) time
    """
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    
    size = linked_list.size()
    mid = size // 2
    mid_node = linked_list.node_at_index(mid-1)
    
    left_half = linked_list
    right_half = LinkedList()
    right_half.head = mid_node.next_node
    mid_node.next_node = None
    
    return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes 
    Returns a new merged list
    
    Runs in 0(n) time
    """ 
    # Create a new linked list that contains nodes from 
    # merging left and right   
    merged = LinkedList()
    # Add a fake head that is discarded later
    merged.add(0)  
    
    # Set current to the head of the linked list
    current = merged.head
    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head
    
    # Iterate over the left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # If the head node of the left is None, we're past the tail
        # Add the node from the right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        elif right_head is None:
            # Not at either tail node 
            # Obtain node data to perform comprison operations
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node 
            # Obtain node data to perform comprison operations             
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to left node    
            else: 
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        current = current.next_node
    
    # Discard fake head and set first merged node as head    
    head = merged.head.next_node
    merged.head = head
    
    return merged  
    
l = LinkedList()
l.add(10)           
l.add(2)           
l.add(44)           
l.add(15)           
l.add(250)   

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)  

# The merge_sort Function:
# This function implements the merge sort algorithm on a linked list.

# Base Case:

# If the linked list has only one element (linked_list.size() == 1), it's already sorted, so the function returns the list as is.
# If the linked list is empty (linked_list.head is None), it returns the list.
# Recursive Case:

# The linked list is split into two halves using the split function.
# merge_sort is then called recursively on both halves.
# The sorted halves are merged back together using the merge function.
# The split Function:
# This function splits a linked list into two halves.

# Base Case:

# If the list is empty or has only one node (linked_list is None or linked_list.head is None), it returns the list as left_half and None as right_half.
# Splitting the List:

# The size of the linked list is determined, and the midpoint is calculated.
# The list is split at the midpoint into two halves:
# The left_half remains as the original list.
# The right_half is created as a new list starting from the node after the midpoint.
# The node at the midpoint (mid_node) is set as the end of the left_half by setting its next_node to None.
# The merge Function:
# This function merges two sorted linked lists into a single sorted linked list.

# Initialization:

# A new linked list (merged) is created, and a "fake" head node is added. This fake head helps simplify the merge process and is discarded later.
# current is set to point to the fake head, and left_head and right_head are set to point to the heads of the left and right linked lists.
# Merging:

# The function iterates as long as there are nodes in either left_head or right_head.
# Cases:
# If left_head is None, it means the left list is exhausted, so nodes from the right list are added to the merged list.
# If right_head is None, it means the right list is exhausted, so nodes from the left list are added to the merged list.
# If both lists have nodes, the data in the current nodes (left_data and right_data) are compared. The smaller value is added to the merged list, and the corresponding list's head is moved to the next node.
# Updating the Current Node:

# After adding a node to the merged list, current is moved to the next node to continue the merge process.
# Finalizing:

# The fake head is discarded by setting the head of the merged list to merged.head.next_node.
# The merged list is returned.      
        