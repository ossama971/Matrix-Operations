import numpy as np
class Matrix:
    def __init__(self,data:list[list[int]]):
        self.row=len(data)
        self.col=len(data[0])
        self.data=data

    def add(self, other):
        result=self.data.copy()
        for i in range(self.row) :
            for j in range(self.col) :
                result[i][j] += other.data[i][j]
        return result

    def subtract(self,other):
        result=self.data.copy()
        for i in range(self.row):
            for j in range(self.col):
                result[i][j]-=other.data[i][j]
        return result

    def multiply(self,other):
        result= np.dot(self.data,other.data)
        return result