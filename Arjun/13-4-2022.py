# using logical operator 

#  Program 1 ---->  write a program to take input from user and check if has pass the exam 

num1 = int(input("Please Enter you marks : "))   #converting string into int

print(num1 > 40 and num1 < 101)   #Logical operator

print(type(num1 > 40 and num1 < 101)) #check the data type inside print function 



# Program 2 -----------

num2 = int(input("Please Enter you marks : "))   #converting string into int

print(num2 > 34 and num2 < 101)   #Logical operator

print(type(num2 > 34 and num2 < 101)) #check the data type inside print function 



# Program 3 ---> write a program to take input from user and check if it is prime

#Prime Number - The Number is  divisible by 1 or Number itself

number = int(input("Plase Enter the Number : "))  #converting string into integer

r = number % 2            #checking the divisibility by 2 
s = number % 3            #checking the divisibility by 3 
t = number % 5            #checking the divisibility by 5 
u = number % 7            #checking the divisibility by 7

print('checking the divisibility by 2 : ',r)
print('checking the divisibility by 3 : ',s)
print('checking the divisibility by 5 : ',t)
print('checking the divisibility by 7 : ',u)

print(r==0 or s==0 or t==0 or u==0)