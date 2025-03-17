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

    
    # def append(self, value):
    #     #create a node
    #     #ADD NODE to the end

    # def prepend(self,value):
    #     #create a node
    #     #add node to the beginning

    # def insert(self, index, value):   
    #     #create a node 
    #     #insert a node

my_linked_list = LinkedList(4) #this creates the 4 which is head and teal and length is 1
print(my_linked_list.head.value) #print the linked list


