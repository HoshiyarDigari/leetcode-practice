class Solution:
    def maxProfit(prices: list[int], fee: int) -> int:
        """
        Algo:
        We have a list of prices of stock on different days. 
        We can either have a stock on any given day or we don't own a stock on that day.
        If we don't have a stock, it could be due to either
            - we sold the stock on that day. Our profit will be profit on previous day + price[i]-fee
            - we had no stock the previous day and we didn't do anything. our profit will be same as the previous day
            - we take the max of these two
        If we have a stock on the day, it could be due to either
            - we bought a stock on this day. Our profit is profit previous day + price(i) 
            - we had a stock on previous day and we did nothing, profit today is same as yesterday.
            - we take max of these two
        On the last day, we shouldn't have any stock. so the max of this situation will be our maxProfit
        """
        #lists to keep track of the states
        profit_holding_stock = [-prices[0]] * len(prices)
        profit_not_holding_stock = [0] * len(prices)
        for day, stock_price in enumerate(prices):
            if day !=0:
                profit_holding_stock[day] = max(profit_not_holding_stock[day-1]-stock_price, profit_holding_stock[day-1])
                profit_not_holding_stock[day] = max(profit_not_holding_stock[day-1], profit_holding_stock[day-1]+ stock_price -fee)
                print('holding', profit_holding_stock)
                print('not holding', profit_not_holding_stock)






assert Solution.maxProfit([1,3,2,8,4,9],0) == 8
