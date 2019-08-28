# Script used for reading and plotting purchase history

import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

y = []
dates = []

# Takes a raw object and extract the dates into the right formating to be plotted
def create_dates(purchased_objects): 
    dates_array = purchased_objects.split("-")
    for i in range(len(dates_array)):
        dates_array[i] = int(dates_array[i].strip("0"))
    return dates_array

# Amount, price
coffee = [0] * 2

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

    # Gives the coffee purchases a date
    if purchased_object[0] == string:
        temp_date = purchased_object[4]
    else:
        purchased_object[4] = temp_date

        # If a kaffehäfte is bought, add more cups
        if "KAFFE" in purchased_object[0]:
            year = create_dates(purchased_object[4])[0]
            month = create_dates(purchased_object[4])[1]
            day = create_dates(purchased_object[4])[2]
            #day = 15


            if "KAFFEH" in purchased_object[0]:
                coffee[0] += 20
                #Wrong value atm for graphical reasons
                y.extend([1])
            else:
                coffee[0] += int(purchased_object[1])
                y.extend([int(purchased_object[1])])       

            # Calculating the total cost
            edited_string = purchased_object[2].replace(",",".")
            coffee[1] += float(edited_string)

            # Creating an array of dates
            dates.extend([datetime(year , month , day)])
#print(dates)
            
plt.style.use('seaborn')
plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()


