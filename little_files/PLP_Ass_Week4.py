#PLP Assignment learning about OPP in python

#Creating a python class
class Person:
     # Constructor that initializes the class attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #Method
    def introduce(self):
        return f"This is {self.name}, {self.age} years old {self.gender}."

# Creating an instance of the Person class with attributes
person_one = Person("Ezekiel", 24, "male")
person_one.introduce()