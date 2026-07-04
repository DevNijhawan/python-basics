
s = "Hello World" #slicing in string

print(s[2:9:2])

name = "Dev"
lan = "Python"
time = "3 hours"

print(f"my name is {name}. I studied {lan} {time} a day") #fstring

#Escape sequences
#\n - create a new line
#\t - create more space
#\\ - create slash in the word
#\' - create word's

print("hello everyone. \n how are you")
print("hello everyone. \t how are you")
print("hello everyone. \\ how are you")
print("hello everyone. \' how are you")


#In string, star(*) operation is repetition operator

s1 = 'Dev Nijhawan'

print("D" in s1)
print("z" in s1)                     # Membership operator
print("D" not in s1)
print("z" not in s1)

# removing unwanted spaces from string there is operator called strip= s1.strip()

s2 = "I am learning java"
print(s2)                               #replace function to replace words= s2.replace()
print(s2.replace("java","python"))

# Next operator is count = to count string in a sentence = s1.count()

'''
print(s1.lower("sentences are in the lower"))
print(s1.upper("sentences are in the upper"))
print(s1.title("first letter of the words in the sentences are upper")""
print(s1.capitalize(only the first letter of the first word of the sentence are upper))
'''

# startwith()
# endswith()
# startwith()
# startwith()

