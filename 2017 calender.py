#import datetime

#now = datetime.date(201, 7, 14)

#print(datetime.date.today().year)

import calendar
year=2017

for month in range(1,13):
 print(calendar.month(year,month))
