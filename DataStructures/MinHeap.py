class EmptyHeapException(Exception):
    """EmptyHeapException, inheriting from the exception class.
    Raised when trying to pop or peek in an empty Heap!"""
    def __init__(self, message="Empty Heap"):
        self.message = message

class Heap: #Min heap
    def __init__(self):
        self.array = []
        self.size = 0

    def __repr__(self):
        return f"{self.array}"

    # Helper functions
    def get_parent_index(self, index):
        return (index - 1) // 2
    def get_left_child_index(self, index):
        return 2 * index + 1
    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size
    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child_data(self, index):
        return self.array[self.get_left_child_index(index)]
    def right_child_data(self, index):
        return self.array[self.get_right_child_index(index)]
    def parent_data(self, index):
        return self.array[self.get_parent_index(index)]

    def swap(self, idx1, idx2):
        self.array[idx1], self.array[idx2] = self.array[idx2], self.array[idx1]

    def heapify_up(self):
        """Called when adding an element to the heap
        While the current element is smaller than it's parent -> swap()"""
        if self.size == 1:
            return
        idx = self.size - 1
        while self.has_parent(idx) and self.array[idx] < self.parent_data(idx):
            self.swap(idx, self.get_parent_index(idx))
            idx = self.get_parent_index(idx)

    def heapify_down(self):
        """Called when we remove an element.
        While the current element has children (checking for left children is enough) and
        its left children value is smaller:
        check it has a right children
        get the index of the children with the smaller value
        swap the current element with the smaller children"""
        if self.size == 1:
            return
        idx = 0
        while self.has_left_child(idx) and self.left_child_data(idx) < self.array[idx]:
            smaller_child_idx = self.get_left_child_index(idx)
            if self.has_right_child(idx) and self.right_child_data(idx) < self.left_child_data(idx):
                smaller_child_idx = self.get_right_child_index(idx)
            self.swap(idx, smaller_child_idx)
            idx = smaller_child_idx

    def add(self, data):
        self.array.append(data)
        self.size += 1
        self.heapify_up()

    def pop(self):
        if self.size == 0:
            raise EmptyHeapException

        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        popped = self.array.pop(self.size - 1)
        self.size -= 1
        self.heapify_down()
        return popped

    def peek(self):
        if self.size == 0:
            raise EmptyHeapException
        return self.array[0]




my_heap = Heap()
my_heap.add(5)
my_heap.add(10)
my_heap.add(3)
my_heap.add(1)
my_heap.add(15)
my_heap.add(20)
my_heap.add(30)
my_heap.add(12)

print(my_heap)

print(my_heap.pop())
print(my_heap.pop())
print(my_heap.pop())

print(my_heap)


my_heap2 = Heap()
try:
    my_heap2.pop()
except EmptyHeapException:
    print("The Heap is empty! Add elements first.")
