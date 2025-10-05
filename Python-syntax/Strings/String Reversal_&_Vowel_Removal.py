#String Reversal_&_Vowel_Removal.py
#Write a program that takes an input string, removes all vowels, and then reverses the resulting string. 

def vowels(word: str) -> str:
    vowelL = ['i','o','u','a','e','A','E','I','O','U'] #list of vowels
    newword = "" # make a string to put in new letters
    for letter in word: # loop for each letter in word
        if letter not in vowelL: # if letter not a vowel 
            newword += letter# add to new word
    return(newword)

""" 
for letter in range(len(word)):
        if word[letter] not in vowelL:
            newword += word[letter]
    return(newword)
"""      

#def rev(word: str) -> str:
    #return(word[::-1]) # string slicing to reverse word
   

def rev(word: str) -> str:
    revword = '' # empty string
    for i in range(len(word) - 1, -1, -1):  # Iterate backward
        revword += word[i]
    return (revword)  # Return the reversed word

 
print(rev(vowels(input("Please enter in a word: \n"))))


# learn that you got to make a empty string before you tranfer a new letter into it.
# strings are immutable 
# accessing string and list through Var[i]
# strings in loops you need the length you can just put range(word) bc its not a int

"""
I learned how to remove vowels from a word by iterating through the string and building a new string with only non-vowel characters. 
I also explored using range() to loop through a string by index, which gives me more control over how I access characters. 
I implemented string reversal by iterating backward through the string and concatenating each character. 
Finally, I combined both functions to first remove vowels and then reverse the resulting string, demonstrating how to compose multiple functions for a more complex result.

"""