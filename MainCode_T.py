

from zeroKey import *

import sqlalchemy
import pandas as pd
import mysql.connector
import talib
import time
import math
import subprocess
 
from sqlalchemy import create_engine, text
from Fetch_YF_Functons import *
from backAl import *
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.dates as mdates
from matplotlib import dates
import mplcursors

#import datetime




# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------
subprocess.call([r'Freeze.bat'])
# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------

ticker       =  "ada-usd"  # lower case
start_Date   =  "2023-02-15"  #%Y/%m/%d 

#end_Date     =  "2023-06-01"
end_Date     =  datetime.now()
intervalA     =  ["1d"]  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
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
       
        i_1d = {}
        data_backtest_dict = fetch_Data_backtest(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, Interval = intervalA)
        #i_60m = []

        for interval in intervalA :

                
                globals()[f"i_{interval}"] = []
                globals()[f"i_{interval}"] = data_backtest_dict[f"{interval}"][0]
                globals()[f"i_{interval}"]['RSI'] = round(talib.RSI((globals()[f"i_{interval}"]['Close']), 7) , 3)
                globals()[f"i_{interval}"]['EMA'] = talib.EMA((globals()[f"i_{interval}"]['Close']), 5)
                

        

        

        df = pd.DataFrame(i_1d)
        df = df.reset_index()
        #print(df)
        print(df.columns[0])
        if df.columns[0] == "Datetime" :
                df.rename(columns={'Datetime' : 'Date'} , inplace= True)
        print(df.shape)
        print(df.columns[0])
        hisp = B_rsi(df)
        
        
 
        

        #print(list(hisp.keys())[0])
        #print("hisp: \n\n" , hisp)

        x = df.Date
        y1=round((df.Close), 2)
        y3=(df.EMA)
        y2=(df.RSI)       
        
        fig, axs = plt.subplots(2 ,  sharex=True, sharey=False)
        
      
        axs[0].plot(x, y1, x, y3)
        axs[0].set_ylabel('Price')
        axs[0].grid()

        
        for i in hisp.keys():
                print(hisp[i])

        for i in hisp.keys():
               print(i)
               axs[0].scatter(x.iloc[i], y1.iloc[i], color = 'green')
               axs[0].scatter(x.iloc[int((hisp[i])[0]['j'])], y1.iloc[int((hisp[i])[0]['j'])], marker="*", color = 'red' )
        

               axs[1].scatter(x.iloc[i], y2.iloc[i],  color = '#88c999')
               axs[1].scatter(x.iloc[int((hisp[i])[0]['j'])], y2.iloc[int((hisp[i])[0]['j'])], marker="*", color = 'red' )
       


        axs[1].plot(x, y2, 'tab:green')
        axs[1].set_ylabel('RSI')
        axs[1].grid()

        # fill area above 70 and below 30
        axs[1].fill_between(x, np.ones(len(x))*30, color="blue", alpha=0.1)
        axs[1].fill_between(x, np.ones(len(x))*70, np.ones(len(x))*100, color="red", alpha=0.1)
        
        axs[1].plot(x, np.ones(len(x))*30, color="blue", linestyle="dotted")
        axs[1].plot(x, np.ones(len(x))*70, color="red", linestyle="dotted")
        
        fig.subplots_adjust(hspace=0.1)

        mplcursors.cursor(hover=True)
       

        
        plt.show()




       

# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     

if onlineFire == "yes" :         
    



        #intervalA = ["5m", "15m"]

        data_online = updateData(intervalA, ticker, start_Date)
 



        print("\n\nData_Online : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n", data_online)

        print("\n\nSleeping for 4 minutes and fetch online again ...!! ")
        time.sleep(240)
        print("\n\nWake up and fetch Online !!!\n\n")


        