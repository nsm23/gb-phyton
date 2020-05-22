class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join('\t'.join([str(el) for el in i]) for i in self.my_list))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for el in range(len(other.my_list)):
                self.my_list[i][el] = self.my_list[i][el] + other.my_list[i][el]
        return Matrix.__str__(self)


matrix_1 = Matrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]])
matrix_2 = Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

print(f'Matrix 1: \n{matrix_1.__str__()} \nMatrix 2:\n{matrix_2.__str__()}')
print()
print(f'Sum(matrix_1 + matrix_2):\n{matrix_1.__add__(matrix_2)}')
