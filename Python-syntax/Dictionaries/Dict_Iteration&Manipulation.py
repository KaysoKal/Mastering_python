"""
Medium: Dictionary Iteration & Manipulation
Print all keys and values in the dictionary in a formatted way.

Check if a specific item exists in the dictionary before accessing it.
Increase all prices by 10% and update the dictionary.
Count how many items in the dictionary have a price greater than $5.
Merge two dictionaries containing food items and their prices. (update)
"""
def Checking_items(dict1, dict2) -> dict:
    """
    Checks if a specific item (Apples) exists in dict1.
    If found, calls Price_increase() to update prices and merge dictionaries.
    """
    item_from_list = "Apples"  # Item to check in the dictionary

    # Convert all keys to lowercase and check if "Apples" (case-insensitive) exists
    if item_from_list.casefold() in (key.casefold() for key in dict1):
        Price_increase(dict1, dict2, item_from_list)  # Call function to increase prices
    else:
        print(f"Item {item_from_list} not found.")  # Print message if item is not found
       

def Price_increase(dict1, dict2, item_from_list):
    """
    Increases all prices in dict1 by 10%, rounds to 2 decimal places, 
    counts items with prices above $5, and merges dict2 into dict1.
    """
    count = 0  # Counter for items with prices above $5

    for item in dict1:
        dict1[item] = round(dict1[item] * 1.10, 2)  # Increase price by 10% and round to 2 decimal places
        if dict1[item] > 5:
            count += 1  # Increment counter if price is greater than $5
    
    dict1.update(dict2)  # Merge dict2 into dict1

    print(f"\nItem {item_from_list} was found.")  # Confirmation message
    
    # Print updated dictionary with formatted prices
    for key, value in dict1.items():
        print(f"{key}: ${value:.2f}")
        
    print(f"{count} items above $5.")  # Print count of items above $5
          

def main():
    """
    Initializes dictionaries, prints original prices, 
    and calls Checking_items() to process them.
    """
    my_dict_fruits = {"Apples": 2.30, "Bananas": 4.90, "Oranges": 4.50}  # Fruit prices
    my_dict_vegetables = {"Carrots": 3.00, "Potatoes": 2.50}  # Vegetable prices
    
    print("Original Prices:")  # Header for original price list
    
    # Print original prices with formatted output
    for keys, values in my_dict_fruits.items():
        print(f"{keys}: ${values:.2f}") 
        
    Checking_items(my_dict_fruits, my_dict_vegetables)  # Call function to check items and update prices
  
    
    """    
    
   
  
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
    
    
    """
    
    
# note break the main function down into smaller steps
# , checking if a item exist in a dict, increase all prices by 10%, counting all items greater then 5 dollars, update dict
  
       

if __name__ == "__main__":
    main()
