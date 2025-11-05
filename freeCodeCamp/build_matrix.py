def build_matrix(rows, cols):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        matrix.append(row)
    return matrix


"""
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]
"""