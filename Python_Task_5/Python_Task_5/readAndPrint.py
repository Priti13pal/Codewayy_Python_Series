 # Program for reading a text file and print its content :

textFile =  open(r"c:\Users\hp\Desktop\CovidForReadPrint.txt",'r')
for i in textFile:
     print(i , end = " ")
textFile.close()
