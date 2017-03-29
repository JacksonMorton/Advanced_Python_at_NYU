#!/usr/bin/env Python

"""
Advanced Python @ NYU w/ David Blaikie
homework_2_2B.py

Write a single list comprehension that returns the list of ids from
student_db.txt. Print the IDs list.
"""

student_db = open('/Users/Jackson/Desktop/code/nyu/student_db.txt').readlines()

ids = [ student.split(':')[0] for student in student_db[1:] ]

print ids
