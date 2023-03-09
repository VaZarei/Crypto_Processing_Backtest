import yfinance as yf
import datetime
import math 
import time

from datetime import date
from datetime import datetime, date, timedelta
from datetime import datetime
from zeroKey import *

ticker       =  "ada-usd"  # lower case
start_Date   =  "2015-01-02"  #%Y/%m/%d 

#end_Date     =  "2023-02-10"
end_Date     =  datetime.now()
#interval     =  "5m"  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
intervalA    =  ["1m", "2m", "5m", "15m", "30m", "60m", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 
intMaxLen = 14

###################################################################################################################################33

a = {"sum":["1m", ["A","B", "C","D"]] , "RSI":["1m", ["A","B", "C","D"]]}


"""
print(a)
print(a["sum"])
print(a["sum"][0])
print(a["sum"][2])
print(a["sum"][2][0])
print(a["sum"][3])
print("-------------")
t= list(a.values())

#print(t[0])
#print(t)

"""

#print(list(a.values()))

data = yf.download(tickers= ticker, start= start_Date , end= end_Date, interval= "1mo")
print(data)