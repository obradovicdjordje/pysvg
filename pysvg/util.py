import numpy as np
import math

def intersection(A, B, C, D):
    a00 = B[0]-A[0]
    a01 = C[0]-D[0]
    b0  = C[0]-A[0]

    a10 = B[1]-A[1]
    a11 = C[1]-D[1]
    b1  = C[1]-A[1]
    d = a01*a10-a11*a00
    if d != 0:
        if a10 != 0:
            v = (a10*b0-a00*b1)/d
            u = (b1-a11*v)/a10
            return C+v*(D-C), u, v
        else:
            if a11 != 0:
                v = b1/a11
                u = (b0-a01*v)/a00
                return C+v*(D-C), u, v

'''      A 30,0
         |
    C------------D 20
         |
         B 30,50
'''

if __name__ == "__main__":
    A = np.array([10.0, 0.0])
    B = np.array([10.0, 10.0])
    C = np.array([10.0, 20.0])
    D = np.array([40.0, 20.0])
    print intersection(A, B, C, D)






