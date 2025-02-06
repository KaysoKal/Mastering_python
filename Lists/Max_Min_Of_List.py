# Find the Maximum & Minimum of a list

import string
def UserInput():
    while True:
        text = input("Please enter in a list of numbers: ")
        if any(char in string.punctuation for char in text):
            print("There should be no special character, Try Again")
            
        elif any(char.isalpha() for char in text):
            print("There should be no letters Try Again")
            
        else:
            text = text.split()
            break
    return text
 
    

def MaxNum(text):
    return(text)

def MinNum(text):
    pass


def main():
    result = UserInput()
    print(MaxNum(result))
    print(MinNum(result))

if __name__ == "__main__":
    main()