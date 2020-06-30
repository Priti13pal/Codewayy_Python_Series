Num1 = input("Enter tne number one: ")
Num2 = input("Enter the number second: ")
try:
    Num3 = int(Num1) / int(Num2)
    
except ZeroDivisionError as e:
    print('Division by zero exception')
    Num3 = None
    
except TypeError as e:
    print('Type error exception')
    Num3 = None
    
print("Division is: ",Num3)

if  Num3 > 5:
    raise Exception('x should not exceed 5.The value of Num3 was:{}'.format(Num3))
    

