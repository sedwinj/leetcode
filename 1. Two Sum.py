# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Approach: Scan with caching. Check to see if target - nums[i] has been encountered. 
        """

        encountered = {}
        for idx, num in enumerate(nums):
            complement = target - num

            if complement in encountered:
                return [encountered[complement], idx]

            encountered[num] = idx
