// https://leetcode.com/problems/zigzag-conversion

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
    /*
     * Approach: Build zigzag (up-down) pattern and then stringify.
     * O(n) time.
     */

    if (numRows == 1) {
        return s
    }

    let pos = 0
    let board = []
    for (let i = 0; i < numRows; i++) {
        board.push([])
    }

    // Create pattern
    let move = 1
    for (let c of s) {
        board[pos].push(c)
        pos += move

        if (pos < 0 || numRows <= pos) {
            move = -move
            pos += 2 * move
        }
    }

    // Stringify pattern
    return board.flat().join('')
};