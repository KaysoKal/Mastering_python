# trying all methods of strings and use cases i would use them withe the syntax. 
# things i learned with my other coding project into here as well 
# STRINGS ARE IMMUTABLE  & they are a sequence of characters 


def Slicing_Concatenation_escapeChar(text):
    # all strings starting positions when slicing start at zero 
    # return a portion of the word depending on the user
    # You will use list brackets to slice a string
    # The space before the colon is the start pos. and after the colon is the end pos. Third position is the step 
    #step is the count if you want get certain letter in a pattern by 2 ,3s or maybe 4
    print(text[::-1])
    
    #Concatenation
    # is adding strings together 
    # you can also multiple a string which will mutple the text by that #
    print(text + text)
    
    # f string use to add a varables to a string
    print(f"Math is the {text}")
    
    #escape characters always begin with a slash 
    #\n is new line, \t is a tab space, \b backspace
    
def string_Manipulation(text2,text3):
    # understanding string manipulations
    print(text2.isalpha(),text3.casefold()) # converts first letter to uppercase, like lower() but convert even intentional char to lower case
    text2, text3 = text2.lower(),text3.upper() # turn string chars to all upper or lower case
    #center(#), center the strings the number you choose
    #count("value",start,end), count how many times a word occurs in a a string also you can position where to search 
    #encoded() encode the string in a code convert string into bytes
    #find() Find the value you looking for and return postition of value can start and end at the position
    # index() find where the value of your chose and return the index
    #format() allow you put curly brackets inside a string value and change them values in side the string 
    # handy bc strings are not muttable 
    text4 = "I {word} you".format(word="Love") # also format types
    print(text4)
    
    #Boolean types True or false
    #isalnum return if strings in in alphacic num order
    #isalpha # true if all letter are alphabet 
    #istitle True if each text start with a upper case letter
    #isupper or islower return true if its upper or lower case letter in the text
    print(text3.istitle())
    


    
    

# To define strings 
def stringsKnowledge():
    # to defining a string and assign a variable 
    # a string is text, word, letters even numbers anything in '' or "" is consider a string
    # multiline strings use for a long text Would use """ """ like muttiline comments 
    text = "hello world"
    print(text,"\n")
    
    #checking if a word or letter is in the text   # for checking if it isn't then use Not
    print("h" in text, "\n")
   
    
    
    # to get length of strting (how many chars are in the text including the spaces)
    textL = len(text)
    print(text,textL, "\n")
    
    # Looping through a string there are two ways
    # first way is through each letter 
    
    for index, letter in enumerate(text): #emuerate let you loop through iterable while also getting the index
        print(index, letter) 
        
    # The second way is the range function  using the length cant use a string bc you will have error of looping a string trying to be interpeted as a int
    for i in range(textL):
        print(i, end=" ") # end is to stop printing a new line 
        

def StringsWithLists():
    LastText = "Testing this strings"
    LastText2 = "laugheriswonderful"
    listTest = LastText.split(" ")
    #Strings with List methods
    #join
    #swapcase swap upper case letter to lower letters and lower letters do the same for upper letters
    print(LastText.split(" ")) # split turn a string into a list you can choose how to separate the string
    print(LastText2.strip("l,a")) # remove trailing or leading characters 
    print(" Yes".join(listTest))
    print()
    
    
def main():
    text = "Test Subject"
    text2, text3 = "dog123abc", "DOG321ABC"
    #stringsKnowledge()
    #Slicing_Concatenation_escapeChar(text)
    #string_Manipulation(text2,text3)
    StringsWithLists()

if __name__ =="__main__":
    main()