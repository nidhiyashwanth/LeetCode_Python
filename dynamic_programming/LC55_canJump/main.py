# WARNING: THIS CODE DOESN'T PASS LEETCODE TEST CASES
# Because time complexity = O(n^2)

class Solution:
    def canJump(self, nums):
        dp_positions = [False] * len(nums)
        dp_positions[0] = True

        for j in range(1, len(nums)):
            for i in range(j):
                if dp_positions[i] and i + nums[i] >= j:
                    dp_positions[j] = True
        return dp_positions[-1]