#hash set/maps Implementation
#pyhton methods

#Hash map is implemneation like an array

"""
hashmap 
------------
|index | key, value|
- index map to key value pair
- empty hashmap is non zero

hashmap - is a dynmaic array
hashmap is having a way to convert a key to a integer and use that integar as a index
then find where to put that key value pair into our array
- in other words you are putting that key value pair dictionary making a key a index then putting into another way with index and the dictionary key and value

mod by the size of the index of the array to get any intger to get to a valid index

hashing collsion - A collision happens when two different inputs (keys) produce the same hash value (index) in a hash table
- before the second input resize the array by double to avoid it if half fulled. But you got back to your first input and rehash it for the new array size.

different ways for handle collision
- store a link list of pairs (chaining)
- open addressing - is trying the next available position to insert an input

video left off at 20.00 on Neetcode

"""

class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val - val
        
class HashMap:
    def __init__(self):
        self.size = 0
        self.capcity = 2
        self.map = [None, None]
        
def hash(self, key):
    index = 0
    for c in key:
        index += ord(c)
    return index % self.capacity

def get(self, key):
    index = self.hash(key)
    
    while self.map[index] != None:
        if self.map[index].key == key:
            return self.map[index].val
        index += 1
        index = index % self.capacity
    return None

def put(self, key, val):
    index = self.hash(key)

    while True:
        if self.map[index] == None:
            self.map[index] = Pair(key, val)
            self.size += 1
            if self.size >= self.capacity // 2:
                self.rehash()
            return
        elif self.map[index].key == key:
            self.map[index].val = val
            return
        
        index += 1
        index = index % self.capacity
        
def remove(self, key):
    if not self.get(key):
        return
    
    index = self.hash(key)
    while True:
        if self.map[index].key == key:
            # Removing an element using open-addressing actually causes a bug,
            # because we may create a hole in the list, and our get() may 
            # stop searching early when it reaches this hole.
            self.map[index] = None
            self.size -= 1
            return
        index += 1
        index = index % self.capacity
        
def rehash(self):
    self.capacity = 2 * self.capacity
    newMap = []
    for i in range(self.capacity):
        newMap.append(None)

    oldMap = self.map
    self.map = newMap
    self.size = 0
    for pair in oldMap:
        if pair:
            self.put(pair.key, pair.val)
            
def print(self):
    for pair in self.map:
        if pair:
            print(pair.key, pair.val)
        