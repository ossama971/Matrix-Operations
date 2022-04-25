import copy
def empty_matrix(m,n):
    mat=[]
    for i in range(m):
        newmat=[]
        for j in range(n):
            newmat.append(0)
        mat.append(newmat)
    return mat

class Matrix:
    def __init__(self,data:list[list[int]]):
        self.row=len(data)
        self.col=len(data[0])
        self.data=data

    def add(self, other):
        result=copy.deepcopy(self.data)
        for i in range(self.row) :
            for j in range(self.col) :
                result[i][j] += other.data[i][j]
        return result

    def subtract(self,other):
        result=copy.deepcopy(self.data)
        for i in range(self.row):
            for j in range(self.col):
                result[i][j]-=other.data[i][j]
        return result

    def multiply(self,other):
        result=Matrix(empty_matrix(self.row,other.col))
        for i in range(result.row):
            for j in range(result.col):
                for o in range(self.row):
                    result.data[i][j]+=self.data[i][o] * other.data[o][j]
        return result.data

       