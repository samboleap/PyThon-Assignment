class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        #print("Hello, my name is " + self.name,"and I am", self.age, "years old.")

        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

myClassmate = Person("Alice",25)

#Accessing attributes of the object
print(myClassmate.name)
print(myClassmate.age)

#Calling the greeting method on the object
myClassmate.greet()