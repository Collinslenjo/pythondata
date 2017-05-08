'''
Functions In python
'''

def Funcname(name):
	print("Hello, %s" %name)

Funcname("Collins")

# sample two (tax return)
def taxReturn(cost):
	return cost * 1.1

print(taxReturn(100))

#Usage of global variables
num1 = 100
num2 = 200
def add():
	return num1 + num2

print(add())

# Pre-defined functions
abs(-500) # Absoulute values
bool(0) # Boolean false
bool(1) # Boolean True
dir() # Directory
help() # help
max() # maximum
min() # minimum
len() # length
str() # Convert to String
print() # preview
range() # Range
sum() # Addition
float() # Float values
int() # Integer values