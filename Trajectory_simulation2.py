import sys

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
##%matplotlib inline
#plt.axes().set_aspect('equal', 'datalim')
#fig = plt.figure()
ax = plt.axes()

#マス目の記載********************************
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

#マス目の記載********************************


#初期値設定
delta_time=0.001#刻み幅
g_speed=1000#最初の重心速度
angle=90*np.pi/180#旋回角度の目標値
max_angle_speed=300*np.pi/180#最大角速度
angle_acc=5000*np.pi/180#角加速度
f_ofset_distance=20#最初のオフセット
e_ofset_distance=20#最後のオフセット
g_acc=-1000#重心速度の加速度


start_x=90#初期値x
start_y=180#初期値y
x=start_x#初期値代入
y=start_y#初期値代入
start_angle=45*np.pi/180#初期値角度

K=0.000002#0.0003##スリップ角の係数
m=0.120#定数項だし意味ない


distance=0

now_t=0#現在の時間

x2=0#台形加速用時間変数
y2=0#台形加速用時間変数
x3=0#台形加速用時間変数
y3=0#台形加速用時間変数
sankaku_mode=0#三角加速用のフラグ



now_angle=start_angle#初期値代入
now_angle_speed=0
now_g_speed=g_speed

while distance<=f_ofset_distance:
    now_t+=delta_time
    x += delta_time * now_g_speed * np.sin(now_angle)
    y += delta_time * now_g_speed * np.cos(now_angle)
    now_angle_speed = 0
    now_angle=now_angle+now_angle_speed*delta_time
    now_g_speed=now_g_speed+g_acc*delta_time
    distance+=delta_time*now_g_speed
    plt.plot(x, y, marker='.', color="purple",markersize=1)
distance=0
t2=now_t

while (now_t-t2)<=max_angle_speed/angle_acc:
    now_t+=delta_time
    x += delta_time * now_g_speed * np.sin(now_angle)
    y += delta_time * now_g_speed * np.cos(now_angle)
    now_angle_speed = angle_acc * (now_t - t2)
    now_angle = now_angle + now_angle_speed * delta_time
    now_g_speed = now_g_speed + g_acc * delta_time
    plt.plot(x, y, marker='.', color="red",markersize=1)
    if now_angle-start_angle>=angle/2:
        sankaku_mode = 1
        break

t3=now_t

if sankaku_mode==0:
    while now_t-t3<=(angle-max_angle_speed*(t3-t2))/max_angle_speed:
        now_t+=delta_time
        x += delta_time * now_g_speed * np.sin(now_angle)
        y += delta_time * now_g_speed * np.cos(now_angle)
        now_angle_speed = max_angle_speed
        now_angle = now_angle + now_angle_speed * delta_time
        now_g_speed = now_g_speed + g_acc * delta_time
        plt.plot(x, y, marker='.', color="green",markersize=1)

    t4 = now_t

    while now_t-t4<=max_angle_speed/angle_acc:
        now_t+=delta_time
        x += delta_time * now_g_speed * np.sin(now_angle)
        y += delta_time * now_g_speed * np.cos(now_angle)
        now_angle_speed = max_angle_speed - angle_acc * (now_t - t4)
        now_angle = now_angle + now_angle_speed * delta_time
        now_g_speed = now_g_speed + g_acc * delta_time
        plt.plot(x, y, marker='.', color="red",markersize=1)

else:
    t4=now_t
    sankaku_max_angle_speed=now_angle_speed
    while (now_t-t4)<=(t3-t2):
        now_t += delta_time
        x += delta_time * now_g_speed * np.sin(now_angle)
        y += delta_time * now_g_speed * np.cos(now_angle)
        now_angle_speed =sankaku_max_angle_speed - angle_acc * (now_t - t4)
        now_angle = now_angle + now_angle_speed * delta_time
        now_g_speed = now_g_speed + g_acc * delta_time
        plt.plot(x, y, marker='.', color="red",markersize=1)


while distance<=e_ofset_distance:
    now_t+=delta_time
    x += delta_time * now_g_speed * np.sin(now_angle)
    y += delta_time * now_g_speed * np.cos(now_angle)
    now_angle_speed = 0
    now_angle = now_angle + now_angle_speed * delta_time
    now_g_speed = now_g_speed + g_acc * delta_time
    distance+=delta_time*now_g_speed
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


now_angle=start_angle
now_angle_speed=0
now_g_speed=g_speed

while distance<=f_ofset_distance:
    now_t+=delta_time
    x += delta_time * now_g_speed * np.sin(now_angle)
    y += delta_time * now_g_speed * np.cos(now_angle)
    now_angle_speed = 0
    now_angle=now_angle+now_angle_speed*delta_time-K*m*now_g_speed*now_angle_speed
    now_g_speed = now_g_speed + g_acc * delta_time
    distance+=delta_time*now_g_speed
    plt.plot(x, y, marker='.', color="black",markersize=1)
distance=0
t2=now_t

while (now_t-t2)<=max_angle_speed/angle_acc:
    now_t+=delta_time
    x += delta_time * now_g_speed * np.sin(now_angle)
    y += delta_time * now_g_speed * np.cos(now_angle)
    now_angle_speed = angle_acc*(now_t-t2)
    now_angle = now_angle + now_angle_speed * delta_time-K*m*now_g_speed*now_angle_speed
    now_g_speed = now_g_speed + g_acc * delta_time
    plt.plot(x, y, marker='.', color="grey",markersize=1)
    if now_angle-start_angle>=angle/2:
        sankaku_mode = 1
        break

t3=now_t

if sankaku_mode==0:
    while now_t-t3<=(angle-max_angle_speed*(t3-t2))/max_angle_speed:
        now_t+=delta_time
        x += delta_time * now_g_speed * np.sin(now_angle)
        y += delta_time * now_g_speed * np.cos(now_angle)
        now_angle_speed = max_angle_speed
        now_angle = now_angle + now_angle_speed * delta_time-K*m*now_g_speed*now_angle_speed
        now_g_speed = now_g_speed + g_acc * delta_time
        plt.plot(x, y, marker='.', color="darkred",markersize=1)

    t4 = now_t

    while now_t-t4<=max_angle_speed/angle_acc:
        now_t+=delta_time
        x += delta_time * now_g_speed * np.sin(now_angle)
        y += delta_time * now_g_speed * np.cos(now_angle)
        now_angle_speed = max_angle_speed-angle_acc*(now_t-t4)
        now_angle = now_angle + now_angle_speed * delta_time-K*m*now_g_speed*now_angle_speed
        now_g_speed = now_g_speed + g_acc * delta_time
        plt.plot(x, y, marker='.', color="grey",markersize=1)

else:
    t4=now_t
    sankaku_max_angle_speed=now_angle_speed
    while (now_t-t4)<=(t3-t2):
        now_t += delta_time
        x += delta_time * now_g_speed * np.sin(now_angle)
        y += delta_time * now_g_speed * np.cos(now_angle)
        now_angle_speed =sankaku_max_angle_speed - angle_acc * (now_t - t4)
        now_angle = now_angle + now_angle_speed * delta_time-K*m*now_g_speed*now_angle_speed
        now_g_speed = now_g_speed + g_acc * delta_time
        plt.plot(x, y, marker='.', color="grey",markersize=1)


while distance<=e_ofset_distance:
    now_t+=delta_time
    x += delta_time * now_g_speed * np.sin(now_angle)
    y += delta_time * now_g_speed * np.cos(now_angle)
    now_angle_speed = 0
    now_angle = now_angle + now_angle_speed * delta_time-K*m*now_g_speed*now_angle_speed
    now_g_speed = now_g_speed + g_acc * delta_time
    distance+=delta_time*now_g_speed
    plt.plot(x, y, marker='.', color="black",markersize=1)
distance=0
#'''

#plt.xlabel('x')
#plt.ylabel('y')
#plt.axis('equal')
ax.set_aspect('equal')
plt.show()