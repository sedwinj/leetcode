# https://leetcode.com/problems/group-anagrams

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Approach: Place words in buckets according to a key shared by all anagrams of that word.
        """

        anagrams = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)

        return anagrams.values()
