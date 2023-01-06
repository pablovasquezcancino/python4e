#Opening a File:

# Before we can read the contents of a file, we must tell python
# wich file we are going to ork with and what we will be doing with the file
# This is done with the open() function
# open() returns a 'file handle' - a variable used to perform operations on the file
# similar to "File => Open" in a word processor

#Using Open()
# handle = open(filename, mode): => returns a handle use to manipulate the file
# fhand = open('mbox.txt', 'r')


fhand = open('fragmento de canto del macho anciano.txt', 'r')
print(fhand)

# File Handle as a Sequence
# A file handle open for read can be trated as a sequence of strings where each line inthe file is a string in the sequence
# We can use the for statement to iterate through a sequence
# Remember - a sequence is an ordered set
xfile = open('fragmento de canto del macho anciano.txt')
for word in xfile:
    print(word) #esto muestra el archivo en la terminal
    
#Counting Lines in a file:
counting_lines = open('fragmento de canto del macho anciano.txt')
count = 0
for line in counting_lines:
    count = count + 1
print('line count:', count)

#Reading the Whole file
# We can read the whole file (newlines and all) into a single string:
rea_file = open('fragmento de canto del macho anciano.txt')
inp = rea_file.read()
print(len(inp)) # imprimir cuantos caracteres tiene
print(inp[20:90]) # mimprimir desde el caracter 20 hasta el 89


print('**************************')
#Searching Through a File
# We can put an if statement in our loop to only print lines that meet some criteria
fhand2 = open('fragmento de canto del macho anciano.txt')
for line in fhand2:
    line = line.rstrip() # => esto permite eliminar el espacio en blanco, para que no se generen lineas en blnaco cada vez que se imprime una linea
    if line.startswith('a'):
        print(line)
        

print('**************************')
#Using in to select lines:
fhand2 = open('fragmento de canto del macho anciano.txt')
for line in fhand2:
    line = line.rstrip()
    if not 'terriblemente' in line:
        continue
    print(line)