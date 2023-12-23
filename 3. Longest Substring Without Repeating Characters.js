// https://leetcode.com/problems/longest-substring-without-repeating-characters

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    /**
     * Approach: Scan the input while recording the longest
     * encountered substring ending at each character. Trim
     * the start of the substring whenever a duplicate character
     * is encountered. Record the longest substring encountered
     * in this way. O(n) time.
     */

    s = s.split('')
    let longest = 0
    let substr = []
    let HALF_S = Math.floor(s.length / 2)
    for (const c of s) {
        substr.push(c)
        let first_pos = substr.findIndex(e => e == c)
        if (first_pos < substr.length - 1) {
            substr = substr.slice(first_pos + 1)

            if (substr.length == 0 && longest >= HALF_S) {
                // Nothing longer will fit the criteria
                break
            }
        }

        longest = Math.max(longest, substr.length)
    }

    return longest
};