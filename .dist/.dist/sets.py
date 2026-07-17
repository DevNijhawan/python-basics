#() this is for tuples
#[] this is for list
#{} this is for sets

# sets are non-sequential and unordered collection of data items

s1 = {22 ,"sets" , 22.5}
print(s1)
print(type(s1))

# we cannot do indexing in sets because they are unordered

#print(s1[0])  # this will give error because sets are unordered and we cannot do indexing in sets

s2 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(s2) # this will print {1, 2, 3, 4, 5} because sets do not allow duplicate elements

# but in list we can have duplicate elements 
l1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(l1) # this will print [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] because list allows duplicate elements

# basic operations on sets

# membership operator in , not in
no = {1, 2, 3, 4, 5}
print(1 in no) # this will print True because 1 is present in the set
print(6 in no) # this will print False because 6 is not present in the set
print(6 not in no) # this will print True because 6 is not present in the set
print(1 not in no) # this will print False because 1 is present in the set

# concatenation and repetition of sets is not possible because sets are unordered and do not support indexing
# sets are mutable but they do not support indexing and slicing because they are unordered
# sets are mutable here means we can add and remove elements from a set but we cannot change the existing elements in a set because they are unordered and do not support indexing

no.remove(5) # this will remove 5 from the set
print(no) # this will print {1, 2, 3, 4}
no.add(6) # this will add 6 to the set
print(no) # this will print {1, 2, 3, 4, 6}

# There is another fucntion called discard() which is used to remove an element from a set but it does not give error if the element is not present in the set
no.discard(7) # this will not give error because 7 is not present in the set
print(no) # this will print {1, 2, 3, 4, 6} 

# operations on sets

# 1. Intersection of sets is used to find the common elements between two sets.
# syntax: set1.intersection(set2) or set1 & set2

student1 ={"dev", "kunal", "sahil", "rohit"} 
student2 ={"dev", "kunal", "sahil", "yash"} 
common_names = (student1.intersection(student2)) 
print(common_names) # this will print {'dev', 'kunal', 'sahil'} because these are the common elements between the two sets
# &(ampersand) operator can also be used to find the intersection of two sets
common_names = (student1 & student2)
print(common_names) # this will print {'dev', 'kunal', 'sahil'}

# 2. Union of sets is used to find all the elements from both sets.
# syntax: set1.union(set2) or set1 | set2 (|) this called pipe operator
all_names = (student1.union(student2))
print(all_names) # this will print {'dev', 'kunal', 'sahil', 'rohit', 'yash'} because these are all the elements from both sets
# |(pipe) operator can also be used to find the union of two sets
all_names = (student1 | student2)
print(all_names) # this will print {'dev', 'kunal', 'sahil', 'rohit', 'yash'}

# if we have to find between three sets then we can use intersection and union of sets like
student3 = {"dev", "kunal", "sahil", "aman","vishal"}
common_names1 = ( student1 & student2 & student3)
all_names1 = ( student1 | student2 | student3)
print(common_names1) # this will print {'dev', 'kunal', 'sahil'} because these are the common elements between the three sets
print(all_names1) # this will print {'dev', 'kunal', 'sahil', 'rohit', 'yash', 'aman', 'vishal'} because these are all the elements from the three sets

# 3. Difference of sets is used to find the elements which are present in one set but not in the other set.
# syntax: set1.difference(set2) or set1 - set2 (-) this is called minus operator
diff_names = (student1.difference(student2))
print(diff_names) # this will print {'rohit'} because this is the element which is present in student1 but not in student2
# -(minus) operator can also be used to find the difference of two sets
diff_names = (student1 - student2)
print(diff_names) # this will print {'rohit'} because this is the element which is


# sets are mutable
# fronzen set are imutable
# frozen set is used to add a unique element to that cannot be changed
# syntax: frozenset({we can add elements in curly brackets})

f1 = frozenset({1, 2, 3, 4, 5})
f2 = frozenset({1,2,6,7,5})
               
print(f1, type(f1))
print(f2, type(f2))

print(f1 & f2) # this will print {1, 5} because these are the common elements between the two frozen sets
print(f1 | f2) # this will print {1, 2, 3, 4, 5, 6, 7} because these are all the elements from both frozen sets
print(f1 - f2) # this will print {2, 3, 4} because these are the elements which are present in f1 but not in f2





# Thats solve for sets
