class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class Stack:

    def __init__(self):
        self.top = None

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
            self.length = 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    def pop(self):
        if self.top == None:
            return None
        else:
            self.top = self.top.next
            self.length -= 1


my_stack = Stack()
my_stack.push("1")
my_stack.push("2")
my_stack.push("3")
my_stack.push("4")
my_stack.push("5")
my_stack.pop()
print(my_stack)







