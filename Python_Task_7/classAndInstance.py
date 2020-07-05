# Write a program using Python class and objects which should have 5 different functions and should create the 5 different instances of that class and print the details of :


class Report:
    
    def __init__(self, firstname, lastname, college, branch, tMarks):
        self.firstname = firstname
        self.lastname = lastname
        self.college = college
        self.branch = branch
        self.tMarks = tMarks
        

      # To display the full name
      
    def fullName(self):
       return "{} {}".format(self.firstname,self.lastname)


     # To display the college and branch
     
    def college_branch(self):
        return "{} {}".format(self.college,self.branch)


     # Display the total marks
     
    def marksObt(self):
        totalMarks = sum(self.tMarks)
        return totalMarks
        #totalMarks = self.marksObt()

    # Total percentage of marks
    
    def percent(self,totalMarks):
        percentage = totalMarks / len(self.tMarks)
        return percentage
        #percentage = self.percent(totalMarks)

       # calculate the grade
       
    def Grade(self,percentage):
        if percentage >= 95:
            return("Grade : A\n")
        elif(percentage>=80 and percentage<90):
            return("Grade: B\n")
        elif(percentage>=70 and percentage<80):
            return("Grade: C\n")
        elif(percentage>=60 and percentage<70):
            return("Grade: D\n")
        else:
            return("Grade: F\n")

    print("         REPORTCARD !!         \n")   

    def Info(self):
        
        print("Name of student :",self.fullName())

        print("College and Branch :",self.college_branch())
        
        totalMarks = self.marksObt()
        print("Total marks out of 500 is :",totalMarks)
        
        percentage = self.percent(totalMarks)
        print("Percentage :",percentage)
        
        grade = self.Grade(percentage)
        print(grade)


# Display report:
student = Report("Priti","pal","YCCE","Computer Technology",[91,89,78,87,90])
student.Info()

        
        


    
    


    
        
    
