#Reading files: Tell, Seek, and Cursor

F = open('configuration.txt')
Content = F.read(5) #reads the first 5 characters of the file
print(Content)

print(F.tell()) #tells the current position of the cursor in the file
F.seek(0) #moves the cursor to the beginning of the file
Content = F.read(5) #reads the first 5 characters of the file again
print(Content)
F.close()   
