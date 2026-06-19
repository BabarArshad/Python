# intro to python strings

str1 = "I am learning Python3"
str2 = 'I am learning Python3'
print(str1)


# There is no difference between single or double quotes when using strings.
# What is important for you is to try to remain consistent within your code.
# Use either single quotes or double quotes, but do not mix them.

#Hi the I'm Babar 
str3 = 'Hi the I\'m Babar'
print(str3)
#or
str4 = "Hi the I'm Babar"
print(str4) 
#or 
str5 = 'Hi the I"m Babar'
print(str5)
#or 
str6 = "Hi the I\"m Babar"
print(str6)

print(type(str5))


# to creat a docuement or write string in multiple lines we can use triple quotes
str7 = '''This is a string that spans multiple lines. It can be used to create docstrings or to write long strings without the need for concatenation.'''
print(str7)
str8 = """I like Bike
Car 
cycle"""
print(str8)

str9 = "I like Bike\nCar\ncycle" #another way to write string in multiple lines using \n
print(str9)

print("a\tb\tc\n1\t2\t3") #using \t to create a tab space between the characters

print("He says: 'I\'m learning Python3'") #using \ to escape the single quote inside the string

print("\\ is a backslash character") #using \\ to print a single backslash character
