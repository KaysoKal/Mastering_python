"""
Hashmaps are Dictionaries 

benfits:
custom keys are easier to find 
allow for search in O(1), and where as arrays/linked list are O(n)

How they work:
built of pre define dsa as array
hashmap is created from array through a hash function
- hashmaps are pre-built for you its good know how hash function work 

Coding hashmaps:
You always got to initialize the key for a dictionary before adding value or you get a error
city_map = {}
cities = ["tokyo", "yuko"]
city_map["japan"] = []
city_map["japan"] += cities

defaultdict is all keys are initialized

how to retreive data
hashmap.keys() , hashmap.values() , hashmap.itmes() 
https://www.youtube.com/watch?v=RcZsTI5h0kg
go back and watch how he did that group anagrams 49

dictionary keys must be immutable

write down 
- learn the science under the hood and the implenation over the hood 
- if you implenated like array you got to do everything under the hood
- but if you do the dict you have to do nothing extra
- how does it work from a 0 to 1 stand point


"""