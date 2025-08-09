"""
String: A string is a sequence collection of charecters 
in python, a string represented using 

1. single qoute 
2. double qoute 
3. triple qoute 

1) Each charecter of a string is represented or accessed by a unique index 
    1. Forward index (or) Positive index -----> starts from left to right -----> starts with 0
    2. Backward index (or) Negative inde -----> starts from right to left -----> starts with -1

"""

x='python'
print(x)
print(type(x))
print(id(x))
print(x[2])
print(x[-2])
print(len(x))

y='programming'

print(x+ ' '+y) #concatentaion------> adding 2 strings-----1st string followed by 2nd string 
