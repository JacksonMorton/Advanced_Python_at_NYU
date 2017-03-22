#!/usr/bin/env python

"""
Advanced Python @ NYU w/ David Blaikie
homework_1_4.py

(Extra Credit) Write the classic "number guessing" program in which you think
of a number and the computer program attempts to guess it. See suggested
output for behavioral details.
"""

from sys import argv
from sys import exit

print 'Think of a number between 0 and 100, and I will try to guess it.'\
      ' Hit [Enter] to start.'
raw_input()

guess_number = 50; guess_history = [50]; last_guess = 50

while True:
    guess = raw_input('Is it {}? (yes/no/quit)  '.format(guess_number))
    last_guess_dummy = guess_number

    if guess == 'yes':
        print 'I knew it!\n'
        exit(1)
    elif guess == 'quit':
        print "Leaving the number guessing game...\n"
        exit(1)
    elif guess == 'no':
        higher_lower = raw_input('Is it higher or lower than {}?  '.format(guess_number))
        if higher_lower == 'lower':
            if guess_number == min(guess_history):
                guess_number = guess_number / 2
            else:
                diffs = []
                for num in guess_history:
                    if guess_number - num > 0:
                        diffs.append(guess_number - num)
                    else: pass
                # highest_lower = highest number that has been guessed that is lower than guess_number
                highest_lower = guess_number - min(diffs)
                guess_number = guess_number - ((guess_number - highest_lower) / 2)
        elif higher_lower == 'higher':
            if guess_number == max(guess_history):
                guess_number = guess_number + ((100 - guess_number) / 2)
            else:
                diffs = []
                for num in guess_history:
                    if num - guess_number > 0:
                        diffs.append(num - guess_number)
                    else: pass
                # lowest_higher = lowest number that has been guessed that is higher than guess_number
                lowest_higher = min(diffs) + guess_number
                guess_number = guess_number + ((lowest_higher - guess_number) / 2)
        else:
            print 'Invalid response. Enter either \'higher\' or \'lower\'.'
        print '\n'
        guess_history.append(guess_number)
        last_guess = last_guess_dummy
    else:
        print 'Invalid response. Enter either \'yes\', \'no\', or \'quit\'.'
