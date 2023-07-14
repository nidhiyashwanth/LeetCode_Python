class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]  # Create a list to store the maximum sum subarray ending at each index
        result = nums[0]  # Initialize the result as the first element of the input list

        for i in range(1, len(nums)):  # Iterate through each element in the input list starting from the second element
            num = nums[i]  # Get the current number

            # Calculate the maximum sum subarray ending at the current index
            # Choose either the current number or the sum of the current number and the maximum sum subarray ending at the previous index
            dp.append(max(num, num + dp[i-1]))

            # Update the result by taking the maximum of the current maximum sum subarray and the previous result
            result = max(dp[i], result)

        return result  # Return the maximum sum subarray
