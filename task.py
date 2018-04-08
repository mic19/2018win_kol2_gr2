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

students = {}

diary = {}
grades = {"1":[], "2":[], "3":[]}
diary["math"] = grades

grades = {"1":[], "2":[], "3":[]}
diary["english"] = grades

def add_student(students, name, surname):
	students[len(students) + 1] = (name, surname)
	return str(len(students))
	
def assign_subjects(index, diary, *args):
	for subject in args:
		temp = diary[subject]
		temp[index] = []
	
def get_student(students, index):
	return students[index]
	
def add_grade(diary, index, subject, *args):
	for grade in args:
		diary[subject][index].append(grade)
	
def get_grades(diary, index, subject = None):
	if subject == None:
		grades_across = []
		for subject in diary:
			grades_across += diary[subject][index]
		return grades_across
	return diary[subject][index]

def add_attendace(diary, index, subject):
	pass
		
def get_attendance(diary, index, subject):
	pass
	


if __name__ == "__main__":
	print(diary)
	index = add_student(students, "Jeremy", "Waterfall")
	#assign_subjects(diary, index, "math", "english")
	index = add_student(students, "Joseph", "Parker")
	#assign_subjects(diary, index, "math", "english")
	index = add_student(students, "Adam", "Savage")
	#assign_subjects(diary, index, "math", "english")
	
	add_grade(diary, "1", "math", 2, 3, 4)
	add_grade(diary, "2", "math", 4, 4, 5)
	add_grade(diary, "3", "math", 5, 4, 5)
	
	add_grade(diary, "1", "english", 2, 4, 5)
	add_grade(diary, "2", "english", 4, 3, 5)
	add_grade(diary, "3", "english", 5, 4, 5)
	
	print(students)
	print(diary)
	print()
	
	print(get_grades(diary, "1"))


