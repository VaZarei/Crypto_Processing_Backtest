import numpy as np

def distanceF(ser1, ser2, df) :
        
        ser3 = df['Close - sma']
        for t in range(len(ser1)):
                        
                        if not(np.isnan(ser2.iloc[t])) :


                                percent = (ser1.iloc[t] - ser2.iloc[t])/ser1.iloc[t] * 100
                                ser3.iloc[t] = round(percent, 3)
                                
                        

        pass

                  