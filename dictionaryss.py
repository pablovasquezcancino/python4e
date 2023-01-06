# key.
# Dictionaries
# Lists indes their entries based on the position in the list
# Dictionaries are like bags - no order
# So we index the things we put in the dictionary with a "lookup tag" or a KEY.

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse) # => {'money': 12, 'candy': 3, 'tissues': 75}
print(purse['candy']) # => 3
purse['candy'] = purse['candy'] + 2
print(purse) # => {'money': 12, 'candy': 5, 'tissues': 75} now candy is 5

