"""
Problem: Remove Duplicates from a List
Difficulty: Easy

Description: Write a Python function that accepts a list of integers as input and returns a set 
that contains only the unique elements of the list.
"""

def remove_duplicates(input_list: list) -> set:
    return(set(input_list))

def UserInput() -> set:
    while True:
        num_in_set = input("Enter in a list of numbers: ") 
        
        if not num_in_set.replace(" ", "").isdigit(): #is digits() is for 0-9 so used the  replace to remove the " " when having two or more digit inputs. 
            print("numbers only")
      
        else:
            num_in_set = num_in_set.split() # turns string into list 
            break # stop while loop 
    return(num_in_set) # return to the main function of user input 

                            
        

def main():
    print(remove_duplicates(UserInput())) 
    
 """
User input function (UserInput) returns num_in_set (the list of numbers) as the argument for the remove_duplicates function.
The duplicate function (remove_duplicates) receives that argument as the parameter (input_list), processes it, and returns a set that contains only the unique numbers (removing any duplicates).
 """

if __name__ == "__main__":
    main()