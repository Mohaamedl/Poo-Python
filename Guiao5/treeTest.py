from binarytree import Node

# create root node
root = Node(3)

# create node at connect at left
node6 = Node (6)
root.left = node6

# create other node and connect to root at right
node8 = Node(8)
root.right = node8
node8.left = Node(1)
node8.right = Node(5)
node8 = root.right

# add nodes to node6
node10 = Node(10)
node9 = Node(9)
node6.left= node10
node6.right= node9
node10.left = Node(2)
node10.right = Node(4)
node7 = Node(7)
node9.left = node7
node7.left = Node(11)
node7.right = Node(12)
node5 = node6.right
print('Binary tree :', root)
node9 = None
node6.right = node9
node7 = Node(7)
node7.left = Node(11)
node7.right = Node(12)
node6.right = node7
print('Binary tree :', root)
