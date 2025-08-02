"""
Polymorphism: Ability to take more than one form 
poly---> Many 
morphism-->forms or fuctionalities or logics 
ex: deposit---> cash or DD or cheque 

Def: The concept of defining multple functionalities or logics to perfom 
     an operation is known as polymorphism 

Types: 
    1. Static polymorphism or comiple-time polymorphism: 
        ex: Method overloading 
            But method overloading is not support by python 
    
    2. Dynamic Polymorphism or Run-time polymorphism
        ex: Method overriding 

Method overloading: 
-------------------
Defining 2 or more methods with same name but with different no of arguments 
or types of arguments.

ex: def add(a,b,c):
    ......
    ......
    ......

    def add(x,y):
    ......
    ......

    def add(p):
    .....
    .....

"""

# Method overriding: The concept of defining a method with same name and 
# same no of parameters in both super class and sub class is known as method overriding 
# here alwyas derived class method overides the base class method 

class x: 
    def m1(self):
        print("from base class")

class y(x):
    def m1(self):
        print("from derived class")

y1=y()
y1.m1() #here subclass method is called or executed bcoz superclass method is 
        #overriden, to execute suepr class method also, crate super object 

x1=x()
x1.m1()

#Note: Method overriding is seen only in inheritance 
