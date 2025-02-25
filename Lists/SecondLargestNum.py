# find the second largest Number in list!

""" 
plan 
- read in user input 
- only accept numbers 
- turn each strings of nubmers into int 
- turn string to list 
- operation to find the largest number first 
- pop the first largest number in new list
- in new list find the next second largest number in list
- print old list with the new list of second largest number

"""

import string

def ListOperation(SecondLargestNum):
    fnum = 0
    Snum = 0
    numholder = 0
    
    for j in range(2):
        if j == 0:  # First loop to find the largest number
            for i in SecondLargestNum:
                if i > fnum:
                    fnum = i  # Update fnum to the largest number
                    print(fnum)
                else:
                    continue
            numholder = fnum  # Store the largest number in numholder
        else:  # Second loop to find the second largest number
            for i in SecondLargestNum:
                if i != numholder and i > Snum:  # Only update Snum if i is not equal to fnum
                    Snum = i  # Update second largest number
                    print(Snum)
                else:
                    break  # Break after finding the second largest once
    
    return Snum  # Return the second largest number

"""
 for j in range(2):
        if j == 0:
            for i in SecondLargestNum:
                if i > fnum:
                    fnum = i
                    print(fnum)
                else:
                    continue
            numholder = fnum
        else:
            for i in SecondLargestNum:
                if numholder > Snum:
                    Snum = i
                    print(Snum)
                else:
                    break   
    return(Snum)
            # Figurre out how to pop the first largest number and then find the second largest number. maybe try a list comprhsension and maybe write down each process of the code 

"""
   
        

def UserInput():
    while True:
        UserInput = input("Please enter numbers only: ") # take in user input 
        if any(i in string.punctuation or i.isalpha() for i in UserInput): # iterable loop to check each char in string for a special symbol or letter
            print("No special characters or letters. Try again.")
            continue #next interation
        else:
            UserInput = [int(i) for i in UserInput.split()] # list compenshion take each string value and turn it into a int for new list.
            # split() divided each substring into a subset of string 
            break
    return(UserInput)


def main():
   numbers = UserInput()
   print(ListOperation(numbers))

if __name__ == "__main__":
    main()