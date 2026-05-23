//You are given an array prices where prices[i] is the price of a given stock on the ith day.
//You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
//Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def buy_sell_profit(prices):
    mini = prices[0]
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < mini:
            mini = prices[i]
        profit = prices[i] - mini
        if profit > max_profit:
            max_profit = profit
    return max_profit

prices = list(map(int, input("Enter prices: ").split()))
print(buy_sell_profit(prices))
