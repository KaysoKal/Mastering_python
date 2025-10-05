"""
Implement the function count_characters(word: str) -> Dict[str, int]. 
It should take a string word and return a dictionary with the count of each character in the word. 
The keys should be the characters and the values should be the count of each character.
"""



def count_characters(word: str) -> dict[str, int]:
    my_dict = {} # empty dict
    listracker = []

    lettersplit = [i for i in word] # split each letter and turn into list
    for i in lettersplit: # transverse the list by each letter
        if i not in listracker:
            counter = 1 # counter for letters
            my_dict[i] = counter # add count value to key as pair
            listracker.append(i) # tracks the letters and add to list

        elif i in listracker:
            # since letter is already in list tracker and keys cant have dupilcates
            counter2 = lettersplit.count(i) # count up all the same letter
            my_dict[i] = counter2  # set counter value as a pair to letter(key)
    return my_dict

def main():
    print(count_characters("hello"))
    print(count_characters("world"))
    print(count_characters("hello world"))
    print(count_characters("this is a longer sentence"))

if __name__ == "__main__":
    main()

