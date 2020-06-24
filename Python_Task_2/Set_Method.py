# Set method in python :

Set_1 = {"software Engeneering", "DAA", "Biomedical", "CRM" }

Set_2 = {"Computer Network", "Language Processor", }

# Adds an element to the set
Set_1.add("Computer Network")
print(Set_1)

# Remove the specified item
Set_1.discard("Biomedical")
print(Set_1)

# Returns a set, that is the intersection of two other sets
print(Set_1.intersection(Set_2))

# Returns whether another set contains this set or not
print(Set_1.issubset(Set_2))

# Return a set containing the union of sets
print(Set_1.union(Set_2))

# Returns whether two sets have a intersection or not
print(Set_1.isdisjoint(Set_2))

# Returns a set with the symmetric differences of two sets
print(Set_1.symmetric_difference(Set_2))



