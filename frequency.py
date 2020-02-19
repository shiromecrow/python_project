import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

Tw=0.00007
Rm=1.07
Rm2=1.37
kt=0.00198
start_speed=500/1000
ng=40/11
kb=0.02
tireR=22.7/1000
acceleration=-1000/1000
Im=0.000000059

V_R = ((((Im * ng * acceleration / tireR) + Tw) * Rm / kt)
			+ (start_speed * ng * kb / tireR))/8.5*4000;
V_R2 = ((((Im * ng * acceleration / tireR) + Tw) * Rm2 / kt)
			+ (start_speed * ng * kb / tireR))/8.5*4000;
gosa=abs(V_R2-V_R)/V_R*100
print("結果1 =",V_R)
print("結果2 =",V_R2)
print("誤差 =",gosa)

Ksp=0.006
Ksi=0.003
Ksd=0.001
delta_speed=40
delta_distance=100
delta_accel=10


PID_s=Ksp*delta_speed+Ksi*delta_distance+Ksd*delta_accel
duty=PID_s/8.5*4000
print("PID=",PID_s)
print("dutyPID=",duty)

Turn_acceleration=1000
pi=3.14
tread=0.0675
ImT=0.0000032
TwT=0.0016
angle_speed=500
kbT=0.005


V_all = (((ImT * ng * Turn_acceleration*pi/180*tread/2/ tireR) + TwT) * Rm2 / kt)+ (angle_speed*pi/180*tread/2  * ng * kbT / tireR)
V_acc =ImT * ng * Turn_acceleration*pi/180*tread/2 / tireR * Rm2 / kt
V_vet =angle_speed*pi/180*tread/2 * ng * kbT / tireR
V_tola=TwT * Rm2 / kt
V_at=((ImT * ng * Turn_acceleration*pi/180*tread/2 / tireR) + TwT) * Rm2 / kt

print("V_all=",V_all)
print("V_acc=",V_acc)
print("V_speed=",V_vet)
print("V_tola=",V_tola)
print("V_at=",V_at)
keyl2= float(input())

# C1 = 1000
# C2 = 1*10^-6
# C3 = 10*10^-6
# C4 = 100*10^-6
# R = 10
# V = 5
#
# plt.axes().set_aspect('equal', 'datalim')
# fig = plt.figure()
# ax = plt.axes()
#
#
#
#
# x = np.linspace(0 , 100000000 , 201)
# plt.plot(x,V*(R)/(R+(1/(2*np.pi*C1*x))), linewidth=3, color="red")#input start_iti input start_angle input angle_range
#
#
#
#
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis('tight')
# ax.set_aspect('equal')
# plt.show()