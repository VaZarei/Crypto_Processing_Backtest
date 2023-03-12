

from zeroKey import *
from PlotP import *
import sqlalchemy
import pandas as pd
import mysql.connector
import talib
import time
import math
import subprocess
 
from sqlalchemy import create_engine, text
from Fetch_YF_Functons import *
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.dates as mdates
from matplotlib import dates
#import datetime




# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------
subprocess.call([r'Freeze.bat'])
# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------

ticker       =  "ada-usd"  # lower case
start_Date   =  "2023-02-02"  #%Y/%m/%d 

#end_Date     =  "2023-02-10"
end_Date     =  datetime.now()
intervalA     =  ["15m"]  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
#intervalA    =  ["1m", "2m", "5m", "15m", "30m", "60m", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 
intMaxLen = 14

# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------    
backTestInput = "yes"  # " no"
onlineFire    = "no"
           



mydb = mysql.connector.connect(
    
  host= mySqlConf("host"),
  user= mySqlConf("user"),
  password= mySqlConf("pass"),
  database=mySqlConf("database_name")

)


# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     


if backTestInput == "yes" :
       
        i_90m = {}
        data_backtest_dict = fetch_Data_backtest(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, Interval = intervalA)
        #i_60m = []

        for interval in intervalA :

                
                globals()[f"i_{interval}"] = []
                globals()[f"i_{interval}"] = data_backtest_dict[f"{interval}"][0]

                globals()[f"i_{interval}"]['RSI'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                

        

        
        
  
        
        
        fig, ax = plt.subplots(figsize=(10, 8)) 
        formatter = dates.DateFormatter('%Y-%m-%d %S:%M:%H')
        ax.xaxis.set_major_formatter(formatter)
        plt.gcf().autofmt_xdate(rotation=90)

        ax.xaxis.set_major_locator(dates.DayLocator(interval=2))

        
        plt.plot(globals()[f"i_{interval}"]['Open'] )
        plt.plot(globals()[f"i_{interval}"]['Close'] )
        plt.xticks(rotation=90)
        
        plt.show()
        
      

      


        
        
     












# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     

if onlineFire == "yes" :         
    



        #intervalA = ["5m", "15m"]

        data_online = updateData(intervalA, ticker, start_Date)
 



        print("\n\nData_Online : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n", data_online)

        print("\n\nSleeping for 4 minutes and fetch online again ...!! ")
        time.sleep(240)
        print("\n\nWake up and fetch Online !!!\n\n")