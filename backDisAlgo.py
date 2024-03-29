import numpy as np
import pandas as pd
from Fetch_YF_Functons import fetch_Data_backtest
from configVar import main_Var







          

def bRsiF(i, df):
   
        """ is i : row in df : dataframe buyspot in positive RSi ?? , this function check it"""
  
        bRule_P_rsi_1 = df.iloc[i-2]['RSI']   >  df.iloc[i-1]['RSI']
        bRule_P_rsi_2 = df.iloc[i-1]['RSI']   <  df.iloc[i]['RSI']
        bRule_P_rsi_3 = (df.iloc[i-1]['RSI']  >  20)   and (df.iloc[i-1]['RSI']  <  60)                 and               (df.iloc[i]['RSI'] < 40)
        
        if   bRule_P_rsi_1 and bRule_P_rsi_2 and bRule_P_rsi_3 :

                
                for m in range(i-1, 0, -1):
                        print(f'i: {i-1}, m: {m}')
                        bRule_P_rsi_0 = (i-m > 30)
                        #print(f'i: {i}, m: {m}')
                        if bRule_P_rsi_0 :
                                return False
                        
                        bRule_P_rsi_4 = df.iloc[m-1]['RSI']   >  df.iloc[m]['RSI']
                        bRule_P_rsi_5 = df.iloc[m]['RSI']     <  df.iloc[m+1]['RSI']

                        bRule_P_rsi_6 = (i-m > 30) 
                        
                        bRule_P_rsi_7 = round(df.iloc[m]['RSI'] ,1)     <  round(df.iloc[i-1]['RSI'], 1)
                        bRule_P_rsi_8 = df.iloc[m]['Close']   >  df.iloc[i-1]['Close']


                        if bRule_P_rsi_4 and bRule_P_rsi_5 and bRule_P_rsi_5 and bRule_P_rsi_7 and bRule_P_rsi_8:

                                for r in range(i-1, m, -1):
                                        if df.iloc[r]['Close'] < df.iloc[i-1]['Close'] and df.iloc[r]['RSI'] < df.iloc[i-1]['RSI'] :
                                                print("FAlse : =========================================================================== ")
                                                return False

                                print("Yessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
                                return True
                                
        else :
                return False
        


def distanceF(ser1, ser2, df) :
        
        ser3 = ser1.copy()
        for t in range(len(ser1)):
                        ser3.iloc[t] = 'nan'
                        if not(np.isnan(ser2.iloc[t])) :


                                percent = (ser1.iloc[t] - ser2.iloc[t])/ser1.iloc[t] * 100
                                ser3.iloc[t] = float(round(percent, 3))
        return  ser3
                                
              


def traDisF(df) :

        buyflag  = True
        sellFlag = True
        buyExeFlag = False
        sellExeFlag = False
        costSnap = []
        lastTransAction = ""
        buyCounter   = 0
        sellCounter  = 0
        tradeCounter = 0

        dict_Detail_Data = data_backtest_dict = fetch_Data_backtest(strTicker=main_Var['s_ticker'], strStart_Date=main_Var['start_Date'], strEnd_Date=main_Var['end_Date'], Interval = main_Var['dfd_interval'])
        
        
        dfd= dict_Detail_Data[main_Var['dfd_interval'][0]][0]
        # print(dfd.head(10))

        # print(type(dfd1), dfd1)

        for i in range(len(df)) :
                
                snapClosePrice = df['Close'][i]
                
                
                #bRule0 = bRsiF(i, df)
                #bRule1 = float(df['dSMA'][i]) < -8.0
                bRule4 = df['RSI'][i-1]   < 30
                bRule5 = df['RSI'][i-2] > df['RSI'][i-1] and df['RSI'][i-1] < df['RSI'][i]
                #bRule3 = df['SMA'][i]   > df['SMA'][i-1]
                #bRule6 = float(df['dSMA'][i])  > -20.0
                
                bRule7 = df['RSI'][i-1] < df['rsiSMA'][i-1]
                bRule8 = df['RSI'][i] > df['rsiSMA'][i]


                if (buyflag or buyExeFlag) and (bRule4 and bRule5) :

                        buyExeFlag = True


                if buyExeFlag :

                        biRule0 =  df['RSI'][i]> 30 # and df['SMA'][i] < df['Close'][i] and df['SMA'][i-1]<df['SMA'][i]
                        #biRule1 =  float(df['dSMA'][i]) < -3.0

                        if biRule0  :


                                df['transAction'][i]   = "Buy"
                                df['PriceAction'][i]   = df['Close'][i]
                                buyPrice               = df['Close'][i]
                                lastTransAction        = "Buy"
                                

                                buyCounter   +=1
                                tradeCounter +=1
                                buyflag  = False
                                sellFlag = True
                                buyExeFlag = False
                                                
                                
## for Sell ------------------------------------------------------------------------------------------------------------
        
                
                if lastTransAction == "Buy" :

                        startDatetime = df.index[i]
                        if i != len(df)-1 :
                                endDatetime   = df.index[i+1]

                        dfd_Close_Check = round(dfd.loc[startDatetime:endDatetime]['Close'],3)
                       

                        for d in range(len(dfd_Close_Check)) :
                                dfdSnapClosePrice = dfd_Close_Check[d]
                                
                                

                                costSnap.append(round(((dfdSnapClosePrice - buyPrice) / (dfdSnapClosePrice) *(100)) , 4))


                                # sRule1  = (max(costSnap) > 7.0)  and  ((max(costSnap)-costSnap[-1]) > 1.5)
                                # sRule2  = True if (costSnap[-1] > 0 and  ((max(costSnap)-costSnap[-1]) > 3.5)) else False

                                sRule4  = (costSnap[-1]) < -5.0
                                
                                # sRule5  = df['Close'][i] > df['SMA_2'][i] and df['SMA_2'][i-1] < df['SMA_2'][i]
                                # sRule6  = ( df['SMA_2'][i-2] > df['SMA_2'][i-1] and df['SMA_2'][i-1] > df['SMA_2'][i]  )
                                # sRule7  = df['RSI'][i] > 70
                                # sRule8  = df['SMA_1'][i-1] > df['SMA_1'][i]

                                sRule9  = df['SMA_2'][i-1] < dfd_Close_Check[d-1]
                                sRule10 = df['SMA_2'][i-2] > df['SMA_2'][i-1] > df['SMA_2'][i]
                                sRule11 = df['SMA_2'][i]   > dfd_Close_Check[d]
                                sRule12 = df['SMA_1'][i]   > df['Close'][i]                   #dfd_Close_Check[d]
                                sRule13 = df['RSI'][i] > 30

                                # sRule111 = df['SMA_2'][i]  > dfd['Close'][d]
                                # sRule122 = df['SMA_1'][i]  > dfd['Close'][d]


                                if (sellExeFlag)  or  (sellFlag and (sRule4 or sRule9) and sRule13)  :

                                        sellExeFlag = True

                                        if sellExeFlag and (sRule4 or (sRule10 and sRule11 and sRule12) )   :

                                                if df['RSI'][i] < 32 : 
                                                        sellExeFlag = False
                                                        continue


                                                df['transAction'][i]   = "Sell"
                                                df['PriceAction'][i]   = df['Close'][i]
                                                lastTransAction        = "Sell"

                                                
                                                sellCounter  +=1
                                                tradeCounter +=1
                                                buyflag  = True
                                                sellFlag = False
                                                sellExeFlag = False
                                                costSnap = []

        return buyCounter, sellCounter, tradeCounter

 #----------------------------------------------------------------------------------------------------------------------------------------------------        



def costF(df, intMoney, floatFee) :

        money = intMoney
        quantity = 0
        lastTransAction = ''

        for i in range(len(df)) :
            
            
            snapClosePrice = df['Close'][i]

            if quantity > 0 :
                    
                    df['FinallyCostBenefit'][i] = round(((intMoney - (money + quantity * snapClosePrice * (1-floatFee))) ) / intMoney * (-100) , 3)
                    
                   
            
            

            if (df['transAction'][i] == "Buy") :

                lastTransAction  = "Buy"
                closePrice = df['PriceAction'][i]
                quantity = money // closePrice
                money = money - quantity *  closePrice * (1-floatFee)


                df['Money'][i]    = money
                df['Quantity'][i] = quantity
                

           
            if lastTransAction == 'Buy' :

                df['snapCost'][i]    = round(((snapClosePrice - closePrice) / (snapClosePrice) *(100)) , 3) 

            if (df['transAction'][i] == "Sell"):

                lastTransAction  = "Sell"
                closePrice = df['PriceAction'][i]
                
                money = money + quantity *  closePrice * (1-floatFee)
                quantity = 0

                df['Money'][i]       = money
                df['Quantity'][i]    = quantity


            

               

                

        


   