class Solution:
    def twoSum(self, nums, target):
        num_indices = {}  # Dictionary to store indices of numbers

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i