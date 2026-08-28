class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
            self.head = None
    
    def insert_front(self, data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head=new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def delete(self,data):
        current=self.head
        previous=None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head= current.next
                return True
            previous = current
            current = current.next
        return False

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

ll = LinkedList()
ll.insert_back("Hola")
ll.insert_back("Mundo")
ll.insert_front("Inicio")
ll.insert_back("Final")

print("Lista inicial:")
ll.print_all()

print("\nEliminar 'Mundo':")
ll.delete("Mundo")
ll.print_all()