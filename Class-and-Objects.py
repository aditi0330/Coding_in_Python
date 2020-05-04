# Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

# A very basic class would look like this:

class MyClass:
    variable = "aditi"

    def function(self):
        print("This is a message inside the class.")

# We will explain why you have to include that "self" as a parameter a little bit later. First, to assign the above class(template) to an object you would do the following:

class MyClass:
    variable = "aditi"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

# Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".

# Accessing Object Variables
# To access the variable inside of the newly created object "myobjectx" you would do the following:

class MyClass:
    variable = "aditi"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable

# For instance the below would output the string "aditi":

class MyClass:
    variable = "aditi"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)

# You can create multiple different objects that are of the same class(have the same variables and functions defined). However, each object contains independent copies of the variables defined in the class. For instance, if we were to define another object with the "MyClass" class and then change the string in the variable above:

class MyClass:
    variable = "aditi"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "apple"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# Accessing Object Functions
# To access a function inside of an object you use notation similar to accessing a variable:

class MyClass:
    variable = "aditi"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()
    
