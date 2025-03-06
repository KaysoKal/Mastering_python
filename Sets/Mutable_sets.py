"""
Create a set of numbers from 1 to 10.
Add the number 11 to the set.
Remove the number 5 from the set.
Print the final set.
Goal:
Understand how to create sets, add elements using add(), and remove elements using remove() or discard().
"""
def Set_Operations():
    The_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # create the set 

    if 5 in The_set:   # check if value 5 in the set
        The_set.remove(5) # remove the value of 5 not index, some methods take either the value or index know your method and if it a list, tuple or set
        
    The_set.add(11)
    
    return(The_set) # return to main function 
    
    

def main():
    print(Set_Operations()) # call the function to print the statment 

if __name__ == "__main__":
    main()