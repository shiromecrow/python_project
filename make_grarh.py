import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
##%matplotlib inline
#plt.axes().set_aspect('equal', 'datalim')
#fig = plt.figure()
#ax = plt.axes()

k=10000
m=2
c=0.1
w=0
delta_w=0.01
end_w=20
xmasyu = [10, 10]


ax=plt.subplot()

x = np.array([0, 0])
y = np.array([0, 100000])
#plt.plot(x, y, linewidth=0.5, color="blue")
x = np.array([0, 100000])
y = np.array([0, 0])
#plt.plot(x, y, linewidth=0.5, color="blue")
a=9.0
q=2.0
p=1

while w<=end_w:
#    A=w**2/(((k-m*w*w)**2+(c*w)**2)**(1/2))
    Re=(k-m*w*w)/(((k-m*w*w)**2+(c*w)**2)**(1/2))
    Im=(-c*w)/(((k-m*w*w)**2+(c*w)**2)**(1/2))
    H11=abs(1/40/(1-w**2/2)+1/40/(1-w**2/5)+9/840/(1-w**2/7))
    H12=abs(2/40/(1-w**2/2)-12/840/(1-w**2/7))
    H13=abs(1/40/(1-w**2/2)-1/40/(1-w**2/5)+9/840/(1-w**2/7))
    H22=abs(4/40/(1-w**2/2)+16/840/(1-w**2/7))
    H23=abs(2/40/(1-w**2/2)-12/840/(1-w**2/7))
    H33=abs(1/40/(1-w**2/2)+1/40/(1-w**2/5)+9/840/(1-w**2/7))
    xmasyu.append(abs(-delta_w**2*(a-2*q*np.cos(2*w))*xmasyu[p]+2*xmasyu[p]-xmasyu[p-1]))

#a    plt.plot(w, A, marker='.', color="purple", markersize=1)
 #   ax.set_xlim(0,50)
 #   ax.set_ylim(0,20)
    plt.plot(w, xmasyu[p], marker='.', color="purple", markersize=10)
   # plt.lines(w, H11, color="purple", markersize=10)
    w=w+delta_w
    p=p+1
    print(w)

#print(xmasyu)
#wmax=(2*k*k/(2*m*k-c*c))**(1/2)
#Amax=wmax**2/(((k-m*wmax*wmax)**2+(c*wmax)**2)**(1/2))
#print(wmax)
#print(Amax)


plt.xlabel('x')
plt.ylabel('y')
#plt.axis('tight')
#ax.set_aspect('equal')
plt.show()