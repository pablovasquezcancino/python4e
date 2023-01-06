# Python functions:
# there are two kinds of functions in python
# Built-in functions that are provided as part of python - print(), input(), type(), float(), int()

#Functions that we define ourselves and then use

#in Python a function is some reusable code that takes arguments(s) as input, does dome computation, and then returns a result or results
# we define a function using the def reserved word

#We call/invoke the function by using the function name, parentheses, and arguments in a expression

# a example of a type function:
i = 42
print(type(i)) # => <class 'int'>
a = 'holi'
print(type(a)) # => <class 'str'>

# functions build for us, example:
def great(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Helloooow')
        

great('es') #this print Hola
great('fr') #this print bonjour, and so on
great('ejemplo') #this print helooo, because is else for default, you know waht i mean? 

# RETURN VALUES
#often a function will take its arguments, do some computation, and 
#return a value to be used as the value of the function call
#in the calling expression. The return keyword is used for this.

def greet():
    return 'hello'

print(greet(), 'pablo') #hello pablo
print(greet(), 'Andréi') #hello Andréi

#A "fruitful" function is one that produces a result (or return a value)
#The return statement ends the function execution and 'sens back' the result os the function


#Multiple Parameter/Arguments
# we can define more than one parameter in the function definition
# we simply add more arguments when we call the function
# we match the number and order of arguments and parameters

def addtwo(a,b):
    added = a + b
    return added 

x = addtwo(3,5)
print(x) # result is 8 jeje

#Void (non-fruitful) functions
# When a function does not return a value, we call it a "void" function


