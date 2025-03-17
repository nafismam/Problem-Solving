class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            if self.length == 0:
                self.head = None
                self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True
    
    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value
    
    def get(self, index):
        if index < 0 and index > self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

    def insert(self, index, value):
        if index < 0 and index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length-1:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.next = after
        after.prev = new_node
        before.next = new_node
        new_node.prev = before

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 and index > self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        before = self.get(index-1)
        after = before.next.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.before = None

        self.length -= 1
        return True

my_dll = DLL(7)
my_dll.append(10)
my_dll.append(11)

my_dll.remove(2)

my_dll.print_list()
# print(my_dll.popFirst())
          