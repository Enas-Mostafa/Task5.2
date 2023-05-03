# Creating binary tree 
# from given list
from binarytree import build , Node
  
  
# List of nodes
nodes =[3, 6, 8, 2, 11, None, 13]
  
# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
      binary_tree)
  
# Getting list of nodes from
# binarytree
print('\nList from binary tree :', 
      binary_tree.values)
print("Enter:\n 1 for adding a new element\n 2 for deleting an element")
choice=int(input("Your choice is :"))
if choice==1:
    element=int(input("Enter the new element:"))
    nodes.append(element)
    new_BT=build(nodes)
    print("The new BT",new_BT)
elif choice==2:
    element=int(input("Enter the element you want to delete:"))
    nodes.remove(element)
    new_BT=build(nodes)
    print("The new BT",new_BT)
else:
    print("please,enter a right choice")

