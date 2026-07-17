# difference between list and tuple is that list is mutable and tuple is immutable
# tuples are created using parentheses ()
# 

t = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(t)
print(type(t))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l, type(l))
t1 = tuple(l)                    # we can change list into tuple using tuple() function
print(t1, type(t1))              # we can change tuple into list using list() function
print(l, type(l))

# Operations

student1 = ("Dev", 20, "Python")
student2 = ("Nijhawan", 21, "Java") 
                                  # concatenation of tuple is done using + operator
student = student1 + student2
print(student)

# Repetition of tuple is done using * operator

student3 = student1 * 3
print(student3)

# Membership operator 
#it is used to check whether an item is present in the tuple or not
# (in) operator 
# (not in) operator

# count() function is used to count the number of occurences of an item in a tuple
faah = (1, 2, 3, 4, 5, 6, 8, 9, 1, 2, 3, 1, 5, 6, 7, 1, 9)
print(faah.count(1))

#index() function is used to find the index of an item in a tuple
print(faah.index(7))

#min() function is used to find the minimum value in a tuple
#max() function is used to find the maximum value in a tuple
#sum() function is used to find the sum of all the items in a tuple

print(f"the minimum value in the tuple is: {min(faah)}")
print(f"the maximum value in the tuple is: {max(faah)}")
print(f"the sum of all the items in the tuple is: {sum(faah)}")

# list are mutuable
# tuples and strings are immutable

# if we want to change the existing list 
# but we cannot change the existing tuple or string
# thats why we use tuples when we want to store data that should not be changed

l1 = [" pyhton", "java", "c++", "c#",]
# we can modiyfy list by using indexing
l1[-1] = "javascript"
print(l1)

# that solve for tuples