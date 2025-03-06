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

def Filiter_set():
    while True:
        The_set = input("Please enter in a list of numbers: ") # this is a string
        The_set = The_set.split()
        # you having mistakes in any and list comprehsinsion remeber that the set start as a string first
                
        print(The_set)
        

        

    
        """ 
            
            for i in The_set:
                if i % 2 != 0:
                    return True
                
                else:
                    return False
        break
    
    The_set = filter(Filiter_set,The_set)
    

            """
def main():
    Filiter_set()

if __name__ == "__main__":
    main()