# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Approach: Walk the matrix in a spiral direction. O(n) time.

        Personal Challenge: Approach is non-destructive. Original matrix is unaltered.

        Matrix recieved in row major order.
        """

        def in_bounds(pos: tuple[int, int]):
            return pos[0] in range(len(matrix)) and pos[1] in range(len(matrix[0]))

        output = []
        accessed = [[False for _ in matrix[0]] for _ in enumerate(matrix)]
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pos = (0, -1)
        count = 0
        while True:
            step = steps[count % len(steps)]
            count += 1

            # Check if all elements accessed
            next_pos = (pos[0] + step[0], pos[1] + step[1])
            if not in_bounds(next_pos) or accessed[next_pos[0]][next_pos[1]]:
                break

            while True:
                pos = (pos[0] + step[0], pos[1] + step[1])
                if (not in_bounds(pos) or accessed[pos[0]][pos[1]]):
                    pos = (pos[0] - step[0], pos[1] - step[1])
                    break
                accessed[pos[0]][pos[1]] = True
                output.append(matrix[pos[0]][pos[1]])

        return output
