import numpy as np


class ArithmeticMixin:

    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def __sub__(self, other):
        return self.__class__(self.data - other.data)

    def __mul__(self, other):
        return self.__class__(self.data * other.data)

    def __truediv__(self, other):
        return self.__class__(self.data / other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Неподходящие матрицы для матричного умножения")
        return self.__class__(self.data @ other.data)


class FileIOMixin:

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
        self.data = np.fromstring(data, sep='\n')


class DisplayMixin:

    def __str__(self):
        return str(self.data)


class GettersSettersMixin:

    def set_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data


class AdvancedArray(ArithmeticMixin, FileIOMixin, DisplayMixin, GettersSettersMixin):
    def __init__(self, data):
        self.data = np.array(data)


def update_data(self, new_data):
    self.data = np.array(new_data)


if __name__ == '__main__':
    np.random.seed(0)
    matrix1 = np.random.randint(0, 10, (10, 10)).tolist()
    matrix2 = np.random.randint(0, 10, (10, 10)).tolist()

    A = AdvancedArray(matrix1)
    B = AdvancedArray(matrix2)

    C = A + B
    C.save_to_file('matrix+.txt')

    D = A - B
    D.save_to_file('matrix-.txt')

    E = A * B
    E.save_to_file('matrix*.txt')

    F = A @ B
    F.save_to_file('matrix@.txt')

    # Получение данных из объекта матрицы
    print("Data from A:")
    print(A.get_data())

    # Обновление матрицы A и отображение новой матрицы
    new_data = np.random.randint(0, 10, (5, 5)).tolist()
    A.set_data(new_data)
    print("\nUpdated A:")
    print(A)
