#TODAYS CODE 

# ======================================

months1 = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
months_31 = {"Jan", "Mar", "May","Jul", "Aug", "Oct", "Dec"}
months_30 = {"Apr", "Jun", "Sep", "Nov"}
months_28 = {"Feb"} #only one element
print(len(months1))
# TO GET THE COMMON ELEMENTS IN THE SET 

print(months1.intersection(months_28)) # BETWEEN TWO SETS
print(months_30.intersection(months_28,months1)) # BETWEEN THREE SETS
i =  months_31.intersection(months_28,months_30) # THE INTERSECTION RESULT CAN BE STORED IN A VARIABLE
print(i)
print(type(i))

# TO GET THE UN-COMMON ELEMENTS IN THE SET 
print(months_30.symmetric_difference(months_28))
print(months1.symmetric_difference(months_31))









# HW PRINT BELOW STRING IN REVERSE ORDER USING NEGATIVE SLICING
name1 = "eloksnim"

# SHARE THE ANS/ERROR  SCREENSHOT