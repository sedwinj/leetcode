# https://leetcode.com/problems/maximum-subarray


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Approach: Kadane's algorithm
        """

        current = -float("inf")
        best = -float("inf")

        for n in nums:
            current = max(current + n, n)
            best = max(best, current)

        return best
