#  Function to count number of words in a sentence :
    
def wordCount(string):
    
    tokens = string.split()
    n_tokens = len(tokens)
    return n_tokens

string =input("Enter the string : ")

