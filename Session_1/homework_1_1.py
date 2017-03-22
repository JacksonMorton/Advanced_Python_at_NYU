#!/usr/bin/env python

"""
Advanced Python @ NYU w/ David Blaikie
homework_1_1.py

Write a program that dynamically downloads weather data for a particular city
and year from the Weather Underground website, the computes average temperature,
range (min and max) temperatures, and standard deviation.
"""

import urllib2
from sys import argv

script, airport, year = argv

url = 'https://www.wunderground.com/history/airport/{}/{}/1/1/'\
      'CustomHistory.html?dayend=31&monthend=12&yearend='\
      '2016&format=1'.format(airport, year)

mean_temp = []

wu_data = urllib2.urlopen(url)
next(wu_data); next(wu_data)

for line in wu_data:
    if line[0:4] == year:
        line = line.split(',')
        mean_temp.append(int(line[2]))
    else: pass

yearly_mean_temp = sum(mean_temp) / float(len(mean_temp))
temp_minus_mean_temp = []
for temp in mean_temp:
    temp_minus_mean_temp.append((temp - yearly_mean_temp)**2)
variance = sum(temp_minus_mean_temp) / float(len(temp_minus_mean_temp))
sd = variance**(0.5)

print "Daily average temperature data for {} in year {}:".format(airport, year)
print "Average temp:  {}".format(yearly_mean_temp)
print "Max daily average temp:  {}".format(max(mean_temp))
print "Min daily average temp:  {}".format(min(mean_temp))
print "Standard deviation:  {}".format(sd)
