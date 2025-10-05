"""
Intermediate Level: Filter Elements in a Set
Problem:
Write a function that:

Takes a set of integers.
Filters out all the even numbers.
Returns a new set containing only the odd numbers.
Hint:

Use the filter() function or a set comprehension to filter elements based on conditions (in this case, odd numbers).
Goal:

Learn how to filter elements from a set using built-in functions like filter() or using set comprehensions.
"""

def User_input():
    while True: #A continous loop for the input statment 
        User_input = input("Please enter in a list of numbers: ")# this is a string. Prompt users to enter a list of numbers
        try:
            The_list = [int(num) for num in User_input.split()] #list comprehnsion. turn string to list and turn it into a int based off whitespace 
            return The_list  
        except ValueError: # if It not a int 
           print("Only numbers can be enter")
           
    

def Isodd(num):  
    return num % 2 != 0  # Returns True for odd numbers, False for even numbers

def Filiter_list(The_list):
    The_list_update = set(filter(Isodd, The_list)) # The Function filiter(function, iterable) the function filter through a list,tuple etc
    print(The_list_update)

    

        
def main():
    The_list = User_input()
    Filiter_list(The_list)

    
    
    

if __name__ == "__main__":
    main()