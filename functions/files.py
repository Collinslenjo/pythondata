'''
Opening and Reading files
'''
import os

testfile = open("test.txt")
file = testfile.read()
print(file)
# finding out where the pointer is
position = testfile.tell()
# reset pointer to position 0 (placing the pointer at the beggining of the file)
position = testfile.seek(0,0)
# Closing the file after reading.
testfile.close()


# '''
# Appending and Reading files
# '''
#testfile = open("test.txt","r") # for reading only
testfile = open("test.txt","w") # for writing only (Overwrites)
#testfile = open("test.txt","wbr") # for reading, writing and binary
testfile.write("\n Collins is an amazing Developer\n")
testfile.close()

# # Appending ( Adding without overwriting the existing content)
testfile = open("test.txt","a") # appending
testfile.write("\n Do what you can do with appending\n")

'''
Copying files
'''
testfile = open("test.txt")
file = testfile.read()
os.rename("test.txt","test2.txt")
testfile.close()

# # deleting
testfile = open("test.txt")
file = testfile.read()
os.remove("test2.txt")
testfile.close()

# Getting an input from a user and copying it to a file
filename = input("Enter your file name:")
print(filename)