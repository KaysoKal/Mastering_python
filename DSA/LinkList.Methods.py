class Node: # define the node class
    def __init__(self,val, Next = None):
        self.val = val # element being stored 
        self.Next = Next # a pointer to the next element 
        
class LinkList: # chaining the link list 
    def __init__(self):
        self.head = None #creating the head node # head points to none
        
    def Insert_at_beginning(self,val):
        newNode = Node(val,self.head) # create a new node with val and have it point to self.head 2 arg which is none!!
        self.head = newNode # self head point to new node 
            
    
    def Insert_at_end(self,val):
        if self.head is None:
            self.head = Node(val,None)
            return # end the code 
        
        curr = self.head # point curr to head 
        while curr.Next: # if curr is link to another node 
            curr = curr.Next # move pointer on to next link
        
        newNode = Node(val,None) #create a new node to attacch at then end of link list 
        curr.Next = newNode #attach the end of curr.next to the new node 
            
            
        
    
    def get_length(self):
        count = 0 
        curr = self.head
        while curr:
            count += 1
            curr = curr.Next
        return count
            
        
    
    
    def print(self):
        curr = self.head
        while curr:
            print(f"{curr.val} -->", end=" ")
            curr = curr.Next
        print(None)
            

            
    def get(self, index):
        curr = self.head
        i = 0
        if self.head is not None:
            while curr and i != index:
                curr = curr.Next
                i += 1
            return curr.val
        else:
            return("Empty list")
                
    def remove_at_index(self, index):
        if self.head is None:  # empty list
            return
    
        if index == 0:  # special case: remove head
            self.head = self.head.Next
            return

        prev = self.head
        i = 0
        while prev and prev.Next:   # stop at second-to-last safely
            if i + 1 == index:
                prev.Next = prev.Next.Next
                return # end the code 
            prev = prev.Next #connect 
            i += 1
            
                
                
            

    


def main():
    mylist = LinkList() # create a empty link list 
    mylist.Insert_at_beginning(10)
    mylist.Insert_at_beginning(20)
    mylist.Insert_at_end(5)
    #mylist.print()
    #print(mylist.get_length())
    #print(mylist.get(2))
    mylist.remove_at_index(2)
    mylist.print()
    
    

if __name__=="__main__":
    main()
        