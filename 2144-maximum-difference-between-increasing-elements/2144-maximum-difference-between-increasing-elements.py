class Solution:
    def maximumDifference(self, nums):
        # Step 1 : Initialization
        min_so_far = nums[0]  
        max_diff = -1

        # Step 2 : Apply Logic and Loop
        for i in range(1, len(nums)):  
            if nums[i] > min_so_far:
                max_diff = max(max_diff, nums[i] - min_so_far)
            else:
                min_so_far = nums[i]

        # Step 3 : Return the Result
        return max_diff  