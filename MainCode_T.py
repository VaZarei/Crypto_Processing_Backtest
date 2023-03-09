

from zeroKey import *
import sqlalchemy
import pandas as pd
import mysql.connector
import talib
import time
import math
 
from sqlalchemy import create_engine, text
from Fetch_YF_Functons import *
from datetime import datetime


# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------
print("pip freeze > requirements.txt")
# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------

ticker       =  "ada-usd"  # lower case
start_Date   =  "2015-01-02"  #%Y/%m/%d 

#end_Date     =  "2023-02-10"
end_Date     =  datetime.now()
intervalA     =  ["1m"]  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
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



if backTestInput == "yes" :
       

        data = fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, Interval = intervalA)
        
        #print(data)
     












        # ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
        # Read or select from table
        """
        query1 = text("select * from {table_name} where Date > '2023-02-01 12:45:00' ; ".format(table_name=table_name))     
        query1 = text("select * from {table_name}  ; ".format(table_name=table_name))     

        df = pd.read_sql(query1, database_connection().connect())
        print(df)
        """
        # ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------



if onlineFire == "yes" :             # --------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    



        #intervalA = ["5m", "15m"]

        data_online = updateData(intervalA, ticker, start_Date)
 



        print("\n\nData_Online : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n", data_online)

        print("\n\nSleeping for 4 minutes and fetch online again ...!! ")
        time.sleep(240)
        print("\n\nWake up and fetch Online !!!\n\n")