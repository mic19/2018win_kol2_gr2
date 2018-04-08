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

import statistics
import json

students = {}

diary = {}
diary["math"] = {}
diary["english"] = {}

def add_student(students, name, surname):
	students[len(students) + 1] = (name, surname)
	return len(students)
	
def assign_subjects(diary, index, *args):
	for subject in args:
		diary[subject][index] = {}
		diary[subject][index]["grades"] = []
		diary[subject][index]["attendance"] = []
	
def add_grade(diary, index, subject, *args):
	for grade in args:
		diary[subject][index]["grades"].append(grade)
	
def get_grades(diary, index, subject = None):
	if subject == None:
		grades_across = []
		for subject in diary:
			grades_across += diary[subject][index]["grades"]
		return grades_across
	return diary[subject][index]["grades"]

def add_attendace(diary, index, subject, *args):
	for attend in args:
		diary[subject][index]["attendance"].append(attend)
		
def get_attendance(diary, index, subject):
	return diary[subject][index]["attendance"]

def save_to_file(diary, students, path):	
	dict_to_save = {}
	dict_to_save["diary"] = diary
	dict_to_save["students"] = students
	
	j = json.dumps(dict_to_save)
	f = open(path, "w")
	f.write(j)
	f.close()
	
def load_from_file(path):
	dict_from_file = {}
	with open(path, "r") as f:
		dict_from_file = json.loads(f.read())
	diary = dict_from_file["diary"]
	students = dict_from_file["students"]

if __name__ == "__main__":
	print("Example\nBefore assigning students:")
	print(diary)
	index = add_student(students, "Jeremy", "Waterfall")
	assign_subjects(diary, index, "math", "english")
	index = add_student(students, "Joseph", "Parker")
	assign_subjects(diary, index, "math", "english")
	
	print("\nAfter assigning students:")
	print(diary)
	add_grade(diary, 1, "math", 3, 4)
	add_attendace(diary, 1, "math", True, True)
	add_grade(diary, 2, "math", 4, 5)
	add_attendace(diary, 2, "math", True, True)

	add_grade(diary, 1, "english", 4, 5)
	add_attendace(diary, 1, "english", True, True)
	add_grade(diary, 2, "english", 3, 5)
	add_attendace(diary, 2, "english", True, True)
	
	print("\nAfter giving grades:")
	print(diary)
	
	temp = get_grades(diary, 1)
	print("\nGrades of studnet with index 1 across all subjects:")
	print(temp)
	print("Average:")
	print(statistics.mean(temp))
	
	save_to_file(diary, students, "task.json")
	

