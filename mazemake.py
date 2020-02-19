import sys
import numpy as np
import csv
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.patches as patches
import cv2

#img1 = cv2.imread('2011Maze_MMCF.png')
#gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#th, bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#plt.imshow(img1)
#cv2.imwrite("result.png",bin)

i=0

fig = plt.figure()
ax = plt.axes()


x = np.array([0, 2880])
y = np.array([0, 0])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([0, 0])
y = np.array([0, 2880])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([0, 2880])
y = np.array([2880, 2880])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([2880, 2880])
y = np.array([0, 2880])
plt.plot(x, y, linewidth=2, color="blue")

for i in range(15):
    x = np.array([0, 2880])
    y = np.array([180*(i+1), 180*(i+1)])
    plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

for i in range(15):
    y = np.array([0, 2880])
    x = np.array([180*(i+1), 180*(i+1)])
    plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")





#column=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#row=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Tcolumn=[21700,12384,5130,32263,5637,1030,419,114,443,1095,5635,24071,5132,12356,21742]
Trow=[27703,24582,3460,32382,31870,15992,15800,32318,30443,25542,31702,17378,24298,14317,28155]
shift=1
tt=0

for i in range(15):
    for tt in range(16):
        shift =1
        shift=shift<<tt
        presence = (int)(Trow[i]) & (int)(shift)
        if presence>0:
            y = np.array([0+tt*180, 180+180*tt])
            x = np.array([180 * (i + 1), 180 * (i + 1)])
            plt.plot(x, y, linewidth=1, color="red")


for i in range(15):
    for tt in range(16):
        shift =1
        shift=shift<<tt
        presence = (int)(Tcolumn[i]) & (int)(shift)
        if presence>0:
            x = np.array([0+tt*180, 180+180*tt])
            y = np.array([180 * (i + 1), 180 * (i + 1)])
            plt.plot(x, y, linewidth=1, color="red")

n=0
plt.text(7*180,7*180,n,size=10)
plt.text(7*180,8*180,n,size=10)
plt.text(8*180,7*180,n,size=10)
plt.text(8*180,8*180,n,size=10)

e = patches.CirclePolygon(xy=(90, 90), radius=70, resolution=5, fc='g', ec='g')

ax.add_patch(e)

x=0
y=0

#animation = ani.FuncAnimation(fig, update_anim, interval=1)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
ax.set_aspect('equal')
plt.show()