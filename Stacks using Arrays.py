class Stack:

    def __init__(self):
        self.array = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.array[-1]

    def push(self, value):
        self.array.append(value)
        self.length += 1

    def pop(self):
        self.array.pop()
        self.length -= 1

my_stack = Stack()
my_stack.push("1")
my_stack.push("2")
my_stack.push("3")
my_stack.pop()
print(my_stack.peek())
print(my_stack)




