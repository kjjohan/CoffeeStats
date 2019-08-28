# Script used for reading and plotting purchase history

import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

# [Amount, price]
coffee = [0] * 2

y = []
dates = []
start = True

# Takes a raw object and extract the dates into the right formating to be plotted
def create_dates(object_date): 
    dates_array = object_date.split("-")
    for i in range(len(dates_array)):
        dates_array[i] = int(dates_array[i].lstrip("0"))
    return dates_array

# Updates values on y and dates
def coffee_calc(purchased_object):
    global y
    global dates
    global start
    global coffee

    year = create_dates(purchased_object[4])[0]
    month = create_dates(purchased_object[4])[1]
    day = 15
    print(month)

    if start:
        start = False
        dates.extend([datetime(year , month , day)])
        y.extend([int(purchased_object[1])])
    else:
        latest_object = dates[len(dates)-1]
        # If true, only update value of previous y
        if(latest_object.year == year and latest_object.month == month):
            y[len(y)-1] += int(purchased_object[1])
        else:
            dates.extend([datetime(year , month , day)])
            y.extend([int(purchased_object[1])])

    # Calculating amount of coffees
    coffee[0] += int(purchased_object[1])
    # Calculating the total cost
    edited_string = purchased_object[2].replace(",",".")
    coffee[1] += float(edited_string)

f = open("kontoutdrag20190828.txt", "r")
history = f.readlines()
# Ugliest solution i could find, why is this even a problem lol
compare_object = history[len(history)-1]
string = compare_object.split("\t")[0]
history = reversed(history)
f.close()

for x in history:
    edited_x = x.replace("\n", "")
    purchased_object = edited_x.split("\t")

    # Gives all the purchases a date
    if purchased_object[0] == string:
        temp_date = purchased_object[4]
    else:
        purchased_object[4] = temp_date

        if "KAFFE" in purchased_object[0]:
            coffee_calc(purchased_object)
            
plt.style.use('seaborn')
plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()


