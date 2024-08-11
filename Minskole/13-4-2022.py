# TODAY'S CODE !!!


# ==============================================


# USE OF LOGICAL OPERATOR
# write a program to take input from user and check if he has passed the exam
num1 = int(input("Please Enter your marks ")) #converting string to int
print(num1 > 34 and num1 < 101 ) # Logical operator
print(type(num1 > 34 and num1 < 101 )) #check the data type of inside print function 


# write a program to take input from user and check if it is prime 

num1 = int(input("Please Enter the no : ")) #converting string to int
r = num1 % 2 #checking the divisibility by 2
s = num1 % 3 #checking the divisibility by 3
t = num1 % 5 #checking the divisibility by 5
u = num1 % 7 #checking the divisibility by 7


print(r , ": checking the divisibility by 2")
print(s , ": checking the divisibility by 3")
print(t , ": checking the divisibility by 5")
print(u , ": checking the divisibility by 7")

print(r==0 or s==0 or t==0 or u==0)