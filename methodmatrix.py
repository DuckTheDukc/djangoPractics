# from sympy import Matrix


# def cramer_rule(A, B):
 
#     det_A = A.det()

#     if det_A == 0:
#         raise ValueError("Определитель матрицы равен нулю, невозможно решить с помощью этого метода")

#     solutions = []
#     for i in range(A.shape[0]):
#         Ai = A.copy()
#         Ai[:, i] = B
#         solutions.append(Ai.det() / det_A)

#     return solutions


# A = Matrix([
#     [1, 1, 1],
#     [5, -3, 2],
#     [3, 5, 1],
# ])

# B = Matrix([0, 1, 0])

# try:

#     solutions = cramer_rule(A, B)

#     print("Решение методом Крамера:")
#     for i, sol in enumerate(solutions, start=1):
#         print(f"x{i}: {sol}")
# except ValueError as e:

#     print(e)
    
    
# from sympy import Matrix, pprint




# augmented_matrix = Matrix([
#     [1, 1, 1, 0],
#     [5, -3, 2, 1],
#     [3, 5, 1, 0],

# ])

# row_reduced_matrix, _ = augmented_matrix.rref()

# print("x=",row_reduced_matrix[0,3])
# print("y=",row_reduced_matrix[1,3])
# print("z=",row_reduced_matrix[2,3])


from sympy import Matrix

A = Matrix([
    [1, 1, 1],
    [5, -3, 2],
    [3, 5, 1],
])

B = Matrix([0, 1, 0])

det=A.det
if det == 0:
    print("Определитель матрицы равен нулю, невозможно решить с помощью этого метода")
else:
    reverse_mat=A.inverse_CH()
    answer=reverse_mat*B
    print("x=",answer[0])
    print("y=",answer[1])
    print("z=",answer[2])