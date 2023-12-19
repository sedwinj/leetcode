# https://leetcode.com/problems/n-queens-ii

from queue import Queue


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Approach: BFS. Closed list is unnecessary because no states are revisited.

        Coords and boards are in row-major order as output requires.
        """

        def valid(positions: list[tuple[int, int]], next_pos: tuple[int, int]) -> bool:
            r1, c1 = next_pos
            for pos in positions:
                r2, c2 = pos

                # Check vertical, diagonals
                if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    return False

            return True

        # queue element: (board, positions)
        open_list = Queue()
        open_list.put(([]))
        solutions = []

        # BFS
        while not open_list.empty():
            positions = open_list.get()
            row = len(positions)

            # Evaluate
            if len(positions) == n:
                solutions.append(positions)
                continue

            # Expand
            for col in range(n):
                next_pos = (row, col)
                if valid(positions, next_pos):
                    open_list.put((positions.copy() + [next_pos]))

        return len(solutions)
