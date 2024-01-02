// https://leetcode.com/problems/string-to-integer-atoi

const MIN_INT = -2147483648
const MAX_INT = 2147483647
const MAX_LENGTH = 10
const CHAR_0 = '0'.charCodeAt(0)

/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
    /*
     * Approach: Parse each character in the input. Return early if output would
     *           exceed the 32-bit integer range. O(n) time. O(1) time after
     *           leading spaces are processed.
     */

    let sign = 1
    let idx = 0
    for (; idx < s.length && s[idx] == ' '; idx++);

    if (s[idx] == '+') {
        idx++
    }
    else if (s[idx] == '-') {
        sign = -1
        idx++
    }

    let digit = null
    let result = 0
    for (; idx < s.length; idx++) {
        digit = s.charCodeAt(idx) - CHAR_0
        console.log(digit)
        if (digit < 0 || 9 < digit) {
            break
        }

        result = result * 10 + digit * sign

        if (result > MAX_INT) {
            return MAX_INT
        }

        if (result < MIN_INT) {
            return MIN_INT
        }
    }

    return result
};