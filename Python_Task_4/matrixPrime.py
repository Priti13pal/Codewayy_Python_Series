
Row = int(input("Enter the number of rows:")) 

Column = int(input("Enter the number of columns:")) 

matrix = [] 

print("Enter the entries rowwise:") 

for i in range(Row):      

    a =[] 

    for j in range(Column):     

         a.append(int(input())) 

    matrix.append(a) 

for i in range(Row): 

    for j in range(Column): 

        print(matrix[i][j], end = " ") 

    print()


print("Prime numbers are")             
for i in range(Row):
    for j in range(Column):
        if((matrix[i][j] > 1)):
            for value in range(2,matrix[i][j]):
                if(matrix[i][j] % value) == 0:
                    break
            else:
                print(matrix[i][j])
            

            
