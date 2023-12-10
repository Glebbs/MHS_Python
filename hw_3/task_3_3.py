from task_3_2 import ArithmeticMixin, FileIOMixin, DisplayMixin, GettersSettersMixin
import numpy as np


class HashableMixin:

    def __hash__(self):
        """ Хэш-функция на основе диагональных элементов матрицы.
        Суммирует диагональные элементы и затем оставляет остаток от деления на 1000.
        """
        h = 0
        for i in range(min(len(self.data), len(self.data[0]))):
            h += int(self.data[i][i])
        return h % 1000


class AdvancedArray(ArithmeticMixin, FileIOMixin, DisplayMixin, GettersSettersMixin, HashableMixin):
    def __init__(self, data):
        self.data = np.array(data)
        self._cached_matmul = {}

    def __matmul__(self, other):
        key = (hash(self), hash(other))
        if key in self._cached_matmul:
            return self._cached_matmul[key]

        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Неподходящие матрицы для матричного умножения")
        result = self.__class__(self.data @ other.data)
        self._cached_matmul[key] = result
        return result


def find_collision():
    np.random.seed(0)

    while 1:
        A = AdvancedArray(np.random.randint(0, 10, (10, 10)))
        C = AdvancedArray(np.random.randint(0, 10, (10, 10)))

        if hash(A) == hash(C) and not np.array_equal(A.data, C.data):
            B = D = AdvancedArray(np.random.randint(0, 10, (10, 10)))
            return A, B, C, D


A, B, C, D = find_collision()

AB = A @ B
CD = C @ D

A.save_to_file('A.txt')
B.save_to_file('B.txt')
C.save_to_file('C.txt')
D.save_to_file('D.txt')
AB.save_to_file('AB.txt')
CD.save_to_file('CD.txt')

with open('artifacts/3.3/hash.txt', 'w') as f:
    f.write(f"AB hash: {hash(AB)}\n")
    f.write(f"CD hash: {hash(CD)}\n")
