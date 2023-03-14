#def posDivRsi(dataFrame) :
"""
hisp={0:[""]}
for i in range(10):
    #print(i)
  
    hisp[i].append(i)
   
    for j in range(i) :
        #hisp={i:[""]}
        #hisp={i:list(hisp.values())}
        #hisp[i].append(j)
        pass
   
print(hisp)
"""

"""
hisp={"m":[]}
for i in range(10):
    hisp["m"].append(i)
print(hisp)

"""
"""
hisp={"m":[]}
hisp["m"].append(5)
print(hisp)

"""
"""
t={1: []}
t[1].append(23)
t[1].append(23)
print(t)
"""

#a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a[0]=5
#print(a)

"""

for i in range(10) :
     t[i]=[]
     for j in range(10) :
          
          [i].append(j)

          if i>j :
            print(i,j)
            t[i].append({"price": 11.5})



for i in range(len(t)) :
                print(i)
                if t[i]==[] :
                        t.pop(i)
print("print : \n", t)     

"""
"""

for i in range (len(df)) : 
                hisp[i]=[]
                for j in range(i) :
                                j=i-j
                                
                                
                                if df.iloc[j]['RSI'] < df.iloc[i]['RSI']:
                                        
                                        if df.iloc[j]['Close'] > df.iloc[i]['Close']:
                                                #print("df.iloc[j]['RSI'] < df.iloc[i]['RSI']" , df.iloc[j]['RSI'],"<" , df.iloc[i]['RSI'])
                                                #print("df.iloc[j]['Close'] > df.iloc[i]['Close']", df.iloc[j]['Close'],">" , df.iloc[i]['Close'])
                                                
                                                hisp[i].append({"priceNow" : df.iloc[i]['Close'], "rsiNow" : df.iloc[i]['RSI'], "priceFind" : df.iloc[j]['Close'], "rsiFind" : df.iloc[j]['RSI']   })
                                                 
                                                

                                        
                                
                                
  

        
        
        #print("print : \n", hisp)
        for i in range(len(hisp)) :
                print(i)
                if hisp[i]==[] :
                        hisp.pop(i)
        print("print : \n", hisp)
"""

hisp = {42: [{'i': 42, 'j': 38, 'priceNow': 0.36, 'rsiNow': 36.83, 'priceFind': 0.36, 'rsiFind': 35.28}], 43: [{'i': 43, 'j': 37, 'priceNow': 0.39, 'rsiNow': 57.05, 'priceFind': 0.39, 'rsiFind': 55.06}, {'i': 43, 'j': 34, 'priceNow': 0.39, 'rsiNow': 57.05, 'priceFind': 0.39, 'rsiFind': 56.23}], 56: [{'i': 56, 'j': 53, 'priceNow': 0.36, 'rsiNow': 36.5, 'priceFind': 0.37, 'rsiFind': 34.09}], 58: [{'i': 58, 'j': 56, 'priceNow': 0.36, 'rsiNow': 38.26, 'priceFind': 0.36, 'rsiFind': 36.5}, {'i': 58, 'j': 54, 'priceNow': 0.36, 'rsiNow': 38.26, 'priceFind': 0.36, 'rsiFind': 32.42}, {'i': 58, 'j': 53, 'priceNow': 0.36, 'rsiNow': 38.26, 'priceFind': 0.37, 'rsiFind': 34.09}, {'i': 58, 'j': 38, 'priceNow': 0.36, 'rsiNow': 38.26, 'priceFind': 0.36, 'rsiFind': 35.28}], 59: [{'i': 59, 'j': 57, 'priceNow': 0.35, 'rsiNow': 32.27, 'priceFind': 0.35, 'rsiFind': 29.53}], 67: [{'i': 67, 'j': 65, 'priceNow': 0.32, 'rsiNow': 24.22, 'priceFind': 0.32, 'rsiFind': 17.1}, {'i': 67, 'j': 64, 'priceNow': 0.32, 'rsiNow': 24.22, 'priceFind': 0.33, 'rsiFind': 22.94}, {'i': 67, 'j': 63, 'priceNow': 0.32, 'rsiNow': 24.22, 'priceFind': 0.33, 'rsiFind': 23.11}], 68: [{'i': 68, 'j': 66, 'priceNow': 0.31, 'rsiNow': 20.38, 'priceFind': 0.31, 'rsiFind': 14.47}, {'i': 68, 'j': 65, 'priceNow': 0.31, 'rsiNow': 20.38, 'priceFind': 0.32, 'rsiFind': 17.1}], 69: [{'i': 69, 'j': 62, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.34, 'rsiFind': 26.36}, {'i': 69, 'j': 61, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.34, 'rsiFind': 25.5}, {'i': 69, 'j': 60, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.34, 'rsiFind': 28.44}, {'i': 69, 'j': 59, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.35, 'rsiFind': 32.27}, {'i': 69, 'j': 58, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.36, 'rsiFind': 38.26}, {'i': 69, 'j': 57, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.35, 'rsiFind': 29.53}, {'i': 69, 'j': 56, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.36, 'rsiFind': 36.5}, {'i': 69, 'j': 55, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.37, 'rsiFind': 39.09}, {'i': 69, 'j': 54, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.36, 'rsiFind': 32.42}, {'i': 69, 'j': 53, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.37, 'rsiFind': 34.09}, {'i': 69, 'j': 52, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.38, 'rsiFind': 43.71}, {'i': 69, 'j': 51, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.39, 'rsiFind': 47.67}, {'i': 69, 'j': 42, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.36, 'rsiFind': 36.83}, {'i': 69, 'j': 41, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.36, 'rsiFind': 39.61}, {'i': 69, 'j': 40, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.37, 'rsiFind': 42.51}, {'i': 69, 'j': 39, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.36, 'rsiFind': 33.54}, {'i': 69, 'j': 38, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.36, 'rsiFind': 35.28}, {'i': 69, 'j': 35, 'priceNow': 0.33, 'rsiNow': 48.9, 'priceFind': 0.38, 'rsiFind': 47.2}], 70: [{'i': 70, 'j': 59, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.35, 'rsiFind': 32.27}, {'i': 70, 'j': 58, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.36, 'rsiFind': 38.26}, {'i': 70, 'j': 57, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.35, 'rsiFind': 29.53}, {'i': 70, 'j': 56, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.36, 'rsiFind': 36.5}, {'i': 70, 'j': 55, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.37, 'rsiFind': 39.09}, {'i': 70, 'j': 54, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.36, 'rsiFind': 32.42}, {'i': 70, 'j': 53, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.37, 'rsiFind': 34.09}, {'i': 70, 'j': 52, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.38, 'rsiFind': 43.71}, {'i': 70, 'j': 51, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.39, 'rsiFind': 47.67}, {'i': 70, 'j': 50, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.39, 'rsiFind': 49.97}, {'i': 70, 'j': 49, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.4, 'rsiFind': 57.89}, {'i': 70, 'j': 48, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.4, 'rsiFind': 55.87}, {'i': 70, 'j': 45, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.39, 'rsiFind': 52.36}, {'i': 70, 'j': 43, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.39, 'rsiFind': 57.05}, {'i': 70, 'j': 42, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.36, 'rsiFind': 36.83}, {'i': 70, 'j': 41, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.36, 'rsiFind': 39.61}, {'i': 70, 'j': 40, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.37, 'rsiFind': 42.51}, {'i': 70, 'j': 39, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.36, 'rsiFind': 33.54}, {'i': 70, 'j': 38, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.36, 'rsiFind': 35.28}, {'i': 70, 'j': 37, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.39, 'rsiFind': 55.06}, {'i': 70, 'j': 35, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.38, 'rsiFind': 47.2}, {'i': 70, 'j': 34, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.39, 'rsiFind': 56.23}, {'i': 70, 'j': 28, 'priceNow': 0.34, 'rsiNow': 58.3, 'priceFind': 0.37, 'rsiFind': 52.63}]}
#hisp = {'i': 42, 'j': 38, 'priceNow': 0.35962700843811035, 'rsiNow': 36.83, 'priceFind': 0.36253100633621216, 'rsiFind': 35.28}

#print("hisp: \n\n", hisp)

for i in hisp :
    
    #print("\n", hisp[i][0])
    print(hisp[70])


#print(hisp[42])