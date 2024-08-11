
# --------------------- tuple ====>    

# we cannot use method in tuple => append() , extend() ,insert(),remove(),pop(),clear()

#  Program 1

fruitA = ['lemon','Apple','Water-Melon','cashunut','Pitch']
for x in fruitA : 
    print(x)


# Program 2

Games = ['cricket','football','hockey']
for y in Games :
    print(y)      

Games[0] = "baseball"
print(Games)

# Program 3

# tuple does not update the value

alpha = ('A','B','C','D','E','F','G')
print(alpha)
#alpha[3] = 'ZA'
print(alpha)

fruit = ['lemon','Apple','Water-Melon','cashunut','Pitch']
print(fruit)

print('-----------------------------------------')
print(fruit[2]) # can access the index value
print(fruit[3])

print('------------')

for ss in fruit : 
    print(ss)

print('=================//////////////======================')

#---------------- slicing() -----------------------------------
#         0       1        2        3       4
Name = ('Ajay','Anjali','Manisha','Gita','sundara')
#        -5      -4       -3        -2       -1     

print(Name[0:4])
print(Name[0::2])
print(Name[::-1]) #('sundara', 'Gita', 'Manisha', 'Anjali', 'Ajay')
print(Name[-5:-1])

y = ()
print(type(y)) #<class 'tuple'>

# function to process the tuple

# ----------------- len() ------------------------
country = ['India','America','Rassia','Afreca','British']
print(len(country)) # 5


# ---------------- max() ------------------

numA = [11,22,33,44,55,55,55]

print(max(numA)) # 55

#------------------min() -------------

print(min(numA)) # 11

#-----------count() -----------

print(numA.count(55)) # 3

# --------------- index()-------------

print(numA.index(44)) # 3


#----------- sorted()-------------

numAB = (88,33,22,22,33,444,22,33,4,8,67,34,23,43)
aaa = sorted(numAB)
print(aaa)

# -------------- in operators 

print(22 in [88,33,22,22,23]) # True
print(22 not in [88,33]) # True 

number = [11,22,3,44,55,66]
if(55 in number):
    print('Available')

else :
    print('notAvailable')


# -----------------------

Animal = ['lion','Tiger','Zebra','Elephant']

for x in Animal : 
    print(x)

print('-------------(########)----------------')

for x in range(len(Animal)):
    print(Animal[x])    
