#print list method

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printList(self):
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
            #new node takey porer ta banabo 
            #then next takei tail banabo
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length + 1
        
my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)

my_linked_list.printList()


        