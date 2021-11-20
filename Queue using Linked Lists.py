class Node:.

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = self.first
            self.length = 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        self.first = self.first.next
        self.length -= 1
        if self.first == self.last:
            self.last = None


my_queue = Queue()
my_queue.enqueue("1")
my_queue.enqueue("2")
my_queue.enqueue("3")
my_queue.dequeue()
print(my_queue.peek())
print(my_queue)




