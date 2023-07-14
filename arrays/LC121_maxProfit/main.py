class Solution:
    def maxProfit(self, prices):
        if not prices:  # Check if the list is empty
            return 0
        
        max_profit = 0  # Initialize the maximum profit as 0
        cheapest_price = prices[0]  # Set the initial cheapest price as the first element in the list
        
        for price in prices:  # Iterate through each price in the list
            cheapest_price = min(price, cheapest_price)  # Update the cheapest price if a lower price is found
            cur_profit = price - cheapest_price  # Calculate the current profit by subtracting the cheapest price from the current price
            max_profit = max(cur_profit, max_profit)  # Update the maximum profit if the current profit is higher
            
        return max_profit  # Return the maximum profit