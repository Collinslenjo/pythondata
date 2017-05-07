'''
Relational operators contrast valuea to get a boolean
only six exist:

> grater than,
< less than ,
== equal to, 
>= grater than or equl to, 
<= less than or equl to, 
!= not eaual to

'''
if 5 == 5 :
	print("My name is Bob")
else:
	print("Do not bite me")

# Logical operators
## Must return True or False (boolean)
age = 14
name = "Bob"
if age > 13 and name == "Bob":
	print("You are Eligible for Facebook")

if age > 13 or name == "Bob":
	print("You are Eligible for Facebook")

# Loops
## Repetiotion of code until the end of the condion gives a false boolean
### for loop
for i in range(0,5):
    print(i)

shopplingList = ["Milk","Bread","Eggs"]
for i in shopplingList:
	print(i)
# printing even numbers
for i in range(0,101,2):
	print(i)

###WHILE lOOPS
counter = 5
while counter < 10:
	print(counter)
	counter = counter + 1

### Nested forLoops
for i in range(0,5):
	for a in range(0,5):
		print(a)

