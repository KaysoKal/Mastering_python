"""
Advanced Level: Perform Set Operations and Combine Results
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
     while True:
        try:
            Userinput1 = input("Please First list of numbers: ") # string of numbers
            Userinput1 = [int(x) for x in Userinput1.split()]
            break
        except ValueError:
            print("Only numbers are allowed")
     
     while True:
         try:
             Userinput2 = input("Please second list of numbers: ") # string of numbers
             Userinput2 = [int(x) for x in Userinput2.split()]
             break
         except ValueError:
             print("Only numbers are allowed")
             
     return(Userinput1, Userinput2)
         


def DefineSet(SetA, SetB) -> set: 
    return(f"Union of Both sets: {SetA.union(SetB)}\nIntersection of Both sets:{SetA.intersection(SetB)}\nDifference of A - B: {SetB.difference(SetA)}\nDifference of B - A: {SetA.difference(SetB)}\nThe Symmetric_difference in both set togther: {SetA.symmetric_difference(SetB)}")


def Uni(UsetA, UsetB: list) -> set:
    # filter through each list comebine them both together as one
    UsetA, UsetB = set(UsetA), set(UsetB)
    for i in UsetB:
        UsetA.add(i)
    return(UsetA)
    
def intersect(UsetA, UsetB: list )-> set:
    UsetA = sorted(UsetA)
    UsetB = sorted(UsetB)
    intersectSet = filter(func, zip(UsetA, UsetB))
    
    return set(pair[0] for pair in intersectSet)
   
    
def func(pair):
    # need to fix alorithm only if each element line up in each set
    i, j = pair
    return i == j
    
    
    
        
        


def main():
     # create a user input set and try using a filiter and add and remove 
    UsetA, UsetB = Uinput()
    print(f"Union from userinput: {Uni(UsetA,UsetB)}")
    print(f"testtting: {intersect(UsetA, UsetB)}")

    SetA = {1, 2, 3, 4, 5}
    SetB = {4, 5, 6, 7, 8}
    print(DefineSet(SetA, SetB))


    # use lambda for filter diffence or intersection
   
    

if __name__ == "__main__":
    main()
    
    
"""
  When a function returns multiple iterables in Python, they are combined into a tuple. This can lead to an 'unhashable type' error if the tuple is used in a context that requires a hashable type (e.g., as a set key).
  To solve this, assign multiple iterables to separate variables before using them in a set or another hash-sensitive operation
"""