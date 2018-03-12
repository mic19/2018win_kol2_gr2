# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)

class Student():
	def __init__(self, name, surname, student_id, classes):
		self.name = name
		self.surname = surname
		self.student_id = student_id
		self.list = {}
		for class_name in classes:
			self.list[class_name] = []#grades

	def add_grade(self, grade, class_name):
		pass#self.grades.append(grade)
		self.list[]

class Diary():
	def __init__(self):
		self.list = {}

	def __str__(self):
		pass

	def add_student(self, student):
		self.list[student.student_id] = student

	def add_grade(self, student_id, class_name, grade):
		if(self.list[student_id] != None):
			self.list[student_id].add_grade(grade, class_name)

	"""
		self.list["class_type"] = class_type
		self.list["grades"] = []

	def add_grade(self, student_id, class_type, grade):
		list[student_id] = student_id
		list[class_type] = class_type
		list[student_id] = student_id
	"""


if __name__ == "__main__":
	diary = Diary()
	student = Student("name", "surname", 1, ("math", "english"))

	diary.add_student(student)# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)

class Student():
	def __init__(self, name, surname, student_id, classes):
		self.name = name
		self.surname = surname
		self.student_id = student_id
		self.list = {}
		for class_name in classes:
			self.list[class_name] = []#grades

	def add_grade(self, grade, class_name):
		pass#self.grades.append(grade)
		#self.list[]

class Diary():
	def __init__(self):
		self.list = {}

	def __str__(self):
		pass

	def add_student(self, student):
		self.list[student.student_id] = student

	def add_grade(self, student_id, class_name, grade):
		if(self.list[student_id] != None):
			self.list[student_id].add_grade(grade, class_name)

	"""
		self.list["class_type"] = class_type
		self.list["grades"] = []

	def add_grade(self, student_id, class_type, grade):
		list[student_id] = student_id
		list[class_type] = class_type
		list[student_id] = student_id
	"""


if __name__ == "__main__":
	diary = Diary()
	student = Student("name", "surname", 1, ("math", "english"))

	diary.add_student(student)
	diary.add_grade(1, "math", 4)





	diary.add_grade(1, "math", 4)




