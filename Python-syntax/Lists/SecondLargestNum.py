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
    largest = 0
   
    for num in SecondLargestNum:
        if num > largest:
            second_largest = largest  # Update second_largest before largest
            largest = num  # Update largest
        elif num > second_largest and num != largest:
            second_largest = num  # Update second_largest if num is not equal to largest

    return second_largest  # Return the second largest number

""" 
    for j in range(2):
        if j == 0:  # First loop to find the largest number
            for i in SecondLargestNum:
                if i > fnum:
                    fnum = i  # Update fnum to the largest number
                else:
                    continue
            numholder = fnum  # Store the largest number in numholder
        else:  # Second loop to find the second largest number
            for i in SecondLargestNum:
                if i != numholder and i > Snum:  # Only update Snum if i is not equal to fnum
                    Snum = i  # Update second largest number
                else:
                    break  # Break after finding the second largest once
    
    return Snum  # Return the second largest number


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
 #Completed 
