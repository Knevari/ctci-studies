class Solution:
    def zero_matrix(self, matrix):
        M = len(matrix)
        N = len(matrix[0])

        rows_to_wipe = set()
        cols_to_wipe = set()

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    rows_to_wipe.add(i)
                    cols_to_wipe.add(j)

        for i in range(M):
            for j in range(N):
                if i in rows_to_wipe or j in cols_to_wipe:
                    matrix[i][j] = 0

        return matrix


def main():
    solution = Solution()

    assert solution.zero_matrix([
        [2, 1, 3, 1, 5],
        [3, 4, 1, 2, 3],
        [4, 5, 0, 2, 3],
        [8, 3, 2, 1, 3],
        [5, 2, 3, 1, 0]
    ]) == [
        [2, 1, 0, 1, 0],
        [3, 4, 0, 2, 0],
        [0, 0, 0, 0, 0],
        [8, 3, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ], "zero_matrix([[2, 1, 3, 1, 5],[3, 4, 1, 2, 3],[4, 5, 0, 2, 3],[8, 3, 2, 1, 3],[5, 2, 3, 1, 0]]) should return [[2, 1, 0, 1, 0],[3, 4, 0, 2, 0],[4, 5, 0, 2, 0],[8, 3, 0, 1, 0],[0, 0, 0, 0, 0]]"

    print("All tests passed!")


if __name__ == "__main__":
    main()
