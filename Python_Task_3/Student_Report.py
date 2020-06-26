# Function for finding Full Name :

def fullName():
    myName=input("Enter name : ")
    print("My full name is",myName)


# Function for finding total marks 
def totalMarks():
    sub1 = int(input("Marks of first subject : "))
    sub2 = int(input("Marks of second subject : "))
    sub3 = int(input("Marks of third subject : "))
    sub4 = int(input("Marks of fourth subject : "))
    sub5 = int(input("Marks of fifth subject : "))
    global totalMarks
    totalMarks = sub1 + sub2 + sub3 + sub4 + sub5
    print( "Total marks obtained are ",totalMarks)


#Function for finding Percentage :
def calculatePercentage(totalMarks):
    global calculatePercentage
    calculatePercentage = (totalMarks/5)
    print("Percentage obtained : ",calculatePercentage)



# Function for findig grade :
def calculateGrade(calculatePercentage):
    if(calculatePercentage >= 95):
        print("Grade  A")
    elif(calculatePercentage >= 85 and calculatePercentage <= 95):
         print("Grade B")
    elif(calculatePercentage >= 75 and calculatePercentage <= 85):
         print("Grade C")
    elif(calculatePercentage >= 65 and calculatePercentage <= 75):
         print("Grade D")
    else:
          print("Failed")


# Function for calling other function:

def detailOfStudent():
    fullName()
    totalMarks()
    calculatePercentage(totalMarks)
    calculateGrade(calculatePercentage)
detailOfStudent()    
    
    

     
         



    
