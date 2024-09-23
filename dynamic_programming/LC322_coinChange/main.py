class Solution:
    def coinChange(self, coins, amount):
        dp_min_coins = [float('inf')] * (amount + 1)  # Create a list to store the minimum number of coins needed for each amount
        dp_min_coins[0] = 0  # Set the minimum number of coins needed for the amount of 0 to be 0

        for i in range(1, len(dp_min_coins)):
            amount = i  # Set the current amount
            for coin_value in coins:  # Iterate through each coin value
                if coin_value <= amount:  # Check if the coin value is less than or equal to the current amount
                    dp_min_coins[i] = min(dp_min_coins[i], dp_min_coins[amount - coin_value] + 1)  # Update the minimum number of coins needed for the current amount

        answer = dp_min_coins[-1]  # Get the minimum number of coins needed for the target amount

        if answer == float("inf"):  # If the answer is infinity, it means it's not possible to make the target amount
            return -1
        else:
            return answer  # Return the minimum number of coins needed