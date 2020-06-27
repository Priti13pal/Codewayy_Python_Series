def square(num):
    return num * num

number = float(input(" Please Enter any Value : "))

sqre = square(number)

print("The Square of a Given Number {0}  = {1}".format(number, sqre))



def myMax(list1):
    maximum = list1[0] 

    for x in list1: 

        if x > maximum : 

             maximum = x 

    return maximum

list1 = [10, 20, 4, 45, 99] 

print("Largest element is:", myMax(list1))



def myMin(list1):
    minimum = list1[0] 

    for x in list1: 

        if x < minimum : 

             minimum = x 

    return minimum

list1 = [10, 20, 4, 45, 99]

print("smallest element is:", myMin(list1))


def totalNum(list1)
total = 0

list1 = [10, 20, 4, 45, 99]

for element in range (0,len(list1)):
    total = total + list1[element]

print("Sum of elements present in list: ",total)    



    


