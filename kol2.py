#
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

import argparse
import json
from collections import defaultdict

parser = argparse.ArgumentParser(description='Menu')


class ClassDiary:
    diary = defaultdict(list)
    courses = ["English", "Maths", "Chemistry", "Physics"]
    squad = [["English", [
        {'name': 'Jan', 'surname': 'Kowalski', 'attendance': 3, "grades": [3, 4, 5, 3, 3]},
        {'name': 'Joahim', 'surname': 'Schmidt', 'attendance': 4, "grades": [5, 5, 5, 5, 5]},
        {'name': 'Pedro', 'surname': 'Suarez', 'attendance': 3, "grades": [4, 3, 3, 3, 2]},
        {'name': 'John', 'surname': 'Smith', 'attendance': 4, "grades": [3, 4, 4, 2, 2]}]],
             ["Maths", [
                 {'name': 'Jan', 'surname': 'Kowalski', 'attendance': 1, "grades": [3, 4, 4, 3, 3]},
                 {'name': 'Joahim', 'surname': 'Schmidt', 'attendance': 1, "grades": [3, 4, 4, 3, 3]},
                 {'name': 'Pedro', 'surname': 'Suarez', 'attendance': 3, "grades": [3, 4, 4, 3, 3]},
                 {'name': 'John', 'surname': 'Smith', 'attendance': 3, "grades": [3, 4, 4, 3, 3]}]]
             ]

    def creatediary(self):
        for course, student in self.squad:
            self.diary[course].append(student)

    def gettotalaverageofstudent(self, name, surname):
        total_average = []
        for subject, students in self.diary.iteritems():
            for student in students:
                for person in student:
                    if person.get('name') == name and person.get('surname') == surname:
                        grades = person.get('grades')
                        # print grades
                        # print sum(grades)/float(len(grades))
                        total_average.append(sum(grades) / float(len(grades)))
        print sum(total_average) / float(len(total_average))
        return sum(total_average) / float(len(total_average))

    def gettotalaverageofall(self):
        total_all_average = []
        for subject, students in self.diary.iteritems():
            for student in students:
                for person in student:
                    total_all_average.append(self.gettotalaverageofstudent(person.get('name'), person.get('surname')))
        print sum(total_all_average) / float(len(total_all_average))
        return sum(total_all_average) / float(len(total_all_average))

    def getcourseaverageofstudent(self, name, surname, course):
        for subject, students in self.diary.iteritems():
            if subject == course:
                for student in students:
                    for person in student:
                        if person.get('name') == name and person.get('surname') == surname:
                            grades = person.get('grades')
                            print sum(grades) / float(len(grades))
                            return sum(grades) / float(len(grades))

    def getcourseaverageofall(self, course):
        average_of_course = []
        for subject, students in self.diary.iteritems():
            if subject == course:
                for student in students:
                    for person in student:
                        average_of_course.append(
                            self.getcourseaverageofstudent(person.get('name'), person.get('surname'), course))
        print sum(average_of_course) / float(len(average_of_course))

    def getattendance(self, name, surname):
        attendance = []
        for subject, students in self.diary.iteritems():
            for student in students:
                for person in student:
                    if person.get('name') == name and person.get('surname') == surname:
                        attendance.append({str(subject): person.get('attendance')})
        print attendance

    def dumptojson(self):
        print json.dumps(classDiary.diary, ensure_ascii=False, sort_keys=True, indent=4)


classDiary = ClassDiary()
classDiary.creatediary()
# classDiary.gettotalaverageofstudent("Jan", "Kowalski")
# classDiary.getcourseaverageofstudent("Jan", "Kowalski", "English")
# classDiary.getcourseaverageofall("English")
# classDiary.getattendance("Jan", "Kowalski")
# TODO: total attendance, user interface, json
