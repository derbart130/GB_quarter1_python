class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        m = []
        for i in range(len(self.matrix)):
            m.append([])
            for j in range(len(self.matrix[0])):
                m[i].append(self.matrix[i][j] + other.matrix[i][j])

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))


matrix_a = Matrix([[7, 56, 9],
                    [69, 2, 87],
                    [30, 41, 4]])

matrix_b = Matrix([[88, 13, 24],
                    [91, 46, 37],
                    [1, 3, 15]])

print(matrix_a + matrix_b)
