import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
##%matplotlib inline
#plt.axes().set_aspect('equal', 'datalim')
#fig = plt.figure()
#ax = plt.axes()

L=0.55
r=0.01/2
m=0.34
E=2.06*10**11
M=0.53
I=4.91*10**-10
A=7.854*10**-5
rho=7871
P=9.8*M
sekiY=0
X=0

delta_x=0.001
end_x=3

ax=plt.subplot()

x = np.array([0, 0])
y = np.array([0, 100000])
plt.plot(x, y, linewidth=0.5, color="blue")
x = np.array([0, 100000])
y = np.array([0, 0])
plt.plot(x, y, linewidth=0.5, color="blue")

F1=P**2*L**3/48/E/I
print("F1=",F1)

F2=rho*A*(P/48/E/I)**2*17*L**7/35

print("F2=",F2)

F3=M*(P*L**3/48/E/I)**2

print("F3=",F3)

Hz=(F1/(F2+F3))**0.5/2/np.pi
print("Hz=",Hz)

#while x<=end_x:
#Y=M*9.8

#sekiY=sekiY+Y*delta_x

#a    plt.plot(w, A, marker='.', color="purple", markersize=1)

  #  plt.plot(X, Y, marker='.', color="purple", markersize=10)
   # plt.lines(w, H11, color="purple", markersize=10)
   # x=x+delta_x
    #print(X,Y,sekiY)

#wmax=(2*k*k/(2*m*k-c*c))**(1/2)
#Amax=wmax**2/(((k-m*wmax*wmax)**2+(c*wmax)**2)**(1/2))
#print(wmax)
#print(Amax)


plt.xlabel('x')
plt.ylabel('y')
#plt.axis('tight')
#ax.set_aspect('equal')
#plt.show()