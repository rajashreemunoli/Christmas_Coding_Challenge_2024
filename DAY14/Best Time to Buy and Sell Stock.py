#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#Example 1:
#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#Example 2:
#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transactions are done and the max profit = 0.


def maxProfit(prices):
    buy=min(prices[1:])
        
    for i in range(1,len(prices)):
        if prices[i]==buy:
            buy_index=i
        else:
            i+=1
            
        sell=0
    for i in range(buy_index+1,len(prices)):
        if prices[i]>buy and prices[i]>prices[i-1]:
            sell=prices[i]
        else:
            i+=1
    if sell==0:
        return 0
    else:
        return sell-buy

if __name__ == "__main__":
    stock_prices = [7,1,5,3,6,4]
    print(f'Maximum profit possible is: {maxProfit(stock_prices)}')