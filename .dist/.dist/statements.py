# == , >= ,<= ,< ,> , != Conditianl Operator
'''
==  Equal to   5 == 5
True

!=  Not equal to  5 != 3
True

>  Greater than  8 > 5
True

<  Less than 3 < 7
True

>=  Greater than or equal to 5 >= 5
True

<=  Less than or equal to 4 <= 8
True
'''

# If block statemnt
# Identation
# syntax : 

# if Condition:
#     statement 1
#     statement 2              # if the condition is true then is compries or go inside this box
#     statement 3

# statement m         # if the condition is false then is will go directly top the statement M



age = float(input("wht is the age of kunal  :"))

if age >= 18:
    print("congratulation kunal you became adult you can now vote ")
print("sorry")

# if-else 




age = float(input("wht is the age of kunal  :"))

if age >= 18:
    print("congratulation kunal you became adult you can now vote ")
else: 
    print("Sorry kunal you cant vote ")
print("thanks")

# when we have do division in statemnts there is function called % 

num = int(input( "what is the number :"))
if num  > 0:
    print("the number is positvie")
elif num < 0:
    print("the number is negative")
else  :
    print("the number is zero")


# Now we are if in if block

marks = int(input( "Congrats , What is your total number :"))

if marks >= 50:
    print("Congrats, You passed the exam")
    if marks >= 90:
        print("A+")
    elif marks >= 85 and marks<90:
        print("A")
    elif marks >= 80 and marks<85:
        print("B")
else :
    print("Study hard , Next time")


# Ternary operator
# It mean write if else statement in one line 
# if marks == 0: print("even") else ("odd")



      


