// https://leetcode.com/problems/longest-palindromic-substring

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    /*
     * Approach: Try building a palindrome from every character
     * in the input, treating it as the center. Identical
     * consecutive characters in the center are squashed.
     * O(n^2) time. O(1) space.
     */

    if (s.length == 1) {
        return s
    }

    let longest = []
    for (let idx = 0; idx < s.length; idx++) {
        let start = idx // The first index in this palindrome
        let end = start // The last index in this palindrome
        // Squash identical consecutive centers.
        for (; end + 1 < s.length && s[end + 1] == s[start]; end++);

        // Go to the end of this consecutive identical consecutive
        // center in next loop.
        idx = end

        /* OPTIMIZATION: Potential improvement for early loop
         * exit by checking longest.length and idx when
         * idx > s.length // 2. Might not be worth it.
         */

        // Move the start and end pointers to the ends of the palindrome
        while (0 <= start - 1 && end + 1 < s.length && s[start - 1] == s[end + 1]) {
            start--
            end++
        }

        // Update the longest encountered palindrome
        let current = s.slice(start, end + 1)
        longest = current.length > longest.length ? current : longest
    }

    return longest
}
