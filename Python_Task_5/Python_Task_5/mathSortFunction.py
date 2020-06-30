# Math Function :


import math 

num1 = -10

num2= 5

  
# returning the absolute value. 

print ("The absolute value of -10 is : ", end="") 

print (math.fabs(num1)) 

  
# returning the factorial of 5 

print ("The factorial of 5 is : ", end="") 

print (math.factorial(num2))


# returning the ceil of -10


print ("The ceil of -10  is : ", end="") 

print (math.ceil(num1))


# Sort set :

subjects = {'science', 'History', 'English', 'Reading'}

subjects_sorted = sorted(subjects, reverse = True)

print(subjects_sorted)


# Sort List :

numbers = [2, 8, 3, 1, 9]

numbers_ascending = sorted(numbers)
print(numbers_ascending)


numbers_descending = sorted(numbers, reverse=True)
print(numbers_descending)


# Sort Tuple :

subjects = {'science', 'History', 'English', 'Reading'}

subjects_sorted = sorted(subjects, reverse = True)

print(tuple(subjects_sorted))


