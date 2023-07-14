# Non-Dynamic Programming Approach
class Solution:
    def canJump(self, nums):
        max_reach = 0
        for current_step in range(len(nums)):
            if current_step > max_reach:
                return False

            current_reach = current_step + nums[current_step]
            max_reach = max(max_reach, current_reach)
        return True