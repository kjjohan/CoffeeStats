# Script used for reading purchase history to create statistics

import numpy as np

# Amount, price
coffee = [0] * 2

f = open("kontoutdrag20190828.txt", "r")
history = f.readlines()

# Ugliest solution i could find, whyh is this even a problem lol
compare_object = history[len(history)-1]
string = compare_object.split("\t")[0]

history = reversed(history)
f.close()

for x in history:
    edited_x = x.replace("\n", "")
    purchased_object = edited_x.split("\t")
    if purchased_object[0] == string:
        temp_date = purchased_object[4]
    else:
        purchased_object[4] = temp_date
        
        if "KAFFE" in purchased_object[0]:
            # If a kaffehäfte is bought, add more cups
            if "KAFFEH" in purchased_object[0]:
                coffee[0] += 19
            coffee[0] += int(purchased_object[1])
            edited_string = purchased_object[2].replace(",",".")
            coffee[1] += float(edited_string)
            
print(coffee[0])
print(coffee[1])




