import random
random.randint(6,272)

#There two type of objects in Python
#1. Scaler objects 
#2. Non Scaler Object

#Scaler objects 
#int - integers
#float - real numbers
#bool - boolean True or False
#No Type - Special One value None

#you can use type() to identify the type of an object
type(5)
type(3.5)

#convert types
float(3)
int(3)

3+2
print(3+2)

pi = 3.14159
radius = 2.2
area = pi*(radius**2)
print(area)
radius = radius + 1

#STRINGS
#Strings are sequences of characters
hi = 'hello there'
#concatenate means put together
name = 'ana'
greet = hi + name
print(greet)
greeting = hi + " " + name
print(greeting)
silly = hi + (" " + name) * 3
print(silly)

x = 1
print(x)
x_str = str(x)
print ('my fav num is ' , x, ".", "x =", x)
print("my fav num is ", "+ x_str" + "."+ "x = " + x_str)

text = input('Type anything :')
print (5*text)
num = int(input('Type anything :'))
print(5*num)




