class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        max_loot_atN = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            max_loot_atN.append(max(nums[i] + max_loot_atN[i-2], max_loot_atN[i-1]))
        return max_loot_atN.pop()