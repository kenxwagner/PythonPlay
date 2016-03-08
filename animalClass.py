import random
import sys
import os
 
class Animal:
    # private variable start with __
    __name = None
    __height = None
    __weight = None
    __sound = None
 
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
 
    def set_name(self, name):
        self.__name = name
 
    def set_height(self, height):
        self.__height = height
 
    def set_weight(self, height):
        self.__height = height
 
    def set_sound(self, sound):
        self.__sound = sound
 
    def get_name(self):
        return self.__name
 
    def get_height(self):
        return str(self.__height)
 
    def get_weight(self):
        return str(self.__weight)
 
    def get_sound(self):
        return self.__sound
 
    def get_type(self):
        print("Animal")
 
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)
 
#Here's the object
cat = Animal('Space Cat', 33, 10, 'Worship me')



 
print(cat.toString())
cat = Animal('Mikey', 39, 8, 'Pet Me')
print(cat.toString())
dog = Animal('Maddie', 82, 26, 'Throw the ball')
print(dog.toString())
elephant = Animal('Jumbo', 4038, 7124, 'Look out')
print(elephant.toString())
 
class Dog(Animal):
    __owner = None
 
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None
 
   #calling super class
        super(Dog, self).__init__(name, height, weight, sound)
 
    def set_owner(self, owner):
        self.__owner = owner
 
    def get_owner(self):
        return self.__owner
 
    def get_type(self):
        print ("Dog")
 
    # Overwrite functions
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), 
											self.get_height(), 
											self.get_weight(), 
											self.get_sound(), 
											self.__owner)
 
   #overloading the method
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)
 
samson = Dog("Samson", 117, 98, "Woof", "Nature")
 
print(samson.toString())
print("Thanks for playing!")

                
