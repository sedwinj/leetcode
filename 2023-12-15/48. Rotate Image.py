# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: list[list[int]], edge_dist: int = None) -> None:
        """
        Requirements: Do not return anything, modify matrix in-place instead.

        Approach: rotate the edge of the matrix. Recurse with the unaltered core
                  as the next matrix.
        """

        # edge_dist: the dist between the current edge and the true edge

        if not edge_dist:
            edge_dist = 0

        # Stop if there is nothing left to rotate
        if edge_dist > (len(matrix) - 1) / 2:
            return

        bounds = [0 + edge_dist, len(matrix) - 1 - edge_dist]

        edges = []
        edges.append([matrix[bounds[0]][x]
                     for x in range(bounds[0], bounds[1])])
        edges.append([matrix[y][bounds[1]]
                     for y in range(bounds[0], bounds[1])])
        edges.append([matrix[bounds[1]][x]
                     for x in range(bounds[1], bounds[0], -1)])
        edges.append([matrix[y][bounds[0]]
                     for y in range(bounds[1], bounds[0], -1)])

        coord = (bounds[0], bounds[1])
        steps = iter([(1, 0), (0, -1), (-1, 0), (0, 1)])
        for edge in edges:
            step = next(steps)
            for val in edge:
                print("val = ", val, "\ncoord = ", coord)
                matrix[coord[0]][coord[1]] = val
                coord = (coord[0] + step[0], coord[1] + step[1])

        self.rotate(matrix, edge_dist + 1)
