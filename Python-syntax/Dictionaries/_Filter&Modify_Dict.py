""" 
Problem:
You are given a list of dictionaries representing students' information, where each dictionary contains the following keys:

"name" (string)
"age" (integer)
"score" (integer)
Write a function to filter out students who are younger than 18 and have a score below 90, and return the names of the remaining students as a list.

You need to use filter(), map(), and lambda functions to solve this.


"""

def func(my_dict, min_age, min_score):
   my_dict_filter = filter(lambda x: x[1]['age'] > min_age and x[1]['score'] < min_score, my_dict.items())
   
   name_list = list(map(lambda x: x[1]['name'], my_dict_filter))
   print(name_list)



def main():
    #for key, value in my_dict.items():
        #print(key,value)
        
    my_dict = {
    1: {"name": "Alice", "age": 20, "score": 85},
    2: {"name": "Bob", "age": 22, "score": 90},
    3: {"name": "Charlie", "age": 21, "score": 78},
    4: {"name": "David", "age": 23, "score": 88},
    5: {"name": "Eva", "age": 20, "score": 92},
    6: {"name": "Frank", "age": 24, "score": 76},
    7: {"name": "Grace", "age": 22, "score": 95},
    8: {"name": "Hannah", "age": 21, "score": 80}
    }

    age = 22
    score = 90
    func(my_dict,age,score)



if __name__ == "__main__":
    main()