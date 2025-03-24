# A function that checks if a word is a palindrome (i.e., it reads the same forwards and backwards)
def palindrome_chcker(palindrome):
    # Convert the input string to lowercase to ensure case-insensitive comparison
    palindrome = palindrome.casefold()
    
    # Create a variable 'unique_word' to store the reversed version of the input word
    unique_word = ""
    
    # Reverse the input word and assign it to 'unique_word'
    unique_word = palindrome[::-1]
    
    # Check if the reversed word is the same as the original word
    if unique_word == palindrome:
        # If they are the same, print that it's a palindrome
        print(F"{True} A palindrome: {unique_word}")
        print(F"The word you entered: {palindrome}")
    else:
        # If they are not the same, print that it's not a palindrome
        print(F"{False} Not a palindrome: {unique_word}")  
        print(F"The word you entered: {palindrome}")

# Prompt the user to enter a word to check if it's a palindrome
palindrome_chcker(input("Please enter a word to test palindrome: "))
