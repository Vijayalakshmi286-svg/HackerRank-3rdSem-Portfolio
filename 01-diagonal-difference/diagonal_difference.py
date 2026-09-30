# HackerRank: Diagonal Difference
# Language: Python

def diagonalDifference(arr):
    n = len(arr)

    primary = 0
    secondary = 0

    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n - 1 - i]

    return abs(primary - secondary)
