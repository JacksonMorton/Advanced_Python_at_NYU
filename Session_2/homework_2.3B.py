#!/usr/bin/env Python

"""
Advanced Python @ NYU w/ David Blaikie
homework_2_1B.py

Reading through stock_prices.csv, build a dict of lists in which the key is the
stock ticker and the value is a list of closing prices for that ticker. Sort the
tickers by the difference between the highest and lowest close prices for each
stock ticker for the year.
"""

stock_prices = open('/Users/Jackson/Desktop/code/nyu/stock_prices.csv')\
               .readlines()[1:]

closing_prices = {}
for item in stock_prices:
    entry = item.split(',')
    if entry[0] not in closing_prices:
        closing_prices[entry[0]] = []
    else:
        closing_prices[entry[0]].append(float(entry[5]))

#print closing_prices

tickers = []
for key in closing_prices:
    high = max(closing_prices[key])
    low = min(closing_prices[key])
    diff = round((high - low), 2)
    tickers.append((key, high, low, diff))

sort_tickers = sorted(tickers, key=lambda ticker: ticker[3], reverse=True)

for item in sort_tickers:
    print "{}:  {} difference ({}-{})".format(item[0], item[3], item[1], item[2])
