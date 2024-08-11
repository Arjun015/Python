#TODAYS CODE 

#=================================================

# CREATING SAMPLE LIST 


luckyno_1 = [0,1,2,3,4,5,6,7,8,9]
print(luckyno_1)
print(len(luckyno_1))

print("*******")
# ACCESSING THE INDIVIDUAL ITEMS IN THE LIST
print(luckyno_1[7])
print(luckyno_1[9])

print("*******")
print(luckyno_1[2:5])

print("*******")
luckyno_2 = ["SUPERMAN1","SUPERMAN2","SUPERMAN3" ]
print(len(luckyno_2))
print(luckyno_2[0:2])


luckyno_1[7:9] = [17,18,19,21]
print(luckyno_1)


# APPEND AT THE END OF THE LIST
print("***APPEND****")
luckyno_2.append("SUPERMAN4")
print(luckyno_2)

# INSERT AT THE GIVEN INDEX POSITION AND THE CURRENT ITEM WILL SHIFT ONE POSITION TO RIGHT
print("***INSERT****")
luckyno_2.insert(2,"BATMAN3")
print(luckyno_2)

# EXTEND IS USED TO JOIN TWO LISTS
print("***EXTEND****")
luckyno_2 = ["SUPERMAN1","SUPERMAN2","SUPERMAN3" ]
luckyno_3 = ["BATMAN1","BATMAN2","BATMAN3" ]
luckyno_2.extend(luckyno_3)
print(luckyno_2)
print(luckyno_2 + luckyno_3) #cocatenation 

luckyno_1 = [2,4,6,3,2,5,8,9]
print(luckyno_1)
print(len(luckyno_1))


# METHODS  IN LIST 
# SORTING
luckyno_1.sort()
print(luckyno_1)
# THIS WILL PRINT IN DESCENDING ORDER
luckyno_1.sort(reverse=True)
print(luckyno_1)

# MAKING A COPY
lucky_copy = luckyno_1.copy()
print("*****THIS IS COPY****")
print(lucky_copy)

# REMOVING ACTUAL ITEM FROM THE LIST
lucky_copy.remove(2)
print(lucky_copy)
lucky_copy.remove(2)
print(lucky_copy)

# POP REMOVED LAST ITEM IN THE LIST WHEN NO INDEX IS GIVEN
print("*****POP****")
lucky_copy.pop()
print(lucky_copy)

# POP REMOVED INDEX  ITEM IN THE LIST
lucky_copy.pop(0)
print(lucky_copy)


# CLEAR 
lucky_copy.clear()
print(lucky_copy)
print(len(lucky_copy))



#************HW**************
# SUM OF ITEMS IN LIST CONTAINING  ALL ONE DIGIT PRIME NUMBERS 
# TAKING MARKS SCORED BY TEN STUDENTS AS INPUT TO A LIST AND CHECKING HOW NAMY HAS SCORED 100 HINT:USE COUNT()