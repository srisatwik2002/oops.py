
'''
classes & object in python


1.)class:-  is a blueprint for creating objects,it can be defined by using class *name*:
eg: car model should have 4 wheels,4 windows,one steering   etc is a blueprint
model for a car

class student:
    pass


2.)object:- is a real world entity ,it uses the blue print of a class and use it for
individual changes

eg:-
class student:
    def __init__(self,name):
        self.name=name
s1=student("qwerty")
print(s1.name)




3.)constructor:- __init__ is a constructor which is present in the classes and
is used for when the obects are initialised to the class , it is represented by
__init__ and attributes(name,age,x) are passed to the class through it.
eg:
class student:
    def __init__(self,name):
        self.name=name
where __init__ is used to initialise the values passed by objects to the class



4.)self patrameter:- the self parameter is used with __init__ constructor and is
used to represent the current instance of a class and is used to access variables
or initialise values to theclass
eg:
class student:
    def __init__(self,name):
        self.name=name
s1=student("qwerty")
print(s1.name)

(or)

anything can be used as a variable name instead of self but self is used
for readability purposes

class student:
    def __init__(abcd,name):
        abcd.x=name
s1=student("qwerty")
print(s1.x)



5.) Attributes:- class attributes and object attributes
class attributes remain same throuhout the class
object attributes changes with respective to the particular object

prefernce of object attributes>class attributes

6.)methods:- methods are functions present inside the class that belong to or
used by the objects

7.)@staticmethod:- do not return anything or it doesnot modify the code

8.) abstraction:- hiding the implementation details of a class
by showing only the essential features to the user

9.)encapsulation:- wrapping data and functions into a single unit (object)
everything in oops is encapsulation

10.)public_private_protected

11.)inheritance:- when one class inherits the properties of one parent class
into a child or derived class is called inheritance

12.) classmethod:- bound to the class and recieves the case
as an implicit first argument

13.)staticmeth  od,classmethod-cls,instancemethods-self

14.polymorphism:-
operator overloading = is allowed to have different
meanings to the types or context.
operator overriding=overiding the same name methods with according the object

'''