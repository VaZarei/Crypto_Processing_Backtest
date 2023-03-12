

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
start_Date   =  "2023-03-02"  #%Y/%m/%d 

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
       
        i_15m = {}
        data_backtest_dict = fetch_Data_backtest(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, Interval = intervalA)
        #i_60m = []

        for interval in intervalA :

                
                globals()[f"i_{interval}"] = []
                globals()[f"i_{interval}"] = data_backtest_dict[f"{interval}"][0]
                globals()[f"i_{interval}"]['RSI'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                

        

        
        #print(i_15m.index)
        #print(i_15m['Open'])

        df = i_15m

        df = df.reset_index()

        #print(df.Datetime)
        #print(df.Open)        
        """
        fig, ax = plt.subplots(figsize=(10, 8)) 
        formatter = dates.DateFormatter('%Y-%m-%d %S:%M:%H')
        ax.xaxis.set_major_formatter(formatter)
        plt.gcf().autofmt_xdate(rotation=90)

        ax.xaxis.set_major_locator(dates.DayLocator(interval=2))

        
        plt.plot(df.Datetime , df.Open )
        plt.plot(df.Datetime )
        plt.xticks(rotation=90)
        
        plt.show()
        
        """
        """
        # plot price
        plt.figure(figsize=(15,5))
        plt.plot(df.Datetime, df.Open)
        plt.title('Price chart (Adj Close)')
        plt.show()


        # plot correspondingRSI values and significant levels
        plt.figure(figsize=(15,5))
        plt.title('RSI chart')
        plt.plot(df.Datetime, df['RSI'])

        plt.axhline(0, linestyle='--', alpha=0.1)
        plt.axhline(20, linestyle='--', alpha=0.5)
        plt.axhline(30, linestyle='--')

        plt.axhline(70, linestyle='--')
        plt.axhline(80, linestyle='--', alpha=0.5)
        plt.axhline(100, linestyle='--', alpha=0.1)
        plt.show()

        """

        #
        
        x = df.Datetime
        y1 = df.Open
        y2 = df.RSI
        
        fig, axs = plt.subplots(2 ,  sharex=True, sharey=True)
        
        axs[0].plot(x, y1)
        axs[0].set_title('Price')
      
        axs[0].set_ylim(ymin=0, ymax=0.6)
  
        plt.scatter(x.iloc[200], y1.iloc[200], marker="o", s=10, color="r", alpha=0.9)
        


        axs[1].plot(x, y2, 'tab:green')
        axs[1].set_title('RSI')
     

        plt.show()














# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     

if onlineFire == "yes" :         
    



        #intervalA = ["5m", "15m"]

        data_online = updateData(intervalA, ticker, start_Date)
 



        print("\n\nData_Online : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n", data_online)

        print("\n\nSleeping for 4 minutes and fetch online again ...!! ")
        time.sleep(240)
        print("\n\nWake up and fetch Online !!!\n\n")