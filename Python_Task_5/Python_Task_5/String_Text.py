# Program which should take string of 3-4 lines and writeit to a txt file:

text = 'Python is a general purpose and high level programming language\n Python use for developing desktop GUI applications etc\n Python readability makes it a great first programming language!!'

saveFile = open('exampleForString.txt','w')
saveFile.write(text)
saveFile.close()
