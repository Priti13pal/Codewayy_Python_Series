def check_marks(mark):
    if mark >= 90:
        return print(True)
    elif mark < 90:
        raise Exception("Raise  Error marks less ")
    

for i in range(0,1):
    marksObt = int(input("Enter marks :"))
    check_marks(marksObt)
          
