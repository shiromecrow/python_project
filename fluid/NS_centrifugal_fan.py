import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import csv
import matplotlib.patches as patche

fig = plt.figure()
ax = plt.axes()

Din=20
Dout=40
Dmax=80
thetain=20.5*np.pi/180
fanR=40#ファンの曲率
fanN=6


x = np.array([0, Din])
y = np.array([0, 0])
plt.plot(x, y, linewidth=1.5, color="blue")

x = np.array([0, Din*np.cos(2*np.pi/fanN)])
y = np.array([0, Din*np.sin(2*np.pi/fanN)])
plt.plot(x, y, linewidth=1.5, color="blue")

now_angle=0
x=Din
y=0
while now_angle<=np.pi/180*360/fanN:
    now_angle=now_angle+0.001
    x += -0.001*Din* np.sin(now_angle)
    y +=  0.001*Din* np.cos(now_angle)
    plt.plot(x, y, marker='.', color="grey", markersize=2)

x = np.array([Din, Dout])
y = np.array([0, 0])
plt.plot(x, y, linewidth=1.5, color="red")

x = np.array([Din*np.cos(2*np.pi/fanN), Dout*np.cos(2*np.pi/fanN)])
y = np.array([Din*np.sin(2*np.pi/fanN), Dout*np.sin(2*np.pi/fanN)])
plt.plot(x, y, linewidth=1.5, color="red")

now_angle=0
x=Dout
y=0
while now_angle<=np.pi/180*360/fanN:
    now_angle=now_angle+0.001
    x += -0.001*Dout* np.sin(now_angle)
    y +=  0.001*Dout* np.cos(now_angle)
    plt.plot(x, y, marker='.', color="grey", markersize=2)

x = np.array([Dout, Dmax])
y = np.array([0, 0])
plt.plot(x, y, linewidth=1.5, color="blue")

x = np.array([Dout*np.cos(2*np.pi/fanN), Dmax*np.cos(2*np.pi/fanN)])
y = np.array([Dout*np.sin(2*np.pi/fanN), Dmax*np.sin(2*np.pi/fanN)])
plt.plot(x, y, linewidth=1.5, color="blue")

now_angle=0
x=Dmax
y=0
while now_angle<=np.pi/180*360/fanN:
    now_angle=now_angle+0.001
    x += -0.001*Dmax* np.sin(now_angle)
    y +=  0.001*Dmax* np.cos(now_angle)
    plt.plot(x, y, marker='.', color="blue", markersize=2)

while now_angle<=100
    x+=


#now_angle=3/2*np.pi+thetain
#x=Din
#y=0
#while x*x+y*y<=Dout*Dout:
#    now_angle=now_angle+0.001
#    x += -0.001*fanR* np.sin(now_angle)
#    y +=  0.001*fanR* np.cos(now_angle)
#    plt.plot(x, y, marker='.', color="blue", markersize=1)
#x1=x
#y1=y

#now_angle=3/2*np.pi+thetain+2*np.pi/fanN
#x=Din*np.cos(2*np.pi/fanN)
#y=Din*np.sin(2*np.pi/fanN)
#while x*x+y*y<=Dout*Dout:
#    now_angle=now_angle+0.001
#    x += -0.001*fanR* np.sin(now_angle)
#    y +=  0.001*fanR* np.cos(now_angle)
#    plt.plot(x, y, marker='.', color="blue", markersize=1)

#x2=x
#y2=y

#now_angle=np.arctan(y1/x1)
#x=x1
#y=y1
#while now_angle<=np.arctan(y2/x2):
#    now_angle=now_angle+0.001
#    x += -0.001*Dout* np.sin(now_angle)
#    y +=  0.001*Dout* np.cos(now_angle)
#    plt.plot(x, y, marker='.', color="grey", markersize=2)



#x = np.array([x1, x1+20*np.cos(np.arctan(y1/x1))])
#y = np.array([y1, y1+20*np.sin(np.arctan(y1/x1))])
#plt.plot(x, y, linewidth=1.5, color="blue")



#x = np.array([x2, x2+20*np.cos(np.arctan(y2/x2))])
#y = np.array([y2, y2+20*np.sin(np.arctan(y2/x2))])
#plt.plot(x, y, linewidth=1.5, color="blue")

#now_angle=np.arctan((y1+20*np.sin(np.arctan(y1/x1)))/(x1+20*np.cos(np.arctan(y1/x1))))
#x=(x1+20*np.cos(np.arctan(y1/x1)))
#y=(y1+20*np.sin(np.arctan(y1/x1)))
#while now_angle<=np.arctan((y2+20*np.sin(np.arctan(y2/x2)))/(x2+20*np.cos(np.arctan(y2/x2)))):
#    now_angle=now_angle+0.001
#    x += -0.001*(Dout+20)* np.sin(now_angle)
#    y +=  0.001*(Dout+20)* np.cos(now_angle)
#    plt.plot(x, y, marker='.', color="blue", markersize=2)







plt.axis('tight')
ax.set_aspect('equal')
plt.show()





















