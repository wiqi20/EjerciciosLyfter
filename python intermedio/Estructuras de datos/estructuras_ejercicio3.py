#Binary tree BST
class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root: Node

    def __init__(self, root=None):
        self.root = root

    def print_structure(self, node=None):
        if node is None:
            node = self.root
            if node is None:
                raise ValueError("the tree is empty")
        
        if node.left is not None:
            self.print_structure(node.left)
        print(node.data)
        if node.right is not None:
            self.print_structure(node.right)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)
try:
    tree = BinaryTree()
    tree.insert("5")
    tree.insert("2")
    tree.insert("6")
    tree.insert("1")
    tree.insert("4")
    tree.insert("7")
    print("\nEstructura del árbol (BST):")
    tree.print_structure()
except Exception as e:
    print("Error:", e)