# Python program to remove empty tuples from a  list of tuples :

def Remove(tuples): 

    tuples = [r for r in tuples if r] 

    return tuples 

tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

print("Sample :",tuples)
print("Output :",Remove(tuples))

