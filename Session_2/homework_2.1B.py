#!/usr/bin/env Python

"""
Advanced Python @ NYU w/ David Blaikie
homework_2_1B.py

Create a sort function that will cause sorted() to sort the file lines in
revenue.txt by the float value at the end of each line. Do not build a new
container of values - sort the lines as they are. When you get the sort function
to work, convert it to a lambda.
"""

lines = open('/Users/Jackson/Desktop/code/nyu/revenue.txt').readlines()

slines = sorted(lines, key=lambda line: float(line.split(',')[2]))

print slines

# The commented code below represents the solution to problem without using a
# lambda function.
# def get_float(line):
#     return float(line.split(',')[2])
#
# slines = sorted(lines, key=get_float)
