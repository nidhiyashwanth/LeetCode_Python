class NumArray:

    def __init__(self, nums):
        self.acc_sum_cache = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            num = nums[i]
            self.acc_sum_cache[i + 1] += self.acc_sum_cache[i] + num

    def sumRange(self, i, j):
        return self.acc_sum_cache[j + 1] - self.acc_sum_cache[i]