"""
Medium: Dictionary Iteration & Manipulation
Print all keys and values in the dictionary in a formatted way.

Check if a specific item exists in the dictionary before accessing it.
Increase all prices by 10% and update the dictionary.
Count how many items in the dictionary have a price greater than $5.
Merge two dictionaries containing food items and their prices. (update)
"""


def main():
    my_dict_fruits = {"Apples": 2.30 , "Bananas": 4.90 , "Oranges": 4.50}
    my_dict_vegetables = {"Carrots": 3.00, "Potatoes": 2.50}
    
    print("The orginal prices")
    for keys , values in my_dict_fruits.items(): # items turn it into a tuple. Tuple is a constant, can access index
        print(f"{keys}, ${values:.2f} ") 
        
        
  
# if any(key.casefold() == "apples".casefold() for key in my_dict_fruits): any is faster is stops once it find it match
# learn more about generator expressions


    item_to_check = "Apples" 
    count = 0 # initialize for count prices > 5
    if item_to_check.casefold() in (key.casefold() for key in my_dict_fruits): # in  goes through all after it find it match 
        print(f"found {item_to_check} in dictionary!")
        for item in my_dict_fruits:
            price_increase = my_dict_fruits[item] * (10/100)
            my_dict_fruits[item] += price_increase
            if  my_dict_fruits[item] > 5:
                count += 1
                
         # Printing updated dictionary
        for food, prices in my_dict_fruits.items():
            print(f"{food} {prices:.2f}")

    # Merging dictionaries
    my_dict_fruits.update(my_dict_vegetables)
    print(my_dict_fruits)
    
# note break the main function down into smaller steps
# functions user input, checking if a item exist in a dict, increase all prices by 10%, counting all items greater then 5 dollars, update dict
  
       

if __name__ == "__main__":
    main()