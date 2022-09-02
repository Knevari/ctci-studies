# Stare into the abyss, and the abyss stares back at you

class Solution:
    # Rotate matrix with extra space
    def rotate_matrix_extra_space(self, matrix):
        o_i = 0
        o_j = 0

        result_matrix = [[0 for _ in range(len(matrix))]
                         for _ in range(len(matrix))]

        for j in range(len(matrix)):
            o_j = 0
            for i in range(len(matrix)-1, -1, -1):
                result_matrix[o_i][o_j] = matrix[i][j]
                o_j += 1
            o_i += 1

        return result_matrix

    # Bitch solution
    def rotate_matrix_in_place(self, matrix):
        N = len(matrix)

        for layer in range(N // 2):
            first = layer
            last = N - first - 1

            for i in range(first, last):
                offset = i - first

                temp = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = temp

        return matrix


def main():
    solution = Solution()

    assert solution.rotate_matrix_extra_space([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ], "rotate_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) should return [[7, 4, 1],[8, 5, 2],[9, 6, 3]]"

    assert solution.rotate_matrix_in_place([
        ["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"],
    ]) == [
        ['m', 'i', 'e', 'a'],
        ['n', 'j', 'f', 'b'],
        ['o', 'k', 'g', 'c'],
        ['p', 'l', 'h', 'd']
    ], "rotate_matrix([['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h'],['i', 'j', 'k', 'l'],['m', 'n', 'o', 'p'],]) should return [['m', 'i', 'e', 'a'], ['n', 'j', 'f', 'b'],['o', 'k', 'g', 'c'],['p', 'l', 'h', 'd']]"

    print("All tests passed!")


if __name__ == "__main__":
    main()
