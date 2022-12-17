class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                s = s + '\t' + str(self.matrix[i][j])
            s += '\n'
        return s

    def __add__(self, mx2):
        res = self.matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res[i][j] = self.matrix[i][j] + mx2.matrix[i][j]
        return Matrix(res)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
z = s + m
print('z')
print(z)
print(type(z))
