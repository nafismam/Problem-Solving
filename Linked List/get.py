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
    
    # to get the value from a certain index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    
my_linked_list = LinkedList(2)
my_linked_list.append(121)
my_linked_list.append(25)
my_linked_list.append(32)

print(my_linked_list.get(2))
