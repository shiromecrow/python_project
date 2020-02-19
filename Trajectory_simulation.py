import sys

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
##%matplotlib inline
#plt.axes().set_aspect('equal', 'datalim')
#fig = plt.figure()
ax = plt.axes()


x = np.array([0, 360])
y = np.array([0, 0])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([0, 0])
y = np.array([0, 360])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([360, 0])
y = np.array([360, 360])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([360, 360])
y = np.array([0, 360])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([0, 360])
y = np.array([180, 180])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([180, 180])
y = np.array([0, 180])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([0, 360])
y = np.array([270, 270])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([270, 270])
y = np.array([0, 360])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")




x = np.array([180, 180])
y = np.array([0, 180])
plt.plot(x, y, linewidth=2, color="blue")

x = np.array([0, 360])
y = np.array([90, 90])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([90, 90])
y = np.array([0, 360])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([180, 180])
y = np.array([180, 360])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([0, 90])
y = np.array([90, 0])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([90, 270])
y = np.array([0, 180])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([0, 90])
y = np.array([90, 180])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([90, 270])
y = np.array([180, 0])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([0, 90])
y = np.array([270, 180])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([0, 90])
y = np.array([270, 360])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([90, 270])
y = np.array([360, 180])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([90, 270])
y = np.array([180, 360])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([270, 360])
y = np.array([360, 270])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([270, 360])
y = np.array([180, 270])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([270, 360])
y = np.array([180, 90])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")

x = np.array([270, 360])
y = np.array([0, 90])
plt.plot(x, y, linewidth=0.5, color="blue", linestyle="dashed")


delta_time=0.001
g_speed=1000
angle=90*np.pi/180
max_angle_speed=900*np.pi/180
angle_acc=5000*np.pi/180
f_ofset_distance=20
e_ofset_distance=60

start_x=90
start_y=180
x=start_x
y=start_y
start_angle=45*np.pi/180



K=0.0002#0.0003##スリップ角の係数
#R0.0003
#R0.0003

m=0.120
R=1#g_speed/angle_acc/t
Fout=m*g_speed*g_speed/R#遠心力mrw^2


now_angle=0
now_angle_speed=0
distance=0

t1=0
t2=0
t3=0
t4=0
t5=0
x2=0
y2=0
x3=0
y3=0
sankaku_mode=0





##for i in range((int)(f_ofset_distance/delta)):
##    y+=delta
##    plt.plot(x, y, marker='.', color="blue")
while distance<=f_ofset_distance:
    t1+=delta_time
    x += delta_time * g_speed * np.sin(start_angle)
    y += delta_time * g_speed * np.cos(start_angle)
    distance+=delta_time*g_speed
    plt.plot(x, y, marker='.', color="purple",markersize=1)
distance=0

while t2<=max_angle_speed/angle_acc:
    t2+=delta_time
    x += delta_time*g_speed * np.sin(t2 * t2 * angle_acc / 2+start_angle)
    y += delta_time*g_speed * np.cos(t2 * t2 *angle_acc/2+start_angle)
    plt.plot(x, y, marker='.', color="red",markersize=1)
    if t2 * t2 * angle_acc / 2>=angle/2:
        sankaku_mode = 1
        break
if sankaku_mode==0:
    while t3<=(angle-max_angle_speed*t2)/max_angle_speed:
        t3+=delta_time
        x += delta_time*g_speed * np.sin(t2 * t2 * angle_acc / 2+t3*angle_acc*t2+start_angle)
        y += delta_time*g_speed * np.cos(t2 * t2 *angle_acc/2+t3*angle_acc*t2+start_angle)
        plt.plot(x, y, marker='.', color="green",markersize=1)

    while t4<=max_angle_speed/angle_acc:
        t4+=delta_time
        x += delta_time * g_speed * np.sin(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle)
        y += delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle)
        plt.plot(x, y, marker='.', color="red",markersize=1)

else:
    while t4<=t2:
        t4+=delta_time
        x += delta_time * g_speed * np.sin(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle)
        y += delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle)
        plt.plot(x, y, marker='.', color="red",markersize=1)

theta1=np.arctan((delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle))/(delta_time * g_speed * np.sin(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle)))
print(theta1)
while distance<=e_ofset_distance:
    t5+=delta_time
    if delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+t4 * t4 * angle_acc / 2)<0 and delta_time * g_speed * np.sin(theta1)>0:
        x -= delta_time * g_speed * np.cos(theta1)
        y -= delta_time * g_speed * np.sin(theta1)
    else:
        x += delta_time * g_speed * np.cos(theta1)
        y += delta_time * g_speed * np.sin(theta1)
    distance+=delta_time*g_speed
    plt.plot(x, y, marker='.', color="purple",markersize=1)
distance=0



distance=0
x=start_x
y=start_y
t1=0
t2=0
t3=0
t4=0
t5=0
x2=0
y2=0
x3=0
y3=0
sankaku_mode=0


R=1#g_speed/angle_acc/t


while distance<=f_ofset_distance:
    t1+=delta_time
    x += delta_time * g_speed * np.sin(start_angle)
    y += delta_time * g_speed * np.cos(start_angle)
    distance+=delta_time*g_speed
    plt.plot(x, y, marker='.', color="black",markersize=1)
distance=0

while t2<=max_angle_speed/angle_acc:
    t2+=delta_time
    x += delta_time*g_speed * np.sin(t2 * t2 * angle_acc / 2-K*m*g_speed*g_speed/g_speed*angle_acc*t2+start_angle)
    y += delta_time*g_speed * np.cos(t2 * t2 *angle_acc/2-K*m*g_speed*g_speed/g_speed*angle_acc*t2+start_angle)
    plt.plot(x, y, marker='.', color="grey",markersize=1)
    if t2 * t2 * angle_acc / 2 >= angle / 2:
        sankaku_mode = 1
        break

if sankaku_mode == 0:
    while t3<=(angle-max_angle_speed*t2)/max_angle_speed:
        t3+=delta_time
        x += delta_time*g_speed * np.sin(t2 * t2 * angle_acc / 2+t3*angle_acc*t2-K*m*g_speed*g_speed/g_speed*angle_acc*t2+start_angle)
        y += delta_time*g_speed * np.cos(t2 * t2 *angle_acc/2+t3*angle_acc*t2-K*m*g_speed*g_speed/g_speed*angle_acc*t2+start_angle)
        plt.plot(x, y, marker='.', color="darkred",markersize=1)

    while t4<=max_angle_speed/angle_acc:
        t4+=delta_time
        x += delta_time * g_speed * np.sin(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2-K*m*g_speed*g_speed/g_speed*angle_acc*(t2-t4)+start_angle)
        y += delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2-K*m*g_speed*g_speed/g_speed*angle_acc*(t2-t4)+start_angle)
        plt.plot(x, y, marker='.', color="grey",markersize=1)

else:
    while t4<=t2:
        t4+=delta_time
        x += delta_time * g_speed * np.sin(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle)
        y += delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2+start_angle)
        plt.plot(x, y, marker='.', color="grey",markersize=1)


theta1=np.arctan((delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2-K*m*g_speed*g_speed/g_speed*angle_acc*(t2-t4)+start_angle))/(delta_time * g_speed * np.sin(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+angle_acc*t2*t4-t4 * t4 * angle_acc / 2-K*m*g_speed*g_speed/g_speed*angle_acc*(t2-t4)+start_angle)))
print(theta1)
while distance<=e_ofset_distance:
    t5+=delta_time
    if delta_time * g_speed * np.cos(t2 * t2 * angle_acc / 2 + t3 * angle_acc * t2+t4 * t4 * angle_acc / 2)<0 and delta_time * g_speed * np.sin(theta1)>0:
        x -= delta_time * g_speed * np.cos(theta1)
        y -= delta_time * g_speed * np.sin(theta1)
    else:
        x += delta_time * g_speed * np.cos(theta1)
        y += delta_time * g_speed * np.sin(theta1)
    distance+=delta_time*g_speed
    plt.plot(x, y, marker='.', color="black",markersize=1)
distance=0
#'''

#plt.xlabel('x')
#plt.ylabel('y')
#plt.axis('equal')
ax.set_aspect('equal')
plt.show()