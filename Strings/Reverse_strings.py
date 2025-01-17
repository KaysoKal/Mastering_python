"""
Reversing words in a sentence is straightforward and focuses on basic string manipulation
project that teaches you how to manipulate words within a string. 
"""


def Rev_string(word :str) -> str: # make a function that takes in a word return a word
        return(word[::-1]) # slicing the string while revseing the index step -1
    
def Rev_string2(word :str) -> str: # slicing using indexes 
    start ,end = 0 ,-1
    return(word[len(word)::-1])

def Rev_string3(word :str) -> str:
    revword = ' ' # empty string to put the characters in rev
    for i in range(len(word) -1,-1, -1): # loop to rev the string 
        #start is word - 1 which it will start at the end of the string
        #end is it will stop looping at 0
        #step for -1 means the loop will go backwards
        revword += word[i] # accssing a speific character in the sting or list
    return revword

#print(Rev_string(input("Type in a word you want to reverse? "))) #input from user is the argument while calling the fuction 
print(Rev_string2(input("Type in a word you want to reverse? "))) 