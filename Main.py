from Operations import Matrix, empty_matrix
matrix_1=Matrix([[1,2],[3,4]])
matrix_2=Matrix([[4,5,4],[6,7,1]])
matrix_3=Matrix([[6,2],[2,5]])

matrix4=empty_matrix(2,2) #empty matrix ex
print(matrix4)

print(matrix_1.add(matrix_3)) # addition ex

print(matrix_1.subtract(matrix_1)) #subtraction ex

print(matrix_1.multiply(matrix_2)) #multiplication ex