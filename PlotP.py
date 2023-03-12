import matplotlib.pyplot as plt
import numpy as np

def plot_RSI(df, window):
    diff = df.Close.diff(periods=1).values
    xdate = [x.date() for x in df.Datetime]
    RSI = []
    for i in range(window+1, len(xdate)):
        neg = 0
        pos = 0
        for value in diff[i-window:i+1]:
            if value > 0:
                pos += value # accumulate positive diff
            if value < 0:
                neg += value # accumulate negative diff
        pos_ave = pos/window # average price of positive diff
        neg_ave = np.abs(neg/window) # average absolute price of negative diff
        rsi = pos_ave/(pos_ave+neg_ave)*100
        RSI.append(rsi)

    # draw RSI figure
    plt.plot(xdate[window+1:], RSI, label = "RSI {}".format(window), lw=2.5, alpha=0.6)
    plt.xlim(xdate[window+1], xdate[-1])
    plt.ylim(0,100)
    plt.legend()

def RSI(df, windows):
    xdate = [x.date() for x in df.index]
    plt.figure(figsize=(15, 10))
    
    # plot the original closing line
    plt.subplot(211)
    plt.plot(xdate, df.Close, label="close")
    plt.xlim(xdate[0], xdate[-1])
    plt.legend()
    plt.grid()
    
    # plot RSI
    plt.subplot(212)
    plt.grid()
    plt.title("RSI")
    for window in windows:
        plot_RSI(df, window)

    # fill area above 70 and below 30
    plt.fill_between(xdate, np.ones(len(xdate))*30, color="blue", alpha=0.1)
    plt.fill_between(xdate, np.ones(len(xdate))*70, np.ones(len(xdate))*100, color="red", alpha=0.1)
    
    # draw dotted lines at 70 and 30
    plt.plot(xdate, np.ones(len(xdate))*30, color="blue", linestyle="dotted")
    plt.plot(xdate, np.ones(len(xdate))*70, color="red", linestyle="dotted")
    plt.show()






