class Node:
    """A class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        
class LinkedList:  
    """A class to represent the linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head  
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a new node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node with the specified data."""
        if not self.head:
            print("List is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print("Data not found in the list")

    def display(self):
        """Display the elements of the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()  # Output: 1 -> 2 -> 3 -> None

    ll.prepend(0)
    ll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

    ll.delete(2)
    ll.display()  # Output: 0 -> 1 -> 3 -> None