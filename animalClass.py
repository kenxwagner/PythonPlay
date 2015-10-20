import random
import sys
import os

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    
    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height
        
    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound
        

    def get__name(self):
        return self.__name

    def get__height(self):
        return str(self.__height)

    def get__weight(self):
        return str(self.__weight)

    def get__sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)

cat = Animal('Mikey', 37, 8, 'Pet Me')
dog = Animal('Maddie', 81, 26, 'Throw the ball')
elephant = Animlal('Jumbo', 4038, 7124, 'Look out')

print (cat.String())
print (dog.String())
print (elephant.String())
