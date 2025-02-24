#Sum_of_Even_Numbers

import string

def Sum_of_Even_num(even):
    even_list = [num for num in even if num % 2 == 0]
    return(f"The Numbers entered: {even_list} \nThe sum: {sum(even_list)}")


def main():
    while True:
        random_list2 = input("Enter a list of numbers: ")
        
        # Fix: Check if any character is punctuation or a letter
        if any(i in string.punctuation or i.isalpha() for i in random_list2):
            print("No special characters or letters. Try again.")
            continue

        else:
            random_list2 = [int(i) for i in random_list2.split()]
            break  # Exit loop if successful   
        
    print(Sum_of_Even_num(random_list2))

if __name__ == "__main__":
    main()

    
#notes list comprhension
"""
When doing list comphrension 
expression The operation perfroming on each item 
item: a varabible represent each element 
iterable: what you looping with tuple, list, dict, string
condition: what you filtering for the expresion 
ex: example = [expression for item in iterable if condtion]
example = [int(i) for i in range(len(text)) if i < 5]
int(i) is the expression
i is the item 
iterable is text
condtion is the if statement 

To get each number individually, input which it would be a string. Then make a compehision list with  condition as if i != " " which each number/or char is split up
but to group numbers or text as substring use split()

"""