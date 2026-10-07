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

    def bubble_sort(self):
        if self.head is None:
            return
        swapped= True
        while swapped:
            swapped = False
            current_node = self.head
            while current_node.next is not None:
                next_node = current_node.next
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                    swapped = True
                current_node = current_node.next

third_node = Node("3")
second_node = Node("2")
first_node = Node("1")
try:
    my_stack = Stack(first_node)
    my_stack.push(second_node)
    my_stack.push(third_node)
    print("\nBefore Bubble sort")
    my_stack.print_structure()
    print("\nAfter Bubble sort")
    my_stack.bubble_sort()
    my_stack.print_structure()
except Exception as e:
    print("Error:", e)