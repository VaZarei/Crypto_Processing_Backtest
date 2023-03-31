import numpy as np
import pandas as pd


def distanceF(ser1, ser2, df) :
        
        ser3 = ser1.copy()
        for t in range(len(ser1)):
                        ser3.iloc[t] = 'nan'
                        if not(np.isnan(ser2.iloc[t])) :


                                percent = (ser1.iloc[t] - ser2.iloc[t])/ser1.iloc[t] * 100
                                ser3.iloc[t] = round(percent, 3)
        return  ser3
                                
                        



def traDisF(df) :

        buyflag  = True
        sellFlag = True
        costSnap = []
        lastTransAction = ""

        for i in range(len(df)) :
                
                snapClosePrice = df['Close'][i]
                
                
                
                bRule1 = float(df['dEMA'][i]) < -3.0
                bRule2 = df['RSI'][i] < 35
                bRule3 = df['Close'][i] > df['Close'][i-1]





                if buyflag and bRule1 and bRule2 and bRule3 :

                        df['transAction'][i]   = "Buy"
                        df['PriceAction'][i]   = df['Close'][i]
                        buyPrice               = df['Close'][i]
                        lastTransAction        = "Buy"

                        buyflag  = False
                        sellFlag = True
                        
                       
## for Sell ------------------------------------------------------------------------------------------------------------
        
                
                if lastTransAction == "Buy" :

                        costSnap.append(round(((snapClosePrice - buyPrice) / (snapClosePrice) *(100)) , 3))
                        
                        sRule1 = (max(costSnap) > 4.0)  and  ((max(costSnap)-costSnap[-1]) > 1.5)
                        sRule2 = ((max(costSnap)-costSnap[-1]) > 3.0)
                        sRule3 =  df['RSI'][i] > 35

                        sRule4 = float(df['dEMA'][i]) > 3.0




                        if sellFlag and sRule3 and (sRule1 or sRule2) :
                                
                                print("max(costSnap) :", max(costSnap))
                                print("costSnap[-1] :", costSnap[-1])
                                print("costSnap : ", costSnap)
                                df['transAction'][i]   = "Sell"
                                df['PriceAction'][i]   = df['Close'][i]
                                lastTransAction = "Sell"

                                buyflag  = True
                                sellFlag = False
                                costSnap = []



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
                money = money - quantity *  closePrice


                df['Money'][i]    = money
                df['Quantity'][i] = quantity
                

           
            if lastTransAction == 'Buy' :

                df['snapCost'][i]    = round(((snapClosePrice - closePrice) / (snapClosePrice) *(100)) , 3) 

            if (df['transAction'][i] == "Sell"):

                lastTransAction  = "Sell"
                closePrice = df['PriceAction'][i]
                
                money = money + quantity *  closePrice
                quantity = 0

                df['Money'][i]       = money
                df['Quantity'][i]    = quantity


            

               

                

        


   