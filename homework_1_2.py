#!/usr/bin/env python

"""
Advanced Python @ NYU w/ David Blaikie
homework_1_2.py

Write a program that takes an integer as user input and uses a while loop to
generate a fibonacci series (in which each number in the series is the sum of
the previous two numbers in the series (the series begins 1, 1, 2, 3, 5, 8, 13,
etc.)) up to the user's number.
"""

from sys import argv

script, user_number = argv
user_number = int(user_number)
n = 1; print n,
m = 1; print m,
dummy = 0
sequence = 0

while (m + n) < user_number:
    sequence =  n + m
    print sequence,
    dummy = m
    m = n + m
    n = dummy
