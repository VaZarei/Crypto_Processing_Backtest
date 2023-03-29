import numpy as np

def distanceF(ser1, ser2, df) :
        
        ser3 = df['Close - sma']
        for t in range(len(ser1)):
                        
                        if not(np.isnan(ser2.iloc[t])) :


                                percent = (ser1.iloc[t] - ser2.iloc[t])/ser1.iloc[t] * 100
                                ser3.iloc[t] = round(percent, 3)
                                
                        



def traDisF(df) :

        buyflag  = True
        sellFlag = True

        for i in range(len(df)) :
                
                
                
                bRule1 = float(df['Close - sma'][i]) < -2.5
                bRule2 = df['RSI'][i] < 35





                if buyflag and bRule1 and bRule2 :

                        df['transAction'][i] = "Buy"
                        df['PriceAction'][i]   = df['Close'][i]

                        buyflag  = False
                        sellFlag = True
                        
                       

        
                sRule1 = float(df['Close - sma'][i]) > 2.5




                if sellFlag and sRule1 :

                        df['transAction'][i] = "Sell"
                        df['PriceAction'][i]   = df['Close'][i]

                        buyflag  = True
                        sellFlag = False



        pass #26.63



def costF(df, intMoney, floatFee) :

        money = intMoney
        quantity = 0

        for i in range(len(df)) :
            
            

            if quantity > 0 :
                    snapClosePrice = df['Close'][i]
                    df['CostBenefit'][i] = round((money + quantity*snapClosePrice*(1-floatFee) / intMoney * (100))-100 , 2)
                    
                   
            
            

            if (df['transAction'][i] == "Buy") :
                
                closePrice = df['PriceAction'][i]
                quantity = money // closePrice
                money = money - quantity *  closePrice


                df['Money'][i]    = money
                df['Quantity'][i] = quantity





            if (df['transAction'][i] == "Sell"):

                closePrice = df['PriceAction'][i]
                
                money = money + quantity *  closePrice
                quantity = 0

                df['Money'][i]       = money
                df['Quantity'][i]    = quantity

                df['CostBenefit'][i] = round((money - intMoney) / intMoney*(1-floatFee) * (100) , 2)

                

        


   