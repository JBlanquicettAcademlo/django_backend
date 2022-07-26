


from abc import ABC, abstractmethod

class Person(ABC): # Abstract Base Class

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def say_hello(self):
        '''This method should be implemented by subclasses'''
        pass
    
    @abstractmethod
    def say_goodbye(self):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def __str__(self):
        return f"{self.name} {self.age}"



class Student(Person): # Inherits from Person

    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

        self.__is_enabled = True # Private variable

    def say_hello(self): # Overrides the superclass method Polymorphism
        return f"Hello my name is {self.name} and I am a student at {self.school}"

    def say_goodbye(self): # Overrides the superclass method Polymorphism
        return f"Goodbye my name is {self.name} and I am a student at {self.school}"

    def enable(self):
        self.__is_enabled = True
    
    def disable(self):
        self.__is_enabled = False
    
    def __str__(self):
        return super().__str__() + f" and I am a student at {self.school} {self.__is_enabled}"

