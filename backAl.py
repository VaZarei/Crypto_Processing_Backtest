 
def B_rsi(df) :

        hisp={}
        
        
       
        for i in range (len(df)) : 
                hisp[i]=[]
                for j in range(i, 0 , -1) :
                                flagCorrectRSI = True
                                #print("\ni:", i, "j:",j)
                                

                                bRule1 = (i-j < 30)
                                bRule2 = df.iloc[i]['RSI']    <  35 
                                bRule3 = df.iloc[j]['RSI']    <  df.iloc[i]['RSI']
                                bRule4 = df.iloc[j]['Close']  >  df.iloc[i]['Close']
                                #bRule5 = flagCorrectRSI


                                if bRule1 and bRule2 and  bRule3 and bRule4  :
                                                        #print("I:", i, "J:",j)
                                                        for m in range (j, i, 1) :
                                                             #print("Im:", i, "Jm:",j , "m:", m)
                                                             
                                                             if df.iloc[m]['Close'] < df.iloc[i]['Close'] :
                                                                 flagCorrectRSI = False
                                                                 print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> break happend >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> df.iloc[m]['Close'] < df.iloc[i]['Close'] ")
                                                                 break
                                                                 
                                                             

                                                        if flagCorrectRSI :
                                                             hisp[i].append({"i" : i, "j": j,  "priceNow" : round(df.iloc[i]['Close'], 3), "rsiNow" : df.iloc[i]['RSI'], "priceFind" : round(df.iloc[j]['Close'], 3), "rsiFind" : df.iloc[j]['RSI']   })
                                                             print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> break happend >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> hisp[i].append")
                                                             break
        for i in range(len(hisp)) :
               
                if hisp[i]==[] :
                        hisp.pop(i)
                               
                                 
                                                
        return hisp
                                        
                                
                                
  

        
        
 