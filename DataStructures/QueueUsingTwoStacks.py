class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        """Pushes new data into the Stack
        if the head is None, set the new_node to be the head
        else FIRST set the new_node to point at the head 
        and then set the new_node to be the head"""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def is_empty(self):
        return self.head is None

    def peek(self):
        """Returns the data at the top of the stack. 
        It does NOT remove the top Node"""
        return self.head.data

    def pop(self):
        """Pops data from the top of the stack. 
        Save the popped elements data to return it later.
        Set the head of the Stack to point to the next element in the Stack and
        return popped data"""
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data


class MyQueue:
    def __init__(self):
        self.stackNewestOnTop = Stack()
        self.stackOldestOnTop = Stack()

    def exchange_stacks(self):
        """Called when OldestOnTop isEmpty and NewestOnTop has elements:
        while we have elements in NewestOnTop, we pop them and push them to OldestOnTop,
        which reverses their order"""
        while not self.stackNewestOnTop.is_empty():
            self.stackOldestOnTop.push(self.stackNewestOnTop.pop())


    def enqueue(self, data):
        """Enqueues elements by pushing them into the NewestOnTop stack"""
        self.stackNewestOnTop.push(data)

    def peek(self):
        """Peeks the last queue element by looking on top of the OldestOnTop stack,
        if the OldestOnTop stack is empty - push elements from NewestOnTop,
        by pushing we reverse the order"""
        if self.stackOldestOnTop.is_empty():
            if self.stackNewestOnTop.is_empty():
                return "Queue is empty"
            else:
                self.exchange_stacks()
        return self.stackOldestOnTop.peek()

    def dequeue(self):
        """Removes elements from the queue by popping the element from the OldestOnTop stack,
        if the OldestOnTop stack is empty - push elements from NewestOnTop,
        by pushing we reverse the order"""
        if self.stackOldestOnTop.is_empty():
            if self.stackNewestOnTop.is_empty():
                return "Queue is empty"
            else:
                self.exchange_stacks()
        return self.stackOldestOnTop.pop()


#Test Cases
my_queue = MyQueue()
my_queue.enqueue(1)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(7)
my_queue.enqueue(11)
my_queue.enqueue(20)

print(f"Peeking {my_queue.peek()}")
print(f"Dequeue {my_queue.dequeue()}")
print(f"Dequeue {my_queue.dequeue()}")
print(f"Dequeue {my_queue.dequeue()}")
print(f"Peeking {my_queue.peek()}")
