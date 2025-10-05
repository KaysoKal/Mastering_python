#find the number of times a specific word appears in a given text

def wordFreqnecy(sentence: str):
    
    sentence = sentence.split(" ") # separeting each word by space & putting it into a list
    unique_word = {} # to find words that are distinct 

    for word in sentence: # check each word in the list . data types are strings
        if word not in unique_word: # check if word in in the new dict
            unique_word[word] = 1 # add word and counter into dict
        else:
            unique_word[word] += 1 # just update the counter for reccuring word
            
    for keys, value in unique_word.items(): # loop both key and value in dict using items()
        print(f"{keys} occurs {value} times") # show in terminal 
    
    
    

wordFreqnecy(input("Enter a setence: \n"))
