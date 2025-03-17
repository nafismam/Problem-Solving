class Node:
    def __init__(self, value):
        #prottek bar na kore just ei class takey daak dibe
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        #create a node
        new_node = Node(value) #call previous node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # printlist function
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # Append in the end 
    def append(self, value):
        new_node = Node(value)    
        #what if the linked list is 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # tail er porer ta new node
            self.tail.next = new_node
            # new node er upor tail jabe
            self.tail = new_node
        # increase length by one
        self.length += 1
        # optional, stand alone e dorkar nai but 
        # onno method e call korle true ba false return kora lagbe
        return True
    
    # Pop from last
    def pop(self):
        if self.length == 0:
            return 
        
        # initialize
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            # eta hobe until kichu thakbena
            temp = temp.next
            # so pre hobe second ast ta
        self.tail = pre #second last pre
        self.tail.next = None #pop out last
        self.length -= 1

        # 1 ta thakle 0 howar por
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

my_linked_list = LinkedList(1)
my_linked_list.append(22)
print("Before:")
my_linked_list.print_list()

print("After:")
my_linked_list.pop()
my_linked_list.print_list()

print("After:")
my_linked_list.pop()
my_linked_list.print_list()