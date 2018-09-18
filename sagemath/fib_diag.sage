# Fibonaci diagonalization (see Intro to Linear Algebra, Strang, Page 300 4th ed)

# Initial values + transform
v = vector([1, 0])
A = matrix([[1, 1], [1, 0]])

# The slow way
for i in range(0, 10):
    print(A^i*v)

# The fast way using diagonalization
ev = A.eigenvectors_right()

diag_matrix_lambda = matrix([[ev[0][0], 0], [0, ev[1][0]]])
ev_matrix_s = matrix([ev[0][1][0], ev[1][1][0]]).T
ev_matrix_s_inv = ev_matrix_s.inverse()

for i in range(10):
    print(ev_matrix_s * diag_matrix_lambda^i * ev_matrix_s_inv * v)





