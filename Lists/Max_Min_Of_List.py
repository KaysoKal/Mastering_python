# Find the Maximum & Minimum of a list

import string
def UserInput(): # create a function for user input 
    while True: # contineous loop 
        text = input("Please enter in a list of numbers: ")
        if any(char in string.punctuation for char in text): # check for any input have a punctuation
            print("There should be no special character, Try Again")
            
        elif any(char.isalpha() for char in text): # check for any letters in text
            print("There should be no letters Try Again")
            
        else:
            text = text.split() # change string to list 
            break # break the loop!

    return text
 
    

def MaxNum(text):
    text = [int(i) for i in text] # change each string of i into a int for the list 
    Highest_num = text[0]
    for i in text:
        if Highest_num < i:
            Highest_num = i
   

        else:
            continue
    return(Highest_num)

def MinNum(text):
    text = [int(i) for i in text]
    Lowest_num = text[0]
    for i in text:
        if Lowest_num > i:
            Lowest_num = i
            
        else:
            continue
    return(Lowest_num)


def main():
    result = UserInput()
    print(f"The Highest number is {MaxNum(result)}")
    print(f"The Lowest number is {MinNum(result)}")
    
    # u any all and punction to put in notes and how to update branch 
    # notes on using a list cophemison and understanding the differece in (i) and [i] when usign a loop and the difference loops to use for a string and a list!!!

if __name__ == "__main__":
    main()