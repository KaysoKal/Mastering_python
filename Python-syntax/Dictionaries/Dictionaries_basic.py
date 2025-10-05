"""
Easy: Basic Dictionary Operations
Create a dictionary that stores three favorite foods and their prices.
Retrieve the price of one specific food item from the dictionary.
Add a new item to the dictionary with a price.
Update the price of an existing item in the dictionary.
Remove an item from the dictionary.
"""


def main():
    food_options = {"Apples": 1.30 , "Bananas": 0.90 , "Oranges": 0.50}
    
    print(f"Food options: {food_options}")
    print(f" The price of apples: {food_options["Apples"]}")
    # to get a something from a certain index
    first_pair = list(food_options.items())[0]
    print(first_pair)
    food_options["Grapes"] = (1.20)
    print(f"New Food options {food_options}")
    
    food_options.pop("Bananas")
    print(f"Updated food options: {food_options}")

if __name__ == "__main__":
    main()