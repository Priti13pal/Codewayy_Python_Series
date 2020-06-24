# Dictionary method in Python :

# Dicitonary creation
Test_Dict1 = {"Bike" : "splendor", "Car" :"Duster","Cycle":"Atlas"}

Test_Dict2 = ("Honda","Hero","pulsar")
value={}
print(value.fromkeys(Test_Dict2,"Bike"))


# Returns a list containing a tuple for each key value pair
print(Test_Dict1.items())

# Returns a list containing the dictionary's keys
print(Test_Dict1.keys())      

 
# Returns a dictionary with the specified keys and value
print(Test_Dict1.get("Car"))

# Copy dictionary
print(Test_Dict1.copy())

# Pop key value pair
print(Test_Dict1.popitem())

# Add update
Test_Dict1.update({"Auto" : "Tata Motors"})
print(Test_Dict1)





