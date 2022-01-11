class Matrix :
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Matrix({self.data})"

    def __add__(self, other):
        assert (len(self.data) == len(other.data)), "두 행열의 크기가 달라서 더할 수 없습니다"
        for i in range(len(self.data)):
            assert len(self.data[i]) == len(other.data[i]), "두 행열의 크기가 달라서 더할 수 없습니다"

        new_list = []
        for i in range(len(self.data)):
            row_list = []
            for j in range(len(self.data[i])):
                row_list.append(self.data[i][j] + other.data[i][j])
            new_list.append(row_list)
        return Matrix(new_list)


    def __mul__(self,other):
        if type(other) == Matrix:

            assert len(self.data)==len(other.data[0]), "두 행열을 곱할 수 없습니다"

            new_list = []
            for i in range(len(self.data)):

                row_list = []
                for j in range(len(other.data[0])):
                    sum = 0
                    for k in range(len(other.data)):
                        sum += self.data[i][k] * other.data[k][j]
                    row_list.append(sum)
                new_list.append(row_list)
            return Matrix(new_list)

        else:
            return Matrix([[a * other for a in self_list] for self_list in self.data])


    def __rmul__(self,other):
        return Matrix([[a * other for a in self_list] for self_list in self.data])

    def __sub__(self, other):
        assert (len(self.data) == len(other.data)), "두 행열의 크기가 달라서 뺄 수 없습니다"
        for i in range(len(self.data)):
            assert len(self.data[i]) == len(other.data[i]), "두 행열의 크기가 달라서 뺄 수 없습니다"

        new_list = []
        for i in range(len(self.data)):
            row_list = []
            for j in range(len(self.data[i])):
                row_list.append(self.data[i][j] - other.data[i][j])
            new_list.append(row_list)
        return Matrix(new_list)
