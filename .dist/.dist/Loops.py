# Each repetation is called Itreation

# Defination of for loops
# A for loop in Python is used to repeat a block of code for each item in a sequence 
# (such as a list, string, tuple, dictionary, or range).


fruits = "banana apple orange grapes"

print()

for f in fruits:
    print(f)
    

# range() function = range() generates a sequence of numbers. It doesn’t store all the numbers at once; 
# instead, it produces them one by one, which makes it memory efficient.
# syntax : range(start, stop ,step):
# for revese range function we use negative indexing in steping


for i in range(3, 33, 3):
    print(i)

# next range function is 
#range(start,stop): this is use for that code that has default step 1 it will not change

for w in range(1,4):
    print(w)
print("Happy Birthday")

#next range(stop)
# in this start has default value 0 and step 1 is also default

for p in range(10):
    print(p)
    


item = ["chips","kurkure","salt","sugar","bread"]

for g in range(len(item)):
    print(g)


profit = [ 14, 55 ,73, 90]

for a in range(len(profit)):
   
    q = a + 1
    print(f"Profit of quater {q} is {profit[a]}")


# Find min and max and total number of integer using loops and tuples

runs = [ 14, 55 ,73, 90, 100, 200, 300, 400, 500]

total = 0
for run in runs:
    total = total + run
print(f"total runs is {total}")


# highest and lowest runs
highest = runs[0]
lowest = runs[0]
for run in runs:
    if run > highest:
        highest = run
    elif run < lowest:
        lowest = run
print(f"highest runs is {highest}")
print(f"lowest runs is {lowest}")

print(max(runs))
print(min(runs))

for num in range(20):
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
        continue

for num in range(50):
    if num % 5 == 0:
        print(f"{num} is divisible by 5")
        break

# continue statement is used to skip the current iteration of a loop and move on to the next iteration.
#break statement is used to exit a loop prematurely, stopping the loop from executing any further iterations.













    