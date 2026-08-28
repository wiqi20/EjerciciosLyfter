#STACK
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def pop(self):
        current_node = self.head
        if current_node is None:
            raise ValueError("The stack is empty")
        else:
            self.head = current_node.next
            return current_node.data

third_node = Node("3")
second_node = Node("2")
first_node = Node("1")
try:
    my_stack = Stack(first_node)
    my_stack.push(second_node)
    my_stack.push(third_node)
    print("\nBefore Pop")
    my_stack.print_structure()
    my_stack.pop()
    print("\nAfter Pop")
    my_stack.print_structure()
    my_stack.pop()
    print("\nAfter Pop")
    my_stack.print_structure()
    my_stack.pop()
    my_stack.pop()
except Exception as e:
    print("Error:", e)