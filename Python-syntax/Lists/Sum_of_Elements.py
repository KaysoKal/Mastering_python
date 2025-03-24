# Write a function that takes a list of numbers and returns their sum (without using sum()).
def UserInput():
    while True:
        string1 = input("Enter a list of Numbers: ")  # User enters a string of numbers

        # Check if input contains any letters
        if any(char.isalpha() for char in string1): # any checks one by one in the string if any char is a letter
            print("Only numbers are allowed")
            continue  # Restart loop if letters are found

        # Process valid input
        if "," in string1:
            string1 = string1.split(",")  # Split using commas
        elif " " in string1:
            string1 = string1.split()  # Split using spaces
        else:
            print("Try again, need spaces or a comma after each number or you only enter in one number!")
            continue  # Restart loop if no valid separator is found
        
        # Exit the loop if input is valid
        break  
    return sumofnum(string1) # Calls sumofnum to calculate the sum and returns it to the caller

#

def sumofnum(string1):
    sum = 0
    for i in range(len(string1)): #range only interperts integers so need to use a len to use a loop
        string1[i] = int(string1[i]) # change the value to a int
        sum += string1[i]
    return(sum) # Return the calculated sum to the calling function
                

def main():
    result = UserInput()  # Calls UserInput to get the sum and stores it in 'result'
    print(f"The total Sum: {result}")

    

if __name__ == "__main__":
    main()
    #Completed 
