class Student:
	# All classes must be initialized by this method
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age

kitty = Student('Kitty',80,25)
daniel = Student('Daniel',85,23)
#concatenation
print(kitty.name +' is '+str(kitty.age) + ' old and attained '+str(kitty.grade)+ ' marks in Mathematics')