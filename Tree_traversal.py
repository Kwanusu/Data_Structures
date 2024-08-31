




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform inorder traversal
def inorderTraversal(root):
  
    # Base case: if null
    if root is None:
        return
      
    # Recur on the left subtree
    inorderTraversal(root.left)
    
    # Visit the current node
    print(root.data, end=" ")
    
    # Recur on the right subtree
    inorderTraversal(root.right)

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorderTraversal(root)

# Output
# 4 2 5 1 3 
# Time Complexity: O(N)
# Auxiliary Space: If we don’t consider the size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree.

# Preorder Traversal:
# Preorder traversal visits the node in the order: Root -> Left -> Right

# Inorder-Traversal-of-Binary-Tree

# Algorithm for Preorder Traversal:

# Preorder(tree)

# Visit the root.
# Traverse the left subtree, i.e., call Preorder(left->subtree)
# Traverse the right subtree, i.e., call Preorder(right->subtree)
# Uses of Preorder Traversal:

# Preorder traversal is used to create a copy of the tree.
# Preorder traversal is also used to get prefix expressions on an expression tree.
# Code Snippet for Preorder Traversal:



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform preorder traversal
def preorderTraversal(root):
  
    # Base case
    if root is None:
        return
      
    # Visit the current node
    print(root.data, end=' ')
    
    # Recur on the left subtree
    preorderTraversal(root.left)
    
    # Recur on the right subtree
    preorderTraversal(root.right)

def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("PreOrder traversal: ", end='')
    preorderTraversal(root)
    print()
if __name__ == "__main__":
    main()
# Output
# 1 2 4 5 3 
# Time Complexity: O(N)
# Auxiliary Space: If we don’t consider the size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree.

# Postorder Traversal:
# Postorder traversal visits the node in the order: Left -> Right -> Root

# Postorder-Traversal-of-Binary-Tree

# Algorithm for Postorder Traversal:

# Algorithm Postorder(tree)

# Traverse the left subtree, i.e., call Postorder(left->subtree)
# Traverse the right subtree, i.e., call Postorder(right->subtree)
# Visit the root
# Uses of Postorder Traversal:

# Postorder traversal is used to delete the tree. See the question for the deletion of a tree for details.
# Postorder traversal is also useful to get the postfix expression of an expression tree.
# Postorder traversal can help in garbage collection algorithms, particularly in systems where manual memory management is used.
# Code Snippet for Postorder Traversal:



class Node:
    # Constructor to create a new node
    def __init__(self, data):
        # Assign data to this node
        self.data = data
        # Initialize left and right children as None
        self.left = None
        self.right = None

# Function to perform postorder traversal
def postorderTraversal(node):
    # Base case: if the current node is null, return
    if node is None:
        return
    # Recur on the left subtree
    postorderTraversal(node.left)
    # Recur on the right subtree
    postorderTraversal(node.right)
    # Visit the current node
    print(node.data, end=' ')

# Main function
def main():
    # Creating the tree nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Perform postorder traversal
    print("Postorder traversal: ", end='')
    postorderTraversal(root)
    print()

# Run the main function
if __name__ == "__main__":
    main()

# Output
# 4 5 2 3 1 
# Level Order Traversal :
# Level Order Traversal visits all nodes present in the same level completely before visiting the next level.

# Level-Order-Traversal-of-Binary-Tree

# Algorithm for Level Order Traversal:

# LevelOrder(tree)

# Create an empty queue Q
# Enqueue the root node of the tree to Q
# Loop while Q is not empty
# Dequeue a node from Q and visit it
# Enqueue the left child of the dequeued node if it exists
# Enqueue the right child of the dequeued node if it exists
# Uses of Level Order:

# Level Order Traversal is mainly used as Breadth First Search to search or process nodes level-by-level.
# Level Order traversal is also used for Tree Serialization and Deserialization .
# Code Snippet for Level Order Traversal:



from collections import deque

# Define a tree node structure
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

# Function to perform level order traversal
def level_order_traversal(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Level Order Traversal: ", end="")
    level_order_traversal(root)

# Output
# 1 2 3 4 5 6 
# Other Tree Traversals:
# Boundary Traversal
# Diagonal Traversal
# 1. Boundary Traversal:
# Boundary Traversal of a Tree includes:

# left boundary (nodes on left excluding leaf nodes)
# leaves (consist of only the leaf nodes)
# right boundary (nodes on right excluding leaf nodes)
# Algorithm for Boundary Traversal:

# BoundaryTraversal(tree)

# If root is not null:
# Print root’s data
# PrintLeftBoundary(root->left) // Print the left boundary nodes
# PrintLeafNodes(root->left) // Print the leaf nodes of left subtree
# PrintLeafNodes(root->right) // Print the leaf nodes of right subtree
# PrintRightBoundary(root->right) // Print the right boundary nodes
# Uses of Boundary Traversal:

# Boundary traversal helps visualize the outer structure of a binary tree, providing insights into its shape and boundaries.
# Boundary traversal provides a way to access and modify these nodes, enabling operations such as pruning or repositioning of boundary nodes.
# 2. Diagonal Traversal
# In the Diagonal Traversal of a Tree, all the nodes in a single diagonal will be printed one by one.

# Algorithm for Diagonal Traversal:

# DiagonalTraversal(tree):

# If root is not null:
# Create an empty map
# DiagonalTraversalUtil(root, 0, M) // Call helper function with initial diagonal level 0
# For each key-value pair (diagonalLevel, nodes) in M:
# For each node in nodes:
# Print node’s data
# DiagonalTraversalUtil(node, diagonalLevel, M):

# If node is null:
# Return
# If diagonalLevel is not present in M:
# Create a new list in M for diagonalLevel
# Append node’s data to the list at M[diagonalLevel]
# DiagonalTraversalUtil(node->left, diagonalLevel + 1, M) // Traverse left child with increased diagonal level
# DiagonalTraversalUtil(node->right, diagonalLevel, M) // Traverse right child with same diagonal level
# Uses of Diagonal Traversal:

# Diagonal traversal helps in visualizing the hierarchical structure of binary trees, particularly in tree-based data structures like binary search trees (BSTs) and heap trees.
# Diagonal traversal can be utilized to calculate path sums along diagonals in a binary tree.