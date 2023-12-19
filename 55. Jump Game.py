# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Approach: List scanning. O(n) time
        """

        idx = 0
        max_idx = 0
        for idx, jump in enumerate(nums):
            if idx > max_idx or max_idx >= len(nums) - 1:
                break

            cur_max = idx + jump
            max_idx = max(max_idx, cur_max)

        return max_idx >= len(nums) - 1
