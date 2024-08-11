# loop 

# for loop  , while loop 

# Program 1 
'''
x = 1 
while(x <= 10):
    print(x)
    x = x + 1
    
'''

# Program 2 
'''
a = 4
while(a < 10):
    print(a)
    a = a + 1
'''
# Program 3

a = 5
while(a < 10):
    print(a) # 5 7 9 
    a = a + 2
    
    

# Program 4 
 
y = 10
while(y >= 1):
    print(y) # 10 9 8 7 6 5 4 3 2 1
    y  = y - 1 # 9 8 7 6 5 4 3 2 1

print('-----------------------------------------')    
# Program 5 
#  break and continue statement 

# Program 5 

s = 1 
while(s <= 5) : 
    print(s) # 1 2 
    if(s == 2):
        break
    s = s + 1


# Program 6 

ee = 10
while(ee >=1):
    if(ee ==6):
        break
    print(ee) # 10 9 8 7 
    ee = ee - 1 # 9 8 7 6


# ------- contineu statement 

# Program 7

'''
uu = 1 
while(uu <= 5):
    print(uu)
    if(uu == 4):
        continue
    uu = uu + 1  # infinite loop
    
'''
'''
uu = 1 
while(uu <= 5):
    if(uu == 4):
        continue
    print(uu) # 1 2 3
    uu = uu + 1  # 2 3 4

'''

# Program 8

w = 1 
while(w <= 5):
    if(w == 3):
        w = w + 1
        continue
    print(w) # 1 2 4 5
    w = w + 1 # 2 3


j = 1
while(j <=5):
    if(j == 3):
        j = j + 1 #4
        continue
    print(j)  # 1 #2 # 4 #5
    j = j + 1  # 2 #3 # 5 # 5

print('----------------------------')

# Program 9 

kk = 5 
while(kk >=1):
    if(kk ==3):
        kk = kk - 1
        continue
    print(kk)
    kk = kk - 1

# for loop --------------------------------------------------------------------

# Program 1

Alpha = ['a','b','c','d','e','f']
for item in Alpha :   # for loop
    print(item)

for x in range(len(Alpha)):    # range function 
    print(Alpha[x])    

print('----------------------------------------')
# Program 2 

for aa1 in range(9):
    if(aa1 == 6) :
        break
    print(aa1)

#Proram 3

for bb in range(9):
    if(bb == 6) :
        continue
    print(bb)

# Program 4 

for cc in range(10):
    pass

