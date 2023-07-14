class Solution:
    def twoSum(self, nums, target):
        nums_visited = {}  # Create an empty dictionary to store visited numbers and their indices
        
        for i in range(len(nums)):  # Iterate through each number in the list
            num = nums[i]  # Get the current number
            complement = target - num  # Calculate the complement needed to reach the target
            
            if complement in nums_visited:  # Check if the complement is already visited
                return [i, nums_visited[complement]]  # Return the indices of the current number and its complement
            else:
                nums_visited[num] = i  # Store the current number and its index in the dictionary
        
        # If no solution is found, an empty list can be returned or an exception can be raised
        # In the given code, there is no explicit handling for the case when no solution is found
        
        # If no solution is found, you can add the following line to return an empty list
        # return []
        
        # Alternatively, you can raise an exception to indicate no solution is found
        # raise ValueError("No two numbers in the list add up to the target")