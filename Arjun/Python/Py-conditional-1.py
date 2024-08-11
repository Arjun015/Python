# conditional statements 

# single input =====>    multiple statement
#numberOfT > 0 and  numberOfT <= 5  ===> 5%
#numberOfT > 5 and  numberOfT <= 10 ===> 10%
#numberOfT > 10                     ===> 30%

# syntax :

# if (condition):
#     statement-1
# else:
#     statement-2


# ----------------  if() statement ------------------

# Program 1

numberOfTicket = 11 
if(numberOfTicket > 0 and numberOfTicket<= 5):
    print('5% discount Granted')
if(numberOfTicket > 5 and numberOfTicket<= 10):
    print('10% discount Granted')
if(numberOfTicket > 10 and numberOfTicket<= 15):
    print('20% discount Granted')
        
        

# if------elif()------stat.

# Program-2 


numberOfTicket = 10
if(numberOfTicket > 0 and numberOfTicket<= 5):
    print('5% discount Granted')
elif(numberOfTicket > 5 and numberOfTicket<= 10):
    print('10% discount Granted')
elif(numberOfTicket > 10 and numberOfTicket<= 15):
    print('20% discount Granted')
        

# Program 3 

mark = 88 
if(mark > 90):
    print('Grade-A')
if(mark > 75):
    print('Grade B') #Grade B
if(mark > 60):
    print('Grade C') # Grade C   


mark = 88 
if(mark > 90):
    print('Grade-A')
elif(mark > 75):
    print('Grade B') #Grade B
elif(mark > 60):
    print('Grade C')    


# Program 4



