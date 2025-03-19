"""
Medium: Dictionary Iteration & Manipulation
Print all keys and values in the dictionary in a formatted way.

Check if a specific item exists in the dictionary before accessing it.
Increase all prices by 10% and update the dictionary.
Count how many items in the dictionary have a price greater than $5.
Merge two dictionaries containing food items and their prices. (update)
"""


def main():
    my_dict_fruits = {"Apples": 1.30 , "Bananas": 0.90 , "Oranges": 0.50}
    
    for keys , values in my_dict_fruits.items(): # items turn it into a tuple. Tuple is a constant, can access index
        pass
        #print(f"{keys}, ${values:.2f} ") 
        
        
  
# if any(key.casefold() == "apples".casefold() for key in my_dict_fruits): any is faster is stops once it find it match
# learn more about generator expressions
    if "apples".casefold() in (key.casefold() for key in my_dict_fruits): # in  goes through all after it find it match 
        for item in my_dict_fruits:
            price_increase = my_dict_fruits[item] * (10/100)
            my_dict_fruits[item] += price_increase
            
        for food, prices in my_dict_fruits.items():
            print(f"{food} {prices:.2f}")
        
            
        
    

  
       

if __name__ == "__main__":
    main()