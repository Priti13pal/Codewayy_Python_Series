# Printing numbers from 1 to 10 except 3 and 7 using (for and while loop)


# Using for loop :

for x in range (11):
    if (x == 3 or x ==7):
        continue
    print(x,end=' ')
print("\n")    


# Using While loop :

x = 0
while(x!= 11):
    if(x == 3 or x == 7):
        x = x+1
    else:
        print(x)
        x = x+1
