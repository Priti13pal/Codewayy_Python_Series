def upperLower(s):
    
    d={"UPPER_CASE":0, "LOWER_CASE":0}

# Using inbuild function for uper and lower case :

    for u in s:
        if u.isupper():
           d["UPPER_CASE"]+=1
        elif u.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

upperLower('I am Studing Python')
