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

def Union(SetA, SetB: set) -> set:
    return SetA.union(SetB)
 

def intersec(SetA, SetB: set) -> set:
     return SetA.intersection(SetB)
     #return SetI
    

def diff(SetA, SetB: set) -> set:
    return SetA.difference(SetB), SetB.difference(SetA)
    

def symmetric():
    pass


def main():
    SetA = {1, 2, 3, 4, 5}
    SetB = {4, 5, 6, 7, 8}
    print(f"Union of Both sets:",Union(SetA, SetB))
    print(f"Intersection of Both sets:",intersec(SetA, SetB))
    SetDA, SetDB = diff(SetA, SetB)
    print(f"Difference of A - B: {SetDA}\nDifference of B - A: {SetDB}")
    # note when you separate mutiple values python turn it into tuple when printing getting unhashable type error
    # create a user input set and try using a filiter and add and remove 
    

if __name__ == "__main__":
    main()