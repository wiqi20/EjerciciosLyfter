class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue():
    def __init__(self, head=None):
        self.head = head

    def print_all(self):
        current_node = self.head
        elements = []
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        print(" -> ".join(elements))

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head=new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def dequeue(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        return None

q = Queue()
q.enqueue("Hola")
q.enqueue("Mundo")
q.enqueue("third")
q.enqueue("fourth")

print("Queue inicial")
q.print_all()

print("\nDEQUEUE:")
removed = q.dequeue()
print("Nodo eliminado:", removed if removed else None)

print("\nCola después de dequeue:")
q.print_all()