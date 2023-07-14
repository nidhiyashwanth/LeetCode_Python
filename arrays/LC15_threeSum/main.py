class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1

            if i>0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left +1]:
                        left +=1
                    left +=1
                    right -=1
                elif nums[left] + nums[right] < target:
                    left +=1
                else:
                    right -= 1
        return res
