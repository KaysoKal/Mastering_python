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
        
        # rule of thumb when meaniplationg existing linklist use a dummy node 
        
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
    
"""
always have a head pointer to transver or modify the list 
use dummy nodes when need for merging, inserting an reording nodes for edge cases
travers using .next and be carefeul bc it can change the orginal strucure of the list so use temp
when reversing the list always use three pointers 
while condition use tq to process every node including last one 
use node.next when wanting to attach somehting to the last node in list


Think of a bookmark in a book 📖:

The book = the linked list.

The bookmark = your pointer (current).

The page you want to attached (current.next = page)

When you move the bookmark (current = current.next), the book’s content hasn’t changed — only where you’re looking.

So a pointer is just a way of keeping track of a position in the linked list without copying the whole thing.

✅ Analogy with a train

current = current.next → You walk forward to the next train car. 🚶

current.next = current.next.next → You unhook a train car and attach the engine directly to the car after it. 🚂

👉 So the key difference:

= on the left side is .next → you are changing the list structure.

= on the left side is just a pointer variable → you are moving your finger along the list.
"""