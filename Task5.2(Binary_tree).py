import binarytree

# Construct a binary tree from a list of integers
tree = binarytree.build([15, 30, 77, 1, 4, 6, 18])

# Print the initial tree
print("Initial Tree:")
print(tree)

# Function to add an element to the tree
def add_to_tree(root, value):
    # If the root is None, create a new node with the value
    if root is None:
        return binarytree.Node(value)

    # If the new value is less than the root's value, add it to the left subtree
    if value < root.value:
        root.left = add_to_tree(root.left, value)

    # If the new value is greater than the root's value, add it to the right subtree
    elif value > root.value:
        root.right = add_to_tree(root.right, value)

    # Return the modified root node
    return root

# Function to delete an element from the tree
def delete_from_tree(root, value):
    # If the root is None, the value is not in the tree
    if root is None:
        return root

    # If the value is less than the root's value, move to the left subtree
    if value < root.value:
        root.left = delete_from_tree(root.left, value)

    # If the value is greater than the root's value, move to the right subtree
    elif value > root.value:
        root.right = delete_from_tree(root.right, value)

    # If the value is equal to the root's value, delete the node
    else:
        # If the node has only one child or no child, return the child node
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # If the node has two children, find the minimum value in the right subtree
        min_node = root.right
        while min_node.left is not None:
            min_node = min_node.left

        # Replace the value of the current node with the minimum value
        root.value = min_node.value

        # Delete the minimum node from the right subtree
        root.right = delete_from_tree(root.right, min_node.value)

    # Return the modified root node
    return root

# Loop until the user chooses to exit
while True:
    # Ask the user for their choice
    choice = int(input("\nChoose an operation:\n1. Add element\n2. Delete element\n3. Exit\n"))

    # Add a new element to the tree
    if choice == 1:
        value = int(input("Enter the value to add: "))
        tree = add_to_tree(tree, value)
        print("Element added successfully.")
        print(tree)

    # Delete an element from the tree
    elif choice == 2:
        value = int(input("Enter the value to delete: "))
        tree = delete_from_tree(tree, value)
        print("Element deleted successfully.")
        print(tree)

    # Exit the program
    elif choice == 3:
        print("Exiting the program.")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please choose again.")