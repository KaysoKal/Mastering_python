"""
Develop a Python program that determines whether two given strings are 
anagrams of each other. An anagram is defined as a word or phrase formed by 
rearranging the letters of another word or phrase, using all the original letters exactly once. 
The program should ignore letter case, spaces, and any special characters.
"""
import re

def Anagram(string1,string2):
    string1 = re.sub(r'[^a-zA-Z]', '', string1).casefold()  # Remove non-alphabet characters and lowercase
    string2 = re.sub(r'[^a-zA-Z]', '', string2).casefold()  # Remove non-alphabet characters and lowercase
    
    if string1.isalpha() and string2.isalpha():  # Check if both are now valid strings with only letters
        
        string1, string2 = string1.casefold() , string2.casefold() # ignore case sensitive
        unique_letters = [] # put each letter of string in list
        for letter in string1: # for each letter in string 
            unique_letters.append(letter) # add to unique list
    
        counter = 0 # Initialize a counter to track matching letters
        for letter2 in string2: # Loop through each letter in the second string
            if letter2 in unique_letters: # # Check if the letter exists in unique_letters
                counter += 1  # Increment the counter if the letter is found
                if counter == len(string2): # If all letters in string2 are matched
                    return("An Anagram")
            else: 
                return("Not an Anagram")
    else:
        return("Not all letters try again :(") 
            


def main():
    string1 = input("Please enter a word: ")
    string2 = input("Please enter second word: ")
   
    # Call the Anagram function and print the result
    print(Anagram(string1,string2))


if __name__ == "__main__":  # use to call main and run code in a organize structure 
    main()
    
#Things i learn sort function can be use to check if two strings are alike
# to remove speical characters import re and use re.sub()