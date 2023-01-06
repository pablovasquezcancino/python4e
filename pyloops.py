# Loops (repeated steps) have iteration variables that change each time through a loop.
# Often these iteration variables go through a sequence of numbers.

n = 5 

while n > 0:
    print(n)
    n = n - 1

print('Blastoff')
print(n)

#Definite Loops 
#Quite often we have a list of items of the lines in a file - 
# effectively a finite set of things
# We can write a loop to run the loop once for each of the items in a set
# using the python for construct
# These loops are called "definite loops" because they execute an exact number of times
# We say that "definite loops iterate through the members of a set"

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')

friends = ['federer', 'nadal', 'alcaraz']
for i in friends:
    print('Happy new year: ', i)
print('done!')

# MAKING "SMART" LOOPS:
# The trick is 'knowing' something about the whole loop when 
# you are stuck writing code that only sees one entry at a time

#Finding the largest value:
# We make a variable that contains the largest value we have seen so far.
# If the current number we are looking at is larger, it is the new largest value we have seen so far


largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# Counting in a Loop:
#To count how many times we execute a loop, we introduces a counter variable
# that starts at 0 and we add one to it each time through the loop

counter = 0
print('before', counter)
for i in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1 
    print(counter, i)
print('after', counter)


# Summing in a loop
#To add up a value we encounter in a loop, we introduce a sum variable tthat
# starts at 0 and we add the value to the sum each time trough the loop

total = 0
print('before', total)
for i in [9, 41, 12, 3, 74, 15]:
    total = total + i
    print(total, i)
print('after', total)



#Finding the average in a loop
# An average jsut combines the counting and sum patterns and divides when the loops is done


count = 0
sum = 0
for i in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + i 
    print(sum, count, i)
print (count, sum, sum/count)


#Filtering in a loop
# We use an if statement in the loop to catch / filter the values we are looking for.
print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 13:
        print('large number ', value)
print('after')


#Search using a boolean variable
#If we just want to search and know if a value was found,
# we use a variable that starts at False and is set to True
#as soon as we find what we are looking for.
found = False
print('before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('after', value)


#How to find the smallest value
numbers = [9, 41, 12, 3, 74, 15]
smallest_so_far = numbers[0] #como en un caso real no sabria cual unmero es el primero, simplemnte comparo todos los numeros con el indice 0
for i in numbers:
    if i < smallest_so_far:
        smallest_so_far = i
    print(smallest_so_far, i)
print(smallest_so_far)


#Looping Through Strings
#Using a while statement and an iteration variable,
# and the len function, we can construct a loop to look at each
# of the letters in a string individually:
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


#Looping Through Strings
# A definite loop using a for statement is much more elegant
# the iteration variable is completely taken care of by the for loop.
fruit2 = 'banana'
for letter in fruit2:
    print(letter)


print('*****************')
#Looping and Counting
# This is a simple loop that loops through each letter in a 
# string and counts the number of times the loop encounters 
# the 'a' character
word = 'banana'
count2 = 0
for letter in word:
    if letter == 'a':
        count2 = count2 +1
print(count2)
