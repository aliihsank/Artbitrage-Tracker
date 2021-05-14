# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:03:27 2021

@author: ali_k
"""

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, requests

graph_limit = 10

# Create figure for plotting
fig, axs = plt.subplots(2, 2)

arrx = []

arrbtc = []

arrada = []

arreth = []

arratom = []

arrtrx = []

uri1 = "https://api.btcturk.com/api/v2/ticker?pairSymbol="
uri2 = "https://api.binance.com/api/v3/ticker/price?symbol="

# SNX MATIC BAT

def animate(i, arrx, arrbtc, arrtrx, arrada, arreth):

    #Read data
    print('===BTC===')
    result1 = requests.get(url=uri1 + 'BTC_TRY').json()["data"][0]["last"]
    
    result2 = float(requests.get(url=uri2 + 'BTCTRY').json()["price"])

    print('BTC: ', result1)
    print('BNN: ', result2)
    
    diff = (100 * abs(result1 - result2) / min(result1, result2))
    arrbtc.append(diff)
    
    print('Diff: ', diff)
    
    print('===TRX===')
    result1 = requests.get(url=uri1 + 'TRX_TRY').json()["data"][0]["last"]
    
    result2 = float(requests.get(url=uri2 + 'TRXTRY').json()["price"])

    print('BTC: ', result1)
    print('BNN: ', result2)
    
    diff = (100 * abs(result1 - result2) / min(result1, result2))
    arrtrx.append(diff)
    
    print('Diff: ', diff)
    
    print('===ADA===')
    result1 = requests.get(url=uri1 + 'ADA_TRY').json()["data"][0]["last"]
    
    result2 = float(requests.get(url=uri2 + 'ADATRY').json()["price"])

    print('BTC: ', result1)
    print('BNN: ', result2)
    
    diff = (100 * abs(result1 - result2) / min(result1, result2))
    arrada.append(diff)
    
    print('Diff: ', diff)

    
    print('===ETH===')
    result1 = requests.get(url=uri1 + 'ETH_TRY').json()["data"][0]["last"]
    
    result2 = float(requests.get(url=uri2 + 'ETHTRY').json()["price"])

    print('BTC: ', result1)
    print('BNN: ', result2)
    
    diff = (100 * abs(result1 - result2) / min(result1, result2))
    arreth.append(diff)
    
    print('Diff: ', diff)
    

    # Add x and y to lists
    arrx.append(dt.datetime.now().strftime('%H:%M:%S'))

    # Limit x and y lists to 20 items
    arrx = arrx[-graph_limit:]
    arrbtc = arrbtc[-graph_limit:]
    arrtrx = arrtrx[-graph_limit:]
    arrada = arrada[-graph_limit:]
    arreth = arreth[-graph_limit:]

    # Draw x and y lists
    axs[0, 0].clear()
    axs[0, 0].plot(arrx, arrbtc)
    axs[0, 0].set_title('BTC')
    axs[0, 1].clear()
    axs[0, 1].plot(arrx, arrtrx)
    axs[0, 1].set_title('TRX')
    axs[1, 0].clear()
    axs[1, 0].plot(arrx, arrada)
    axs[1, 0].set_title('ADA')
    axs[1, 1].clear()
    axs[1, 1].plot(arrx, arreth)
    axs[1, 1].set_title('ETH')
    
    plt.setp(axs[0, 0].get_xticklabels(), rotation=45)
    plt.setp(axs[0, 1].get_xticklabels(), rotation=45)
    plt.setp(axs[1, 0].get_xticklabels(), rotation=45)
    plt.setp(axs[1, 1].get_xticklabels(), rotation=45)
    
    time.sleep(1)

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(arrx, arrbtc, arrtrx, arrada, arreth), interval=1000)
plt.show()