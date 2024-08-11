# TODAYS CODE 

# =========================================

# SETS
# HOW TO CREATE A SET

even1 = {2,4,6,10}
odd1 = {1,3,5,9}

print(even1) #the o/p will not be in the same order as we have entered the vale
print(odd1) #the o/p will not be int the  same order as we have entered the vale
print(len(even1))
print(len(odd1))

num1 = (3,) #tuple , if no of elements is one
print(type(num1))


odd1 = {} #this is an empty set = dictionary
print(odd1)
print(type(odd1))

# CHECKING THE PROPERTIES OF SERTS
even1 = {2,4,6,8,2,12,14,16,8} #only unique values are there in sets o/p
print(even1) #the o/p will not be int same order as we have entered the vale
print("Lenght of Even is ")
print(len(even1))


# METHODS
print("*****METHODS******")


even1 = {2 ,4,6,8}
even1.add(10) # TO INSERT SINGLE ELEMENT
print(even1)

odd1 = {1,3,5,7,9}
even1.update(odd1) #TO INSERT COMPLETE SET 
print(even1)


num1 = {1,2,3,4,5,6,7,8,9}
print(num1.remove(4))
print(num1)

print(num1.discard(9))
print(num1)


print(num1.discard(23)) # NO ERROR EVEN IF THE ELEMENT IS ABSENT
print(num1)


# num1 = {1,2,3,4,5,6,7,8,9}
# print(num1.pop(4)) # THIS WILL THROW ERROR
# print(num1)


num1 = {1,2,3,4,5,6,7,8,9}
print(num1.pop()) # ANY RANDOM ITEM WILL BE DELETED
print(num1)
print(num1.pop()) # ANY RANDOM ITEM WILL BE DELETED
print(num1)


num1.clear()
print(num1)




# HW : CHECK THE BEHAVIOUR OF pop() method in set()


# OR THE DOUBT ASKED IN THE END ::


# TRY TO EXECUTE BELOW CODE AND TRY TO NOTICE THE  OUTPUT / ERROR :

even1 = {2,4,6,8} 
print(even1)
even1.print()