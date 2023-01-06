# Slicing Strings
# We can also look at any continuos section of a string using a colon operator.
# The second number is one beyond the end of the slice - "up to but not including"
# If the second number is beyond the end of the string, it stops at the end
s = 'Monty Python'
print(s[0:4]) # => Mont
print(s[6:7]) # => p
# If we leave off the first number or the last number of the slice,
# it is assumed to be the beginning or end of the string respectively
print(s[:2]) # => Mo
print(s[8:]) # => thon



print('*****************')
# STRING LIBRARY
# Python has a number of string functions which are in the string library
# These functions are alredy built into every string - we invoke them by appending the function to the string variable
# These functions do not modify the original string, instead they return a new string that has been altered
#lower()
saludo = 'Hola Bob'
zap = saludo.lower()
print(zap) # => hola bob
# find()
# upper()
# replace()
saludito = 'Hola Bob'
sal = saludito.replace('o', 'x') # => remplazame todas las o por x 
print(sal) # => Hxla Bxb


#Stripping Whitespace
""" Sometimes we want to take a string and remove whitespace at the beginning
and/or end.
istrip() and rstrip() remove whitespace at the left or right
strip() removes both beginning and ending whitespace"""

#Prefixes:
line = 'please have a nice day'
line.startswith('please') # => True
