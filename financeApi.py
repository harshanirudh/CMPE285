import yfinance as yf
import datetime

def printCurrentDateAndTime():
    dateTS = datetime.datetime.now()
    dtsString = dateTS.strftime("%c")
    print(dtsString)
    print()

def printStockName(stock,symbol):
        #print name of stock along with symbol
        print(stock.info['longName'],"(",symbol,")")
        print()
def valueChange(stock):
    curr_st_pr = stock.info['currentPrice']
    prev_st_pr = stock.info['previousClose']
    print("Current stock price $",curr_st_pr)
    priceDiff = curr_st_pr - prev_st_pr
    precentDiff = (abs(priceDiff)/prev_st_pr)*100
    print()
    if(priceDiff > 0):
        print("Value Change in stock price")
        print()
        print("Price Increased by","+",priceDiff,"(+",precentDiff,"%)")
        
    else:
        print("Value Change in stock price")
        print()
        print("Price Decresed by","-",abs(priceDiff),"(-",precentDiff,"%)")

while(1):
    #take symbol as input
    print("Please enter a Stock symbol:")
    print()
    stock_symbol = input()
    print()

    #Get result from API and do exception handling for no network
    try:
        stock = yf.Ticker(stock_symbol)
    except ConnectionError as e:
        print("Caught and exception ,Connection error", e)
        break

    #Print current date and time
    printCurrentDateAndTime()
    if(stock.info['regularMarketPrice'] is None):
        # Print invalid if symbol is not present
        print("Invalid symbol")
    else:
        printStockName(stock,stock_symbol)
        valueChange(stock)
    print("-----------------------------------------------------------------------------------------------------------------")
    print()
    print()
