

from zeroKey import *
from backDisAlgo import *

import sqlalchemy
import pandas as pd
import numpy as np
import mysql.connector
import talib
import time
import openpyxl
import subprocess
import math
 
from sqlalchemy import create_engine, text
from Fetch_YF_Functons import *
from backAl import *
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Alignment

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
start_Date   =  "2023-02-01"  #%Y/%m/%d 

end_Date     =  "2023-03-13"
end_Date     =  datetime.now()
intervalA     =  ["60m"]  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
#intervalA    =  ["1m", "2m", "5m", "15m", "30m", "60m", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 
intMaxLen = 14
rsi_period = 7


intMoney = 1000
floatFee = 0.005

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

      

        for index , interval in enumerate(intervalA) :
                
                globals()[f"i_{interval}"] = data_backtest_dict[f"{interval}"][0]
                df = data_backtest_dict[f"{interval}"][0]
                
                df.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1 , inplace=True)
                
                
                df['RSI']         = ''
                df['EMA']         = ''
                df['dEMA']        = '' 
                df['SMA']         = ''
                #df['SMA']         = ''
               
               
                df['transAction'] = ''
                df['PriceAction'] = ''
                df['Money']       = ''
                df['Quantity']    = ''
                df['snapCost']    = ''
                df['FinallyCostBenefit'] = ''
        

                
                df['RSI'] = round(talib.RSI((globals()[f"i_{interval}"]['Close']), 12) , 3)   
                df['EMA'] = talib.EMA((globals()[f"i_{interval}"]['Close']), 30)
                df['SMA'] = talib.SMA((globals()[f"i_{interval}"]['Close']), 14)
                df['dEMA'] = distanceF(globals()[f"i_{interval}"]['Close'], globals()[f"i_{interval}"]['EMA'], df)
                
                

                

                ser1 = globals()[f"i_{interval}"]['Close']
                ser2 = globals()[f"i_{interval}"]['SMA']
                
                
                
                
                traDisF(df)
                costF(df, intMoney, floatFee)

                

                df.to_excel(f'i_{interval}.xlsx', sheet_name=(f'i_{interval}'))


                globals()[f"df_{interval}"] = pd.DataFrame(globals()[f"i_{interval}"])
                globals()[f"df_{interval}"] = globals()[f"df_{interval}"].reset_index()
    
                if globals()[f"df_{interval}"].columns[0] == "Datetime" :
                        globals()[f"df_{interval}"].rename(columns={'Datetime' : 'Date'} , inplace= True)



                 




                globals()[f"hisp_{interval}"] = B_rsi(globals()[f"df_{interval}"])

                

     
        

        x = globals()[f"df_{interval}"].Date
        y1=round((globals()[f"df_{interval}"].Close), 6)
        
        y2=(globals()[f"df_{interval}"].RSI)
        y3=(globals()[f"df_{interval}"].EMA)
        y4=(globals()[f"df_{interval}"].SMA)       
        
        fig, axs = plt.subplots(2 ,  sharex=True, sharey=False)
        
      
        axs[0].plot(x, y1, color = '#4D4646')
        axs[0].plot(x, y3, x,y4)
        axs[0].set_ylabel('Price')
        axs[0].grid()

        
    
        for i in range(len(df)):
               
               if df['transAction'][i] == "Buy" :
                       axs[0].scatter(x.iloc[i], y1.iloc[i], color  = 'green')
                       axs[1].scatter(x.iloc[i], y2.iloc[i],  color = 'green')

               if df['transAction'][i] == "Sell" :
                       axs[0].scatter(x.iloc[i], y1.iloc[i], color  = 'red')
                       axs[1].scatter(x.iloc[i], y2.iloc[i],  color = 'red')
                       
               
               
               





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
       

        print("data_backtest_dict :  :   :  :   :   :  : \n", data_backtest_dict)
        plt.show()

   

       

# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     

if onlineFire == "yes" :         
    



        #intervalA = ["5m", "15m"]

        data_online = updateData(intervalA, ticker, start_Date)
 



        print("\n\nData_Online : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n", data_online)

        print("\n\nSleeping for 4 minutes and fetch online again ...!! ")
        time.sleep(240)
        print("\n\nWake up and fetch Online !!!\n\n")


        