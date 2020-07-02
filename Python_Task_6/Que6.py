def findType(num):
    divisionSum = 0
    for i in range(1,num,1):
        if num % i == 0:
            divisionSum = divisionSum + i
    if divisionSum == num:
        return 0
    elif divisionSum < num:
        return 1
    else:
        return -1

num = int(input("Enter number : "))
for i in range(0,num,1):
    num = int (input("Enter num :"))
    divisionType = findType(num)
    
    if divisionType == 0:
        print("Perfect ")
    
    elif divisionType == -1 :
        print("Deficient")
    
    elif divisionType == 1 :
        print("Abundant")
