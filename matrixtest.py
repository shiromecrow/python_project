import sys
import numpy as np
import csv
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches



print("逆行列テスト")

omegatest=1

#mat=np.matrix([[20-4*omegatest**2,-6,0],[-6,12-3*omegatest**2,-6],[0,-6,20-4*omegatest**2]])

mat=np.matrix([[-1,-4,0,0],[0,5,-1,0],[0,-1,5,-4],[0,0,-4,4]])
X=np.matrix([[2],[3],[4]])
SS=np.matrix([[22],[0],[62]])
PP=np.matrix([[1],[0],[0]])
print(mat)

#mat2=np.dot(mat,X)
#print(mat2)

mat3=mat**-1
print(mat3)

#mat4=np.dot(mat3,SS)
#print(mat4)

mat5=np.linalg.det(mat)
print(mat5)

mat6=mat5*mat3
print(mat6)

#mat7=mat5*np.dot(mat3,PP)
#print(mat7)


print("test_end**********************************")