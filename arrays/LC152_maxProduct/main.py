class Solution:
    def maxProduct(self, nums):
        max_till_idx = [nums[0]]
        min_till_idx = [nums[0]]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            max_till_idx.append(max(num, num * max_till_idx[i - 1], num * min_till_idx[i-1]))
            min_till_idx.append(min(num, num*max_till_idx[i-1], num * min_till_idx[i-1]))
            max_prod = max(max_prod, max_till_idx[i])
        return max_prod