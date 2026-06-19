# write and apped to text file

# open file for writing
with open('myfile.txt', 'w') as file:
    file.write('Hello, World!\n') #\n is used to add a new line after the text
    file.write('This is a text file.\n')    

with open('myfile.txt', 'a') as file: # open file for appending
    file.write('This line is appended to the file.\n')  

with open('myfile.txt', 'r+') as file: # open file for reading and writing
    content = file.read() # read the content of the file
    print(content) # print the content of the file
    file.write('This line is added after reading the file.\n') # write to the file after reading it