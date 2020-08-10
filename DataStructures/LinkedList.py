class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        self.traverse()
        return "None"

    def isEmpty(self):
        return self.head is None

    def add(self, data):
        """Adds a new node to the List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        """Adds the Node at the end of the list (implemented without using the isEmpty function).
        Set the current node to be the head of the Linked List.
        Traverse the list until we reach the last node.
        We check to see if current_node actually points at something,
        if it does: Set the current_node's next to point at the new_node
        else: Set the head to be the new node
        """
        new_node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        if current_node:
            current_node.next = new_node
        else:
            self.head = new_node

    def remove(self, data):
        """If the List is not empty:
        traverse the list until we find the desired value
        if the entire list is traverse and the value is not found:
        the value is not in the list"""
        if self.isEmpty():
            return "Nothing to remove"

        current_node = self.head
        while current_node.next.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next.data != data:
            return f"\nNode with data: {data} was not found"
        if self.head is current_node:
            self.head = current_node.next
            return f"Removed Node with data: {current_node.data}"
        if not current_node.next.next:
            current_node.next = None
            return current_node.next.data
        current_node.next = current_node.next.next
        return current_node.next.data

    def traverse(self):
        """Traverses the list and prints all the values on one line"""
        if self.isEmpty():
            return "The List is empty!"
        current_node = self.head
        print() #added to split the data on consecutive traverses
        while current_node:
            print(f"{current_node.data} ->", end=' ')
            current_node = current_node.next

    def reverse(self):
        """Reverses the Linked List"""
        if self.isEmpty():
            return "Nothing to traverse"

        #Nodes
        prev_node = None
        current_node = self.head
        next_node = self.head.next

        while next_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next

        current_node.next = prev_node
        self.head = current_node

linked_list = LinkedList()
linked_list.add(2)
linked_list.add(1)
linked_list.add(5)
linked_list.add(20)
linked_list.add(3)
linked_list.add(7)

print(linked_list)
linked_list.remove(5)
print(linked_list.remove(100))
print(linked_list)

linked_list.reverse()
print(linked_list)

linked_list.add(50)
print(linked_list)

linked_list.reverse()
print(linked_list)
