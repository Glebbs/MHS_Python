import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы разных размерностей")

        result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы разных размерностей")

        result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] * other.matrix[i][j]

        return Matrix(result)

    def __matmul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Неподходящие матрицы для умножения")

        result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.matrix])


np.random.seed(0)
A = Matrix(np.random.randint(0, 10, (10, 10)))
B = Matrix(np.random.randint(0, 10, (10, 10)))

try:
    sum_result = A + B
    mul_result = A * B
    matmul_result = A @ B
except ValueError as e:
    print(e)

with open('artifacts/3.1/matrix+.txt', 'w') as f:
    f.write(str(sum_result))

with open('artifacts/3.1/matrix*.txt', 'w') as f:
    f.write(str(mul_result))

with open('artifacts/3.1/matrix@.txt', 'w') as f:
    f.write(str(matmul_result))
