

class Node: # repsent a single element in the link list 
    def __init__(self, data):
        self.data = data #2.)  once we append a number a new node is created with data[10 | None]
        self.next = None # the pointer , refernece the next node
          
# link list class mangaged the chain of nodes 
class LinkList:
    def __init__(self):
        self.head = None # 1.) start of the list no node dont eaxist yet
        
    def append(self, data): # adding new node at the end
        new_node = Node(data) # create a new node with the given data
        
        if not self.head: # if list is empty 
            self.head = new_node
            return 
        
        current = self.head # start from the head of the list a temp node 
        while current.next: #transvere until the last node 
            current = current.next #moves pointer to the next node
        current.next = new_node # link the new node to the end of the list

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
       
def main():
    listpractice = LinkList() #create a empty list
    listpractice.append(10)
    listpractice.append(20)
    listpractice.display()

if __name__ == "__main__":
    main()
    
