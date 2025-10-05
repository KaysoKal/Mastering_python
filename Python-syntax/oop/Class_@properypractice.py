class dog:
    def __init__(self, name: str, breed: str):
        self.name = name #define public attribute
        self.__breed = breed # define private attribute

    @property #getter for breed
    def breed(self): #methdod to get breed
        #def get_breed(self): could be define as this without using @property
        """Get the breed of the dog."""
        return self.__breed # return breed to instance

    @breed.setter #setter for breed
    def breed(self, user_input):
        #set_breed(self, user_input): could be define as this without using @breed.setter
        self.__breed = user_input
        print(self.__breed) # print breed to terminal 


def main():
    dog_type = dog("luffy", "germanshepard") # call dog class and pass in parameters
    print(dog_type.name, dog_type.breed)
    dog_type.breed = "pug" # change breed using setter
   
   
if __name__ == "__main__":
    main()