"""
Perform Set Operations and Combine Results
Problem:
You are given two sets:
Set A: {1, 2, 3, 4, 5}
Set B: {4, 5, 6, 7, 8}
Write a program that:

Creates both sets.
Finds the union of both sets. X
Finds the intersection of both sets.
Finds the difference between Set A and Set B. only in one set and not the other 
Finds the symmetric difference between Set A and Set B. the result of diffrerence but together 
Returns all the results as individual sets.
"""


def Uinput():
    # Prompt the user for the first list of numbers
    while True:
        try:
            Userinput1 = input("Please First list of numbers: ")  # Get a string of numbers
            Userinput1 = [int(x) for x in Userinput1.split()]  # Split the string into integers
            break
        except ValueError:
            # Handle case if the input is not a valid number
            print("Only numbers are allowed")
     
    # Prompt the user for the second list of numbers
    while True:
        try:
            Userinput2 = input("Please second list of numbers: ")  # Get a string of numbers
            Userinput2 = [int(x) for x in Userinput2.split()]  # Split the string into integers
            break
        except ValueError:
            # Handle case if the input is not a valid number
            print("Only numbers are allowed")
             
    return(Userinput1, Userinput2)  # Return the two lists


def DefineSet(SetA, SetB) -> set: 
    # Return formatted string showing set operations between two sets
    return(f"Union of Both sets: {SetA.union(SetB)}\n\nIntersection of Both sets: {SetA.intersection(SetB)}\n\nDifference of A - B: {SetB.difference(SetA)}\nDifference of B - A: {SetA.difference(SetB)}\n\nThe Symmetric_difference in both set togther: {SetA.symmetric_difference(SetB)}")


def Uni(UsetA, UsetB: list) -> set:
    # Combine the two sets (union)
    UsetA, UsetB = set(UsetA), set(UsetB)  # Convert the lists to sets
    for i in UsetB:
        UsetA.add(i)  # Add elements of UsetB to UsetA
    return(UsetA)  # Return the resulting union


def intersect(UsetA, UsetB: list) -> set:
    # Find the intersection of two sets
    intersectSet = filter(lambda num: num in UsetA, UsetB)  # Filter elements from UsetB that are also in UsetA
    # Filter (function, iterable) applies a function to each element in iterable
    # lambda - a function without defining
    
    return set(intersectSet)  # Return the intersection as a set


def UdiffA_B(UsetA, UsetB: list) -> set:
    # Find the difference between two sets (A - B and B - A)
    DiffA = set(filter(lambda num: num not in UsetB, UsetA))  # Elements in UsetA but not in UsetB
    DiffB = set(filter(lambda num1: num1 not in UsetA, UsetB))  # Elements in UsetB but not in UsetA
    return (DiffA, DiffB)  # Return both differences


def USymA_B(UsetA, UsetB: list) -> set:
    # Find the symmetric difference between two sets (elements in either A or B, but not both)
    SymA = list(filter(lambda num: num not in UsetB, UsetA))  # Elements in UsetA but not in UsetB
    SymB = list(filter(lambda num1: num1 not in UsetA, UsetB))  # Elements in UsetB but not in UsetA
    for i in SymB:
        SymA.append(i)  # Append elements of SymB to SymA
    return set(SymA)  # Return the symmetric difference


def main():
    # Create a user input set and try using filter, add and remove
    UsetA, UsetB = Uinput()  # Get two sets from user input
    print(f"Union from User input: {Uni(UsetA,UsetB)}")  # Display union of sets
    print(f"\nIntersection from User input: {intersect(UsetA, UsetB)}")  # Display intersection of sets
    
    UdiffA, UdiffB = UdiffA_B(UsetA, UsetB)  # Get differences of sets
    print(f"\nDifference A - B from User input: {UdiffA}\nDifference B - A from userinput: {UdiffB}\n")
    
    SymA = USymA_B(UsetA, UsetB)  # Get symmetric difference of sets
    print(f"Symmetric_difference from User input: {SymA}\n")

    # Define and display operations on predefined sets
    SetA = {1, 2, 3, 4, 5}
    SetB = {4, 5, 6, 7, 8}
    print(DefineSet(SetA, SetB))  # Show set operations on predefined sets
    

if __name__ == "__main__":
    main()  # Run the main function if this script is executed

