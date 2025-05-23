class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

myStack = Stack(4)

myStack.printStack()

