#Reverse a list, do not use a [::-1] or reverse() 

def Rev_list(current_List):
    # Split the input string into a list of words (using whitespace as the delimiter)
    current_List = current_List.split()
    
    # Determine the number of elements in the list
    lengthList = len(current_List)
    
    # Initialize an empty list to hold the reversed elements
    backwardList = []
    
    # Start from the last index of the list
    i = lengthList - 1
    
    # Loop through the list in reverse order
    while True:
        # If the index is valid (i.e., not less than 0), append the element to backwardList
        if i > -1:
            backwardList.append(current_List[i])
            i -= 1  # Move to the previous index
        else:
            # Exit the loop once all elements have been processed
            break
            
    # Return the list of reversed elements
    return backwardList
        
    
def Rev_string(current_List):
    # Function placeholder for reversing a string; not yet implemented
    pass
    
    
def main():
    # Prompt the user to enter a word or number to be reversed
    current_List = input("Enter a word or number to be reversed: ")
    
    # Print the reversed list returned by Rev_list function
    print(Rev_list(current_List))
    
    # Additional functionality can be added here if needed
    pass

    
# This ensures that main() is executed only when the script is run directly
if __name__ == "__main__":
    main()

