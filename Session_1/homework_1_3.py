#!/usr/bin/env python

"""
Advanced Python @ NYU w/ David Blaikie
homework_1_3.py

(Extra credit) Find prime numbers in a range of numbers. Ask the user for an
integer, and display all prime numbers (i.e., numbers that have no even divisor
above 1) between 2 and the user's number.
"""

print '* Prime Numbers *'

max_integer = int(raw_input('Please enter max integer: '))

for i in range(2, max_integer+1):

    prime = True

    for j in range(2,i):
        remainder = i % j
        if remainder == 0:
            prime = False
        else: pass

    if prime: print i
    else: pass
