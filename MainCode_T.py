

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
from datetime import datetime


# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------
subprocess.call([r'Freeze.bat'])
# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------

ticker       =  "ada-usd"  # lower case
start_Date   =  "2015-01-02"  #%Y/%m/%d 

#end_Date     =  "2023-02-10"
end_Date     =  datetime.now()
intervalA     =  ["90m"]  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
intervalA    =  ["1m", "2m", "5m", "15m", "30m", "60m", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 
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
       
        
        data_backtest_dict = fetch_Data_backtest(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, Interval = intervalA)
        #i_60m = []

        for interval in intervalA :

                
                globals()[f"i_{interval}"] = []
                globals()[f"i_{interval}"] = data_backtest_dict[f"{interval}"][0]

                globals()[f"i_{interval}"]['RSI'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI2'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI3'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI4'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI5'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI6'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI7'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI8'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI9'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI10'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI11'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI12'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI13'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI14'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI15'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)
                globals()[f"i_{interval}"]['RSI16'] = talib.RSI((globals()[f"i_{interval}"]['Open']), 2)


    

        

        
        

        print((i_90m))
        #print(i_60m)

        #i_60m['RSI'] = talib.RSI(i_60m['Open'], 2)

        #print(i_60m)



        
        
     












# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     

if onlineFire == "yes" :         
    



        #intervalA = ["5m", "15m"]

        data_online = updateData(intervalA, ticker, start_Date)
 



        print("\n\nData_Online : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n", data_online)

        print("\n\nSleeping for 4 minutes and fetch online again ...!! ")
        time.sleep(240)
        print("\n\nWake up and fetch Online !!!\n\n")