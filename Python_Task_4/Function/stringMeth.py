# Function to find middle charater of string


def middleChar():
  middleChar = input('Enter String: ')
  if len(middleChar) % 2 == 0:
 
    print(middleChar[len(middleChar) // 2 - 1] + middleChar[len(middleChar) // 2])
  else: 

    print(middleChar[len(middleChar) // 2])

def countVowel():
    
    string=input("Enter string:")
    vowels=0
    for i in string:

       
       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    print("Number of vowels are:\n")
    print(vowels)


def calculateLen(string): 
    counter = 0

    for i in string: 
        counter += 1 
        return counter
string = "Python"
#print("Length of the string :",counter)
print(calculateLen(string))



def calculateWord(string):
    string=input("Enter string:")
    char=0
    word=1
    for i in string:
        char=char+1
        if(i==' '):
            word=word+1
    print("Number of words in the string:")
    print(word)
