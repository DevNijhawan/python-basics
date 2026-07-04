# list can be created by a square bracket []

# slicing of list

l1 = [ 1, 4, 5, 6, 7, 8, 9,]
print(l1[1:7:3])

# concatenation in list
 
l2 = [1, 2, 3]
l3 = [4, 5, 6]
print(l2+l3)

# Repetiton of lists 

print(l2*3)

# append() function adds an item to the end of the list  
# syntax = list.append(item) 

name = ["dev", "yash", "sahil"]
print(name)
name.append("vikash")
print(name)

# if I want to add item in middle we have a function called insert
#syantax = list.insert(index,item)

print(name)
name.insert(2,"nobody")
print(name)


#If we want to add more than 1 item in a list we have function called extend
#syntax = list.extend(["1", "2"])

food = ["pizza", "burger", "fries"]
print(food)
food.extend(["momos", "garlic bread"])
print(food)


# if i want to remove an item from a list the function called remove
#syntax = list.remove(item)

food.remove("burger")
print(food)

# if want to remove item through indexing the function name called pop
# syntax = list.pop()
  

# if want to remove item through indexing the function name called pop

food.pop(3)
print(food)


# if we want to reverse a list there is a fun called reverse 
#syntax - item.reverse()

nums = [0,9,8,7,6,5,4,3,2,1]
print(nums)
nums.reverse()
print(nums)


# if we want to sort the list we have a fun called sort
# syntax - item.sort()
# list is sort in ascending order
# if we want to sort in decencding order
# syntax - item.list(reverse = True)
# syntax - item.list(reverse = True)

nums = [1,4,7,3,8,9,5,2,]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)


# If we have a big list and we have to count the item in the list we have function called count
# syntax = item.count()

no = [1,2,3,4,5,6,7,9,9,7,6,4,3,2,3,2,4,6,89,0,1,2,6,7,9,34,2,7,9,4,23,56,89,0,6,5,4,33,4,6]
print(f"The list is : {no}")
item_to_count = int(input("Enter the number to be counted : "))
w = no.count(item_to_count)
print(f"The occurence of the {item_to_count} is {w}")


# Membership operator 
# min() is to find the smallest number 
# max() is to find the biggest number
# sum() is to find the total of the number list 

 
no = [1,3,4,66,9999,25378]
print(f" the smalles number in the list: {min(no)}")
print(f" the biggest number in the list: {max(no)}")
print(f" the total of the list: {sum(no)}")


l2 = [[1,0], [2,3], [4,5,[6,7]]]
print(l2[-1][-1][-1])


       
