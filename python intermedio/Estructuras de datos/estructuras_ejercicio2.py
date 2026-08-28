#DOUBLE ENDED QUEUE
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Dequeue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def pop_left(self):
        current_node = self.head
        if current_node is None:
            raise ValueError("The Dequeue is empty")
        else:
            self.head = current_node.next
            return current_node.data

    def push_right(self, new_node):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def pop_right(self):
        if self.head is None:
            raise ValueError("The Dequeue is empty")
        current_node = self.head
        prev_node = None

        while  current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next

        if prev_node is None:
            self.head = None
        else:
            prev_node.next = None

        return current_node.data

third_node = Node("3")
second_node = Node("2")
first_node = Node("1")
try:
    my_dequeue = Dequeue(second_node)
    my_dequeue.push_right(third_node)
    my_dequeue.push_left(first_node)
    print("\nBefore Pop")
    my_dequeue.print_structure()
    my_dequeue.pop_left()
    my_dequeue.pop_right()
    print("\nAfter Pop")
    my_dequeue.print_structure()
    my_dequeue.pop_left()
    print("\nAfter Pop")
    my_dequeue.print_structure()
    my_dequeue.pop_left()
    my_dequeue.pop_right()
except Exception as e:
    print("Error:", e)