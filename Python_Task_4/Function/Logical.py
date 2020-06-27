def andOperator(a=1):
    
    if a >=1 and a<=10:
        print("Number from 1 to 10")
    else:
        print("Number is out of range")


def orOperator(a=1):
    if a >=2 or a<=10:
        print("Number from 1 to 10")
    else:
        print("Number is out of range")


def notOperator(a=1):
    print("Not Present in range")
    print(not(a >= 25 and a<=30))



