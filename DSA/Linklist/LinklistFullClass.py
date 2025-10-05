# Template for a node in a linked list
class LinkedListNode:
    def __init__(self, val, nextNode=None):
        self.val = val                # the value stored in the node
        self.nextNode = nextNode     # reference to the next node (default is None)

# Class for managing the linked list
class LinkedList:
    def __init__(self, head=None):
        self.head = head             # the head is the first node in the list

    # Insert a new node at the end of the list
    def insert(self, value):
        node = LinkedListNode(value)  # create a new node with the given value
        if self.head is None:
            self.head = node          # if list is empty, new node becomes head
            return
        
        currentNode = self.head       # start from the head
        
        while True:                          # loop forever
            if currentNode.nextNode is None:  # if no next node
                currentNode.nextNode = node   # connect the new node here
                break                         # we're done, stop looping
            else:
                currentNode = currentNode.nextNode  # otherwise, keep walking to the next node

    # Print the linked list values
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(f"{currentNode.val} ->", end=" ")
            currentNode = currentNode.nextNode
        print("None")  # end of list


# Create a new linked list
myList = LinkedList()

# Insert some values
myList.insert(10)
myList.insert(20)
#myList.insert(30)

# Print the list
myList.printLinkedList()

    