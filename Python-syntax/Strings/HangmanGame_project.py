"""
Project One 
Create a word-guessing game where the player tries to guess a hidden word.


"""

import random
import string



def randomWordGen() -> str:
   my_list = ["apples", "bananas", "mangos"] # created a list 
   Hangmanword = random.choice(my_list) # use to choice a random word 
   word_length = len(Hangmanword) # get len of word
   chances = word_length + int(word_length * .5) # the chances they get 
   print(f"\nWelcome to hangman!\n\nThe word you are guessing have {word_length} letters.\n\nYou will have {chances} chances")
   guessFunction(word_length,chances,Hangmanword) # access for other function to use 
   
def guessFunction(word_len, chances,Hangmanword):
    HangmanwordL = list(Hangmanword) # list of letters from the word
    guessed_word = ["_"] * word_len # same amount of underscores as hangmanword
    guessed_letters = set() # remove duplicates of a occuring letter

        
    while True: # a while loop would be better then a for loop because because it would run forever until i break it
        #for loop interates only over a certein amount of times so not the best way about it
        
        print("\nCurrent word:", " ".join(guessed_word))  # Show current state of the word
        inputletter = input("Enter in a letter: ").lower() # user guess a letter
        
        if len(inputletter) != 1 or not inputletter.isalpha():  # if its not one letter come back and make a while loop until it true 
            print("Enter in a single valid letter and try again: ") 
            continue
                
        if inputletter in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(inputletter)  # Add to guessed letters
        
        if inputletter in HangmanwordL:  # If the letter is in the word
            print("Correct!")
    
            for i, letter in enumerate(HangmanwordL):  # Iterate through the HangmanwordL list with both index (i) and letter value
                if letter == inputletter:   # Check if the user's guessed letter matches the current letter
                    guessed_word[i] = inputletter   # If it matches, update the guessed_word list at the corresponding index
            if "_" not in guessed_word:  # Check if the word is completely guessed
                print("\nCongratulations! You guessed the word:", Hangmanword)
                break
        else:
            chances -= 1
            print(f"Incorrect. You have {chances} chances left.")
            if chances == 0:  # Out of chances
                print("\nYou lose. The word was:", Hangmanword)
                break
           
        
            
            # Break down this into more functions
            
   

    

def main():
    #LetterGuessing = input("")
    randomWordGen()

if __name__ == "__main__":
    main() # use to call main and organize the code structure 
    
