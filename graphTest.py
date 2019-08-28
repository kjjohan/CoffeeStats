# Test for plot
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

dates = [
    datetime(2019, 4, 25),
    datetime(2019, 5, 25),
    datetime(2019, 6, 26),
    datetime(2019, 7, 27)
]
print(dates[3].month)
print(dates[len(dates)-1].month)
y = [0, 1, 2, 3]

plt.plot_date(dates, y, linestyle='solid')

plt.gcf().autofmt_xdate()

#date_format = mpl_dates.DateFormatter('%b, %Y')

#plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.show()



