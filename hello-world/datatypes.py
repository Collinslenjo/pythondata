# Datatypes and Ints using operators
#Addition
age1 = 20
age2 = 42
age3 = age1 + age2
print(age3)
#subtraction
age1 = 20
age2 = 42
age3 = age1 - age2
print(age3)
#multiplication
age1 = 20
age2 = 42
age3 = age1 * age2
print(age3)
#division
age1 = 20
age2 = 42
age3 = age1 / age2
print(age3)
#modulus
age1 = 20
age2 = 42
age3 = age1 % age2
print(age3)

# Datatypes in strings
# concatenating
firstname = "Collins"
lastname = "Lenjo"
fullname = firstname + " " + lastname
print(fullname)
# return one only (slice)
random = "collo kjrgfvyhurthgehgiojgekrhbij;gkdhufiugj erghlflije"
getter = random[0:5]
ally = random[0:]
print(ally)
print(getter)

# DataTypes Lists
shoppingList =["apples", "carrots", "milk", "bread", "eggs"]
print(shoppingList[2])
#deleting from a list
del shoppingList[2] #function
print (shoppingList)

array1 = [12,23,56]
array2 = [52,25,76]
array3 = array1 + array2
print(array3)

print len(shoppingList) #function

numArray = [150,4000, 380, 46]

print max(numArray) #function
print min(numArray) #function

shoppingList.append("Brocoli") #function
print (shoppingList)

print shoppingList.count("carrots") #function

# Dictionaries Datatypes
students = {"Erick":14,"Victor":12,"Tina":26,"Chris":15}
print students["Victor"]
#Updating the dicionary
students["Victor"] = 13;
print students["Victor"]
#deleting
del students["Victor"]
print(students)

'''
Dictionary functions
'''
students = {"Steve":12,"Prof":16,"Edgar":14}
students.clear() #clearing sunctions
print students
#del students
#print students

students = {"Steve":12,"Prof":16,"Edgar":14}
print len(students) #function
print students.keys() #function
print students.values() #function

student2 = {"Erick":14,"Victor":12,"Tina":26,"Chris":15}

students.update(student2)
print students