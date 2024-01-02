// https://leetcode.com/problems/reverse-integer

const MIN_INT = 147483648
const MAX_INT = 147483647
const FIRST_DIGIT = 2
const MAX_LENGTH = 10

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    /*
     * Approach: Convert input to string and reverse it.
     * Compare the largest digit in x to the largest digit in
     * the maximum integer (using appropriate positive or
     * negative domain). If necessary, Convert the rest of x
     * to a 32-bit number and compare to the rest of the
     * maximum integer. Return appropriate result.
     * O(1) time.
     */

    let sign = x < 0 ? -1 : 1
    x = Math.abs(x).toString().split('').reverse().join('')
    let max = (sign < 0 ? MIN_INT : MAX_INT)

    let first_x = Number(x[0])
    let first_max = FIRST_DIGIT
    if (x.length == MAX_LENGTH && (
        first_x > first_max ||
        first_x == first_max && Number(x.slice(1)) > max)
    ) {
        return 0
    }

    return Number(x) * sign
};