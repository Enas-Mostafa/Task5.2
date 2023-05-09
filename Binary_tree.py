from binarytree import build, Node

def add_element(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = add_element(root.left, value)
    else:
        root.right = add_element(root.right, value)
    return root

def delete_element(root, value):
    if not root:
        return root
    if value < root.value:
        root.left = delete_element(root.left, value)
    elif value > root.value:
        root.right = delete_element(root.right, value)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        temp = root.right
        while temp.left:
            temp = temp.left
        root.value = temp.value
        root.right = delete_element(root.right, temp.value)
    return root

if __name__ == '__main__':
    nodes = [7, 9, 13,3]
    binary_tree = build(nodes)

    print('Original binary tree:', binary_tree)

    while True:
        choice = input('Enter your choice (1: Add element, 2: Delete element): ')
        if choice == '1':
            value = int(input('Enter the value to add: '))
            binary_tree = add_element(binary_tree, value)
            print('Updated binary tree:', binary_tree)
        elif choice == '2':
            value = int(input('Enter the value to delete: '))
            binary_tree = delete_element(binary_tree, value)
            print('Updated binary tree:', binary_tree)
            