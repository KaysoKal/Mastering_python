"""
Intermediate Level: Removing Items with a Loop Using pop()
Problem:
You are given a list of integers, and you need to:

Use a loop to traverse through the list.
Remove all even numbers using the pop() method.
After removing all the even numbers, append the remaining numbers to a new list.
Key operations to use:
pop() to remove elements during the loop.
append() to add the remaining numbers to a new list.
Completed 
"""
def Oddnums(listN: list[int]) -> list[int]:
    newList = []
    counter = 0
    
    # a quick way to do it
    # newList2 = [i for i in listN if i % 2 != 0] # list comprhension 

    for i in listN:  # Loop through each element in the input list
        newList.append(i)  # Add the current element to the newList
        
        if i % 2 == 0:  # If the current number is even
            newList.pop(counter)  # Remove the last added element from newList (which is the even number)
            
            continue  # If the number is odd, continue to the next iteration
        
        counter += 1  # Increment the counter to move to the next index in the list
        
    print(newList)
   
    

def main():
    List_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Oddnums(List_of_integers)

if __name__ =="__main__":
    main()
