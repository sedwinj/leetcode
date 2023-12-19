# https://leetcode.com/problems/n-queens

from queue import Queue


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        Approach: BFS. Closed list is unnecessary because no states are revisited.

        Coords and boards are in row-major order as output requires.
        """

        def valid(positions: list[tuple[int, int]], next_pos: tuple[int, int]) -> bool:
            r1, c1 = next_pos
            for pos in positions:
                r2, c2 = pos

                # Check vertical, horizontal, diagonals
                if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
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

        # Build output boards
        QUEEN = "Q"
        EMPTY = "."
        boards = []
        for solution in solutions:
            board = [[EMPTY for j in range(n)] for i in range(n)]
            for coord in solution:
                board[coord[0]][coord[1]] = QUEEN
            board = [''.join(row) for row in board]
            boards.append(board)

        return boards
