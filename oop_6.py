import random


class MatrixUtils:
    @staticmethod
    def zeros(rows:int, cols:int):
        m = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(0)
            m.append(row)
        return m

    @staticmethod
    def identity(n):
        m = MatrixUtils.zeros(n, n)
        for i in range(n):
            m[i][i] = 1
        return m

    @staticmethod
    def from_list(data:list, rows:int, cols:int):
        m = []
        i = 0
        for r in range(rows):
            m.append(data[i:i + cols])
            i += cols
        return m

    @staticmethod
    def random_matrix(rows, cols, min_val=1, max_val=10):
        m = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(random.randint(min_val, max_val))
            m.append(row)
        return m

    @staticmethod
    def pattern_matrix(rows, cols, pattern_func):
        m = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(pattern_func(i, j))
            m.append(row)
        return m

    @staticmethod
    def dimensions(matrix):
        return (len(matrix), len(matrix[0]))

    @staticmethod
    def total_sum(matrix):
        sum = 0
        for r in matrix:
            for c in r:
                if isinstance(c, int|float):
                    sum += c
        return sum

    @staticmethod
    def min_max(matrix):
        min = matrix[0][0]
        max = matrix[0][0]
        for r in matrix:
            for c in r:
                    if c < min:
                        min = c
                    elif c > max:
                        max = c
        return (min, max)
    