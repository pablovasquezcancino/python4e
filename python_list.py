# List Constants
# List constants are surrounded by square brackets and the elements in the list are separated by commas
# A list element can be any python object - even another list
# A list can be empty

friends = ["federer", "nadal", "alcaraz"]

#List and definite loops - best pals
for friend in friends:
    print('Happy new year', friend)
print('done!')
print(friends[1]) # => nadal.
friends[1] = "djokovic"
print('ha la lista de friends le hemos agregado un valor, hemos reemplazado a nadal por djokovic', friends)


# Using Range Function:
# The range function returns a list of numbers that range from zero to one less than the parameter
# we can construct an index loop for an integer iterator


#CONCATENATING LIST USING + 
tenistas = ["federer", "nadal", "alcaraz"]
futbolistas = ["maradios", "roman", "caniggia"]
deportistas = tenistas + futbolistas
print("dos listas unidas:", deportistas)

#List can be sliced using:
print(deportistas[1:4]) # => ['nadal', 'alcaraz', 'maradios']

#List methods:
#append
#count
#extend
#index
#insert
#pop
#remove
#reverse
#sort

#Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print(stuff)
print(99 in stuff) # => true


#Best Friends: Strings and lists:
#Split() breaks a string into parts and produces a list of strings. We think
# of this as words. We can access a particular word or loop through all the words
relato = 'ahi va maradona el genio del futbol mundial'
h = relato.split()
print(h) # => ['ahi', 'va', 'maradona', 'el', 'genio', 'del', 'futbol', 'mundial']   
for w in h:
    print(w) # => imprime cada plabra por separado jeje

