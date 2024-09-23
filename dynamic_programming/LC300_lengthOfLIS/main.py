class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp_sub_sequence = [1] * len(nums)
        max_so_far = 1
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp_sub_sequence[j] = max(dp_sub_sequence[i] + 1, dp_sub_sequence[j])
                max_so_far = max(max_so_far, dp_sub_sequence[j])
        return max_so_far