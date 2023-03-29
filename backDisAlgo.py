import numpy as np

def distanceF(ser1, ser2, df) :
        
        ser3 = df['Close - sma']
        for t in range(len(ser1)):
                        
                        if not(np.isnan(ser2.iloc[t])) :


                                percent = (ser1.iloc[t] - ser2.iloc[t])/ser1.iloc[t] * 100
                                ser3.iloc[t] = round(percent, 3)
                                
                        

        pass


def traDisF(df) :

        buyflag  = True
        sellFlag = True

        for i in range(len(df)) :
                
                
                
                bRule1 = float(df['Close - sma'][i]) < -2.2





                if buyflag and bRule1 :

                        df['transAction'][i] = "Buy"
                        df['PriceAction'][i]   = df['Close'][i]

                        buyflag  = False
                        sellFlag = True
                        
                       

        
                sRule1 = float(df['Close - sma'][i]) > 2.2




                if sellFlag and sRule1 :

                        df['transAction'][i] = "Sell"
                        df['PriceAction'][i]   = df['Close'][i]

                        buyflag  = True
                        sellFlag = False



        pass
