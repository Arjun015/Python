# TODAYS CODE  ======================================

# TUPLES
# HOW TO CREATE A TUPLE
secret_recipe1 = ("step1", "step2", "step3", "step4", "step5","step5")
print(secret_recipe1)
print(type(secret_recipe1))

secret_recipe2 = ("step1", "step2")
print(secret_recipe2)
print(type(secret_recipe2))

# check the characteristics for single element/item and blank/none
secret_recipe3 = ("step1",) # the "," is essential to make it a tuple without it wll show as "string"
print(secret_recipe3)
print(type(secret_recipe3))


# reading individual items/ range of items  from a tuple 
print(secret_recipe1[1]) # single element
print(secret_recipe1[0:3]) # range of elements

# CHECK IF TUPLE IS MUTABLE OR NOT
secret_recipe1[1] = "step9" # this will throw error
print(secret_recipe1.replace("step3")) # this will also throw error



# METHODS IN TUPLE . Except for methods used to chnage elements , most other
# methods of LIST will also work here eg. sum() function 
secret_recipe1 = ("step1", "step2", "step3", "step4", "step5","step5")
print(secret_recipe1)
print(type(secret_recipe1))


print(secret_recipe1.count("step5")) # pass the value of element
print(secret_recipe1.index("step3")) # output will be the index position
