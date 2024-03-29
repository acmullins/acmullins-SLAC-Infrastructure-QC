import numpy as np

E_i = np.full(shape =12, fill_value = 100)
E_f = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
E_closure = E_i - E_f

print(E_f)

Port = np.array([[1,0,0,0,0,0,1,0,0,0,0,0],
                 [0,1,0,0,0,0,0,1,0,0,0,0],
                 [0,0,1,0,0,0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,0,0,0,1,0,0],
                 [0,0,0,0,1,0,0,0,0,0,1,0],
                 [0,0,0,0,0,1,0,0,0,0,0,1],
                 [0,0,1,0,0,0,1,0,0,0,0,0],
                 [1,0,0,0,0,0,0,1,0,0,0,0],
                 [0,1,0,0,0,0,0,0,1,0,0,0],
                 [0,0,1,0,0,0,0,0,0,1,0,0],
                 [0,0,0,1,0,0,0,0,0,0,1,0],
                 [0,0,0,0,1,0,0,0,0,0,0,1],])

print(np.linalg.det(Port))

#A = np.linalg.solve(Port, E_closure)