from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Compute the gain (delta) for each num if we apply XOR with k
        deltas = [(num ^ k) - num for num in nums]
        
        total = sum(nums)
        gains = [d for d in deltas if d >= 0]
        
        # If the number of positive gains is even, we can use all of them
        if len(gains) % 2 == 0:
            return total + sum(gains)
        
        # Otherwise, we must exclude one gain (min positive or swap with max negative)
        min_gain = min(gains)
        max_loss = max((d for d in deltas if d < 0), default=float('-inf'))

        return total + sum(gains) + max(max_loss, -min_gain)
        