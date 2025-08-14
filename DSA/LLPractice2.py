class Node:
    # all need a value and a pointer 
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = None # 
        
    def append(self,data):
        #create a new node 
        newNode = Node(data)
        
        if self.head is None: # saying if its empty 
            self.head = newNode
            return
        
        #transvering the list
        #current is the tempary nod you move through out the list we did that with head we would lose it
        # think of equal sign as pointing to something from right to left 
        # current = im pointing to this node 
        # current.next = newnode mean im attaching new node to this node 
        current = self.head 
        while current.next: # keeping going to the next node as long as there is one
            current = current.next # walk through the list , move current to next node in the list 
        current.next = newNode #once current.next is point to last node, mae it next point to new node and now new node is at the end 
        
        
        #print the LL
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ->")
            current = current.next
        print("None")

def main():
    LL = LinkList()
    LL.append(10)
    LL.append(20)
    LL.display()
        
        
if __name__=="__main__":
    main()