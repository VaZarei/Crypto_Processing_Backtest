

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
from configVar import main_Var
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler

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




# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------    

           



mydb = mysql.connector.connect(
    
  host= mySqlConf("host"),
  user= mySqlConf("user"),
  password= mySqlConf("pass"),
  database=mySqlConf("database_name")

)


# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     


if main_Var['backTestInput'] == "yes" :
       
    
        data_backtest_dict = fetch_Data_backtest(strTicker=main_Var['s_ticker'], strStart_Date=main_Var['start_Date'], strEnd_Date=main_Var['end_Date'], Interval = main_Var['intervalA'])
        

      

        for index , interval in enumerate(main_Var['intervalA']) :
                
                globals()[f"i_{interval}"] = data_backtest_dict[f"{interval}"][0]
                df = data_backtest_dict[f"{interval}"][0]
                df1 = df
                
                df.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1 , inplace=True)
                
                
                df['RSI']         = ''
                df['rsiSMA']      = ''



                df['SMA_1']         = ''
                df['SMA_2']         = ''

                df['dSMA_1']      = '' 
                df['dSMA_2']      = '' 
                df['dClose']      = ''
               
                df['transAction'] = ''
                df['PriceAction'] = ''
                df['Money']       = ''
                df['Quantity']    = ''
                df['snapCost']    = ''
                df['FinallyCostBenefit'] = ''
        

                
                df['RSI'] = round(talib.RSI((globals()[f"i_{interval}"]['Close']), 20) , 3)  
                df['rsiSMA'] = talib.EMA(df['RSI'], 10)

                df['SMA_1'] = talib.SMA((globals()[f"i_{interval}"]['Close']), 15)
                df['SMA_2'] = round(talib.SMA((globals()[f"i_{interval}"]['Close']), 30),4)
                
               
                df['dSMA_1'] = distanceF(df['Close'], df['SMA_1'], df)
                df['dSMA_2'] = distanceF(df['Close'], df['SMA_2'], df)


                df['dClose'] = distanceF(df['Close'], df.Close.shift(1), df)
                

                

                #ser1 = globals()[f"i_{interval}"]['Close']
                #ser2 = globals()[f"i_{interval}"]['SMA']
                
                
                
                
                buyCounter, sellCounter, tradeCounter = traDisF(df)
                costF(df, main_Var['intMoney'], main_Var['floatFee'])
                
             




                
                print(f"\n\n buyCounter : {buyCounter}    sellCounter : {sellCounter}   tradeCounter : {tradeCounter}" )
                df.to_excel(f'i_{interval}.xlsx', sheet_name=(f'i_{interval}'))


                globals()[f"df_{interval}"] = pd.DataFrame(globals()[f"i_{interval}"])
                globals()[f"df_{interval}"] = globals()[f"df_{interval}"].reset_index()
    
                if globals()[f"df_{interval}"].columns[0] == "Datetime" :
                        globals()[f"df_{interval}"].rename(columns={'Datetime' : 'Date'} , inplace= True)



                 




                #globals()[f"hisp_{interval}"] = B_rsi(globals()[f"df_{interval}"])

                

     
        

        x = globals()[f"df_{interval}"].Date
        y1=round((globals()[f"df_{interval}"].Close), 6)
        

        y2=(globals()[f"df_{interval}"].RSI)
        y3=(globals()[f"df_{interval}"].SMA_1)
        y4=(globals()[f"df_{interval}"].SMA_2)  
        y5= df['rsiSMA']     
        
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
        axs[1].plot(x, y5, 'tab:red')
        axs[1].set_ylabel('RSI')
        axs[1].grid()

        
        # fill area above 70 and below 30
        axs[1].fill_between(x, np.ones(len(x))*30, color="blue", alpha=0.1)
        axs[1].fill_between(x, np.ones(len(x))*70, np.ones(len(x))*100, color="red", alpha=0.1)
        
        axs[1].plot(x, np.ones(len(x))*30, color="blue", linestyle="dotted")
        axs[1].plot(x, np.ones(len(x))*70, color="red", linestyle="dotted")
        
        fig.subplots_adjust(hspace=0.1)

        mplcursors.cursor(hover=True)
       

        #print("data_backtest_dict :  :   :  :   :   :  : \n", data_backtest_dict)
        plt.show()

   

       

# ---------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     

if main_Var['onlineFire'] == "yes" :         
    



        #intervalA = ["5m", "15m"]

        data_online = updateData(main_Var.intervalA, main_Var.ticker, main_Var.start_Date)
 



        print("\n\nData_Online : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n", data_online)

        print("\n\nSleeping for 4 minutes and fetch online again ...!! ")
        time.sleep(240)
        print("\n\nWake up and fetch Online !!!\n\n")


        