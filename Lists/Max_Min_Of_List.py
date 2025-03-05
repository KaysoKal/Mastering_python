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
    text = [int(i) for i in text] # convert each string element into a int for the list 
    Highest_num = text[0] #set the highest number to the first index of list
    for i in text: # loop each value in list
        if Highest_num < i: # check if high number is less then value in list
            Highest_num = i #set value to new highest number
   

        else:
            continue # go to the next list value 
    return(Highest_num)

def MinNum(text):
    text = [int(i) for i in text]
    Lowest_num = text[0] #set the lowest number to the first index of list
    for i in text: # loop each value in list
        if Lowest_num > i:
            Lowest_num = i
            
        else:
            continue
    return(Lowest_num)


def main():
    result = UserInput()
    print(f"The Highest number is {MaxNum(result)}")
    print(f"The Lowest number is {MinNum(result)}")
    
if __name__ == "__main__":
    main()
    #Completed 
