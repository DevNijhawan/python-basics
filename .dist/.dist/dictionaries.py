# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# it encloses the data in curly braces {} and the key:value pairs are separated by a colon : and each key:value pair is separated by a comma ,.

food = {'fruit': '100', 'vegetable': '50', 'water': '20'}
print(food) # this will print {'fruit': '100', 'vegetable': '50', 'water': '20'}
print(type(food)) # this will print <class 'dict'>

# we can use len() function in dict

print(len(food)) # this will print 3 because there are 3 key:value pairs in the dictionary

# to fetch the value in dict we have to give the key name to find it 

print(food['vegetable']) # this will print 50 because the value of the key 'vegetable' is 50

# if we want change the vale of key we can do it by giving the key name and assigning the new value to it

food['vegetable'] = '55' # this will change the value of the key 'vegetable' to 55
print(food)

# and we can add a new key to the dict by this method 

food['snacks'] = '90' # this will add a new key 'snacks' with value '90' to the dict
print(food) # this will print {'fruit': '100', 'vegetable': '55', 'water': '20', 'snacks': '90'}

# get() method is used to fetch the value of a key in dict. 
# if the key is not present in the dict it will return None.
# on the other we want to fetch a key in simple way when there is no key peresent 
# they give error but ub get() they give no error and give NONE as output

# We can use membership operator in and in not , not in
# but in dict we can use in key to check true or false not in value it give error

# next operations on dict
# update() method is used to update the value of a key in dict.

sem1 ={"maths": 96, "chemistry":90, "physics":85}
sem2 ={"maths": 100, "DSA":80, "python":75}

sem1.update(sem2) # this will update the value of the key 'maths' to 100 and add the new keys 'DSA' and 'python' to the dict
print(sem1) # this will print {'maths': 100, 'chemistry': 90, 'physics': 85, 'DSA': 80, 'python':75}

# and we add  a new key to the dict by this method also 

# to delete a key there is a function called pop()
 
sem1.pop("python")
print(sem1) 

# keys cannot be duplicated in dict because they are unique

# not allowed keys - list, set , dict
# allowed keys - int, float, string, tuple,bool
# keys of dict can only be of immutable types

s1 ={ 'id': 121, 'name': 'dev', 'marks':[55,33,[32,66,1]]} # this is allowed because list is mutable but it is a value not a key
print(s1['marks'][-1][-1]) 

# this way can we do indexing for key values in dict

# we fetch keys by using key() method 
print(s1.keys(),type(s1.keys())) 

# we can fetch values also by using values()

print(s1.values(), type(s1.values()))

# we can fetch both the key and value by usning items()
# each items are in tuples

print(s1.items(), type(s1.items()))


# in  dict we have function called copy
# syntax - copy.copy() this is shallow copy 
# shallow copy means we copy the dict but the address are different 
# in dict we have function called deepcopy
# syntax - copy.deepcopy() this is deep copy
# in deep copy also dict address are different
# difference b\w is shallow copy not changing address in innerlist but deep copy does 

import copy

s2 = copy.deepcopy(s1)
print(s2)

(s2["marks"][1]) = "1,0,1"
print(s2)
print(s1)
