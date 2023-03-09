import yfinance as yf
import datetime
import math 
import time
import talib
import mysql.connector

from datetime import date
from datetime import datetime, date, timedelta
from datetime import datetime
from zeroKey import *


mydb = mysql.connector.connect(
    
  host= mySqlConf("host"),
  user= mySqlConf("user"),
  password= mySqlConf("pass"),
  database=mySqlConf("database_name")

)



## BackTest >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval) :
     
     
     try:
            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            table_name="{ticker}_{interval}".format(ticker= strTicker.replace("-","") ,interval= strInterval)
            frame = data.to_sql(con= database_connection() , name=table_name , if_exists='replace')
  
     except :
             print("\n\n May be Download is Faild . I'm trying again ... ")
             errorCounter = 0
             _checkEmpty = True
             while _checkEmpty :
                                errorCounter +=1
                                print("\nErrorCounter :", errorCounter)
                                data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
                                print("startDate: ", strStart_Date, "endDate : ", strEnd_Date)
                                if data.empty:  
                                        time.sleep(5)
                                        print( "\nData is Empty.I'm Tring again...  ", strInterval)
                                else:
                                         _checkEmpty= False
                                         table_name="{ticker}_{interval}".format(ticker= strTicker.replace("-","") ,interval= strInterval)
                                         frame = data.to_sql(con= database_connection() , name=table_name , if_exists='replace')
                                         time.sleep(1)
     
     return data

def fetch_Data_backtest(strTicker, strStart_Date, strEnd_Date, Interval) :

    """
        This Function make fetch data from yahoo finance according to ticker, start and end date and timeframe(strinterval)
        output : if everything is normal is a data table
        output : if timeframe(strinterval) be incorrecy is "-1"
    """

    data_backtest_dict = {}
    for strInterval in Interval:


        sd =  strStart_Date
        ed =  strEnd_Date

        if str(type(strEnd_Date))  == "<class 'datetime.datetime'>" :
                strEnd_Date = (str(datetime.now())[0:10])
                print("---------- > End_Date = datetime.now \n\n")

        print("\n\n\nStart_Date : " , strStart_Date, "\nEnd_Date   : ", strEnd_Date, "\n\n")
        intervalDate, interval_from_Now = (count_date_Diff(str(strStart_Date), strEnd_Date))


        if (strInterval == "1m") :
            
            if intervalDate < 31 and interval_from_Now < 8 :

                print("\nStart_Date        : ", strStart_Date)
                print("End_Date          : ", strEnd_Date)
                print("interval          : ", strInterval ,"\n\n")
                
                data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                strStart_Date = sd  
                strEnd_Date   = ed
                
            
            else:
            
                delta = interval_from_Now - 29
                strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
                print("\n -------------- > Forced new start date: ", strStart_Date)
                print(" -------------- >            end   date: ", strEnd_Date , "\n")
                intervalDate, interval_from_Now = (count_date_Diff(str(strStart_Date), strEnd_Date))
            

                if intervalDate > 8 :
                    
                    decide = input("\n\"intervalDate > 8\"\nInterval between Start_Date and End_Date is more than 7 days, please choose constant:(start/end) : ")
                    delta = intervalDate - 6
                    
                    if decide == "start" :

                        strEnd_Date = str((datetime.strptime(strEnd_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
                        
                        print("\nStart_Date        : ", strStart_Date)
                        print("End_Date          : ", strEnd_Date)
                        print("interval          : ", strInterval ,"\n\n")

                        data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                        strStart_Date = sd  
                        strEnd_Date   = ed
                        
                        

                    if decide == "end" :

                        strStart_Date = str((datetime.strptime(str(strStart_Date), '%Y-%m-%d') + timedelta(days=delta)).date())

                        print("\nStart_Date        : ", strStart_Date)
                        print("End_Date          : ", strEnd_Date)
                        print("interval          : ", strInterval ,"\n\n")
                        
                        data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                        strStart_Date = sd  
                        strEnd_Date   = ed 
                        
                        

        elif (strInterval == "2m") or (strInterval == "5m") or  (strInterval == "15m") or (strInterval == "30m") or (strInterval == "90m") :
            
            if interval_from_Now < 60 :
                
                print("\nStart_Date        : ", strStart_Date)
                print("End_Date          : ", strEnd_Date)
                print("interval          : ", strInterval ,"\n\n")

                data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                strStart_Date = sd  
                strEnd_Date   = ed  

            else:
            
                delta = interval_from_Now - 59
                strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())

                print("\nStart_Date        : ", strStart_Date)
                print("End_Date          : ", strEnd_Date)
                print("interval          : ", strInterval ,"\n\n")

                data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                strStart_Date = sd  
                strEnd_Date   = ed  
                
                

        elif (strInterval == "60m") or (strInterval == "1h"):

            if interval_from_Now < 729 :
                
                print("\nStart_Date        : ", strStart_Date)
                print("End_Date          : ", strEnd_Date)
                print("interval          : ", strInterval ,"\n\n")

                data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                strStart_Date = sd  
                strEnd_Date   = ed  
                

            else:
            
                delta = interval_from_Now - 729
                strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())

                print("\nStart_Date        : ", strStart_Date)
                print("End_Date          : ", strEnd_Date)
                print("interval          : ", strInterval ,"\n\n")

                data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                strStart_Date = sd  
                strEnd_Date   = ed 
                
                

        elif (strInterval == "1d") or (strInterval == "5d")or (strInterval == "1wk")or (strInterval == "1mo")or (strInterval == "3mo"):
            
            
                print("\nStart_Date        : ", strStart_Date)
                print("End_Date          : ", strEnd_Date)
                print("interval          : ", strInterval ,"\n\n")

                data_backtest_dict[strInterval] = [tryExcept_backtest(strTicker, strStart_Date, strEnd_Date, strInterval)]
                strStart_Date = sd  
                strEnd_Date   = ed 

                
        else:
            
            pass
        


    return data_backtest_dict

def data_process_backtest (intervalA ,data_online : dict, ticker) :
    
    data_process_dict = {}

    for i in intervalA :
         
        
        table_name="{ticker}_{interval}_P".format(ticker= ticker.replace("-","") ,interval= i)
        mycursor = mydb.cursor()
        query = """
                create table IF NOT EXISTS {table_name}({Date} varchar(50));
                                                         
                
                                                        

                  
                """.format(table_name = table_name, Date = data_online[i].columns[0] )
        print("Query >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> : \n", query)
        #val = ["2024-01-01" , "254789"]
        mycursor.execute(query)
        mydb.commit()

        table_name="{ticker}_'P_'{interval}".format(ticker= ticker.replace("-","") ,interval= i)
        data_process_dict["sum"]  = [i, sum(data_online[i]["Open"])]
        data_process_dict["RSI"]  = [i, talib.RSI(data_online[i]["Open"])]
         
        print("-----------------------------------------------")
        

    #print(data_process_dict.keys())
    #print(data_process_dict)

    return data_process_dict

          












## Online Fire >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def count_date_Diff (start_Date, end_Date) :

    """ 
        This Function count deferent interval between start to end date
        The output is integer and only Date 
    """
    
   
    if str(type(end_Date))  == "<class 'datetime.datetime'>" :
        end_Date = (str(datetime.now())[0:10])
        print("yess")

    startDate = date(int(start_Date[0:4]) , int(start_Date[5:7]),  int(start_Date[8:10]))
    endDate = date(int(end_Date[0:4]) , int(end_Date[5:7]),  int(end_Date[8:10]))
    intervalDate = endDate - startDate  
    end_Now = end = (str(datetime.now())[0:10])
    end_wanted = date(int(end_Now[0:4]) , int(end_Now[5:7]),  int(end_Now[8:10]))
    interval_from_Now = end_wanted - startDate

    print("intervalDate      : ", intervalDate.days)
    print("interval_from_Now : ", interval_from_Now.days)
   
   
    return int(intervalDate.days) , int(interval_from_Now.days)  # count enddate - start date  ,  start Day for find last days


def fetch_DataF_O(strTicker, strStart_Date, strEnd_Date, strInterval) :

    """
        This Function make fetch data base online ask ,  from yahoo finance according to ticker, start and end date and timeframe(strinterval)
        output : if everything is normal is a data table
        output : if timeframe(strinterval) be incorrect is "-1"
    """
    
    checkin = False

    if str(type(strEnd_Date))  == "<class 'datetime.datetime'>" :
            #strEnd_Date = (str(datetime.now())[0:10])
            print("---------- > End_Date = datetime.now \n\n")

    print("\n\n\nStart_Date : " , strStart_Date, "\nEnd_Date   : ", strEnd_Date, "\n\n")
    intervalDate, interval_from_Now = (count_date_Diff(str(strStart_Date), strEnd_Date))


    if (strInterval == "1m") :
        
        if intervalDate < 31 and interval_from_Now < 8 :

            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")
            
            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            
        
        else:
        
            delta = interval_from_Now - 29
            print( " Delta : ", delta)
            print("start date :" , strStart_Date)
            strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
            print("\n -------------- > Forced new start date: ", strStart_Date)
            print(" -------------- >            end   date: ", strEnd_Date , "\n")
            intervalDate, interval_from_Now = (count_date_Diff(str(strStart_Date), strEnd_Date))
        

            if intervalDate > 8 :
                
                decide = "end"
                delta = intervalDate - 6
                

                if decide == "end" :

                    strStart_Date = str((datetime.strptime(str(strStart_Date), '%Y-%m-%d') + timedelta(days=delta)).date())

                    print("\nStart_Date        : ", strStart_Date)
                    print("End_Date          : ", strEnd_Date)
                    print("interval          : ", strInterval ,"\n\n")

                    data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
                    


    elif (strInterval == "2m") or (strInterval == "5m") or  (strInterval == "15m") or (strInterval == "30m") or (strInterval == "90m") :
        
        if interval_from_Now < 60 :
            
            print("\nStart_Date        : " , strStart_Date)
            print("End_Date          : "   , strEnd_Date)
            print("interval          : "   , strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            print(data)

        else:
        
            delta = interval_from_Now - 59
            strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())

            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            print(data)
            
            

    elif (strInterval == "60m") or (strInterval == "1h") :

        if interval_from_Now < 729 :
            
            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            

        else:
        
            delta = interval_from_Now - 729
            strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())

            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            
            

    elif (strInterval == "1d") or (strInterval == "5d")or (strInterval == "1wk")or (strInterval == "1mo")or (strInterval == "3mo"):
        
        
            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)

            
    else:
        
        checkin = True
    

    return data.reset_index() if checkin == False else (print("\n\n\n....> Fetch Data failed because ticker or interval are incorrect !\n\n\n\n"))


def interval_Online ( intMaxLen , strInterval) :

    """ this function calculate start and end date per intMaxLen (maximom period of rsi or ...) base strInterval (1m , 2m , ... )"""
    
    if strInterval == "1m" :
        
        cal = math.ceil(2*intMaxLen*1/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        print("strStart_Date : " , strStart_Date)
        strEnd_Date     =  datetime.now()
        

    
    if strInterval == "2m" :

        cal = math.ceil(2*intMaxLen*2/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        

    
    if strInterval == "5m" :
        
        cal = math.ceil(2*intMaxLen*5/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        

    
    if strInterval == "15m" :

        cal = math.ceil(2*intMaxLen*15/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        

    if strInterval == "30m" :

        cal = math.ceil(2*intMaxLen*30/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        
    
    if strInterval == "1h" :

        cal = math.ceil(2*intMaxLen*60/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        
        


    if strInterval == "90m" :

        cal = math.ceil(2*intMaxLen*90/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        


    if strInterval == "4h" :

        cal = math.ceil(2*intMaxLen*240/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        


    if strInterval == "1d" :

        cal = math.ceil(2*intMaxLen*1440/1440)
        print(cal, intMaxLen)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        


    

    if strInterval == "5d" :

        cal = math.ceil(2*intMaxLen*7200/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        
            
    if strInterval == "1wk" :

        cal = math.ceil(2*intMaxLen*10080/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        
    

    if strInterval == "1mo" :
        
        cal = math.ceil(2*intMaxLen*44640/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        


    if strInterval == "3mo" :
        
        cal = math.ceil(2*intMaxLen*133920/1440)
        strStart_Date = str((datetime.now() - timedelta(days = cal)).date())
        

    #start_date , end_date, cal =interval_Online(1440, "1m")
    #print("\nstart_date : ",start_date, "\nend_date   : ",end_date,  "\ncal        : ",cal )"""

    return (strStart_Date, cal)

        #print(data)


def updateData(intervalA, ticker, start_Date) :
        intervalA, ticker, 
        
        end_Date     =  str((datetime.now() + timedelta(days=1)).date())
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>/////   Date Time Now : ", end_Date)
        
        

        data_online = {}

        for i in intervalA :
                
                
                _checkEmpty = True
                errorCounter = 1
             

                try :
                     
                     data = fetch_DataF_O(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=i)         
                     data_online[i] = data
                     table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= i)
                     frame = data.to_sql(con= database_connection() , name=table_name , if_exists='replace')
                     
                     print("Try for fetch and push  in interval : " ,i , " ---------- > OK!\n")
              

                     
                except :
                        
                       print("\n>>>>>>>>>>>>>>>  May be internet connection is failed because download is failed !\n")
                       while _checkEmpty :
                                errorCounter +=1

                                print("\nErrorCounter :", errorCounter)

                                data = fetch_DataF_O(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=i)
                                
                                if data.empty:
                                       
                                        time.sleep(3)
                                        print( "\nData is Empty.I'm Tring again... ")
                                else:
                                         _checkEmpty= False
                                         data_online[i] = data
                                         table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= i)
                                         frame = data.to_sql(con= database_connection() , name=table_name , if_exists='replace')
                                         print("Data.Empty: ", data.empty)
                
                                         time.sleep(1)
  
        
                                

        return data_online




def data_processF (intervalA ,data_online : dict, ticker) :
    
    data_process_dict = {}

    for i in intervalA :
         
        
        table_name="{ticker}_{interval}_P".format(ticker= ticker.replace("-","") ,interval= i)
        mycursor = mydb.cursor()
        query = """
                create table IF NOT EXISTS {table_name}({Date} varchar(50));
                                                         
                
                                                        

                  
                """.format(table_name = table_name, Date = data_online[i].columns[0] )
        print("Query >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> : \n", query)
        #val = ["2024-01-01" , "254789"]
        mycursor.execute(query)
        mydb.commit()

        table_name="{ticker}_'P_'{interval}".format(ticker= ticker.replace("-","") ,interval= i)
        data_process_dict["sum"]  = [i, sum(data_online[i]["Open"])]
        data_process_dict["RSI"]  = [i, talib.RSI(data_online[i]["Open"])]
         
        print("-----------------------------------------------")
        

    #print(data_process_dict.keys())
    #print(data_process_dict)

    return data_process_dict

          