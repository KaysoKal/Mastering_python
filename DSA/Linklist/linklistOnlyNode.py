
class LinkedlistNode:
    
    def __init__(self, value, nextNode = None):
        self.value = value # get the value 
        self.nextNode = nextNode # points to next node
        
# you assign a value to node 
node1 = LinkedlistNode(3) 
node2 = LinkedlistNode(5)
node3 = LinkedlistNode(7)

# you connect the nodes 
node1.nextNode = node2 # 3 points to node 2 (5)
node2.nextNode = node3 # 5 points to node 3 (7)

#transvering the node
currentNode = node1 # current node is our head 
while True:
    print(f"{currentNode.value} ->", end=" ")
    if currentNode.nextNode == None:
        print(None)
        break
    currentNode = currentNode.nextNode # you set the current node you on to the next node so start the loop over again 

    