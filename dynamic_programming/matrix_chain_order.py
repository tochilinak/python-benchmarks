import sys

"""
Dynamic Programming
Implementation of Matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""


def matrix_chain_order(array):
    n = len(array)
    matrix = [[0 for x in range(n)] for x in range(n)]
    sol = [[0 for x in range(n)] for x in range(n)]

    for chain_length in range(2, n):
        for a in range(1, n - chain_length + 1):
            b = a + chain_length - 1

            matrix[a][b] = sys.maxsize
            for c in range(a, b):
                cost = (
                    matrix[a][c] + matrix[c + 1][b] + array[a - 1] * array[c] * array[b]
                )
                if cost < matrix[a][b]:
                    matrix[a][b] = cost
                    sol[a][b] = c
    return matrix, sol


# Print order of matrix with Ai as Matrix
def print_optiomal_solution(optimal_solution, i, j):
    if i == j:
        print("A" + str(i), end=" ")
    else:
        print("(", end=" ")
        print_optiomal_solution(optimal_solution, i, optimal_solution[i][j])
        print_optiomal_solution(optimal_solution, optimal_solution[i][j] + 1, j)
        print(")", end=" ")