import time
import datetime
import pandas as pd 

# for exampel vti is vanguard total index
# we can any stock ticker avalable on yhaoo finance  
spy500 = 'VTI'
#time.mktime() method of Time module is used to convert a time. struct_time object or a tuple containing 9 elements corresponding to time. struct_time object to time in seconds passed since epoch in local time.
period1 = int(time.mktime(datetime.datetime(2010, 12, 1, 23, 59).timetuple()))#starting 
period2 = int(time.mktime(datetime.datetime(2021, 10, 31, 23, 59).timetuple()))#ending
#price up date after a month. we can also heve 1d 5d 
interval = '1mo' #price up date after a month. we can also heve 1d 5d 

#here we plug in veriables with help of fsting 
banch_mark_string = f'https://query1.finance.yahoo.com/v7/finance/download/{spy500}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

#here we use pandas.read_csv method to read data 
bench_markdf = pd.read_csv(banch_mark_string)
print(bench_markdf.head())



