# Program for display full name, college name, address, total marks and percentage.

# Declaration of variables
First_Name = "Priti "
Middle_Name = "Motilal "
Last_Name = "Pal "
College_Name = "Yeshwantrao Chavan College of Engineering "
Address = "Nagpur "

#Full name using Concatenation :

Full_Name = First_Name + Middle_Name + Last_Name
print(Full_Name)

#college name and address :

College_Name_and_Address = (College_Name + Address)
print("\n Computer Technology from ",College_Name_and_Address)


# Marks Declaration:

Marks_Software_Engineering = 89
Marks_DAA = 90
Marks_Salesforce = 88
Marks_Biomedical = 91
Marks_Language_Processor = 87

print("\nMarks of five best subject: ")
print("\n")
print("Software_Engineering", Marks_Software_Engineering)
print("DAA", Marks_DAA)
print("Salesforce", Marks_Salesforce)
print("Biomedical", Marks_Biomedical)
print("Language_Processor", Marks_Language_Processor)

Total_marks = Marks_Software_Engineering + Marks_DAA + Marks_Salesforce + Marks_Biomedical + Marks_Language_Processor
print("\nTotal_marks : ",Total_marks)


#Percentage :

Total = 500
Percentage = (Total_marks / Total) * 100
print("Percentage = ",Percentage)






