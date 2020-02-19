import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

start_iti = -90   #slaは0,大回りは-90
ofset_start = 90
start_angle = 0
end_angle = 180
angle_v = 360/43.46*180/np.pi
center_v = 800
ofset_end = 90
a = 1

plt.axes().set_aspect('equal', 'datalim')
fig = plt.figure()
ax = plt.axes()


x = np.array([0, 360])
y = np.array([0, 0])
plt.plot(x, y, linewidth=1, color="blue")

x = np.array([0, 0])
y = np.array([0, 360])
plt.plot(x, y, linewidth=1, color="blue")

x = np.array([360, 0])
y = np.array([360, 360])
plt.plot(x, y, linewidth=1, color="blue")

x = np.array([360, 360])
y = np.array([0, 360])
plt.plot(x, y, linewidth=1, color="blue")

x = np.array([0, 360])
y = np.array([180, 180])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([180, 180])
y = np.array([0, 180])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([0, 360])
y = np.array([270, 270])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([270, 270])
y = np.array([0, 360])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([0, 360])
y = np.array([180, 180])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")


x = np.array([180, 180])
y = np.array([0, 180])
plt.plot(x, y, linewidth=1, color="blue")

x = np.array([0, 360])
y = np.array([90, 90])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([90, 90])
y = np.array([0, 360])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([180, 180])
y = np.array([180, 360])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([0, 90])
y = np.array([90, 0])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([90, 180])
y = np.array([0, 90])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([0, 90])
y = np.array([90, 180])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.array([90, 180])
y = np.array([180, 90])
plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

x = np.linspace(np.pi-np.pi/180*start_angle, np.pi-np.pi/180*end_angle, 201)
plt.plot(np.cos(x)*(180*center_v/np.pi/angle_v)+90+(180*center_v/np.pi/angle_v), np.sin(x)*(180*center_v/np.pi/angle_v)+180+ofset_start+start_iti, linewidth=3, color="red")#input start_iti input start_angle input angle_range

x = np.array([90, 90])
y = np.array([180+start_iti, 180+ofset_start+start_iti])
plt.plot(x, y, linewidth=3, color="green")

x = np.array([np.cos(np.pi-np.pi/180*end_angle)*(180*center_v/np.pi/angle_v)+90+(180*center_v/np.pi/angle_v), np.cos(np.pi-np.pi/180*end_angle)*(180*center_v/np.pi/angle_v)+90+(180*center_v/np.pi/angle_v)+ofset_end*np.sin(np.pi-np.pi/180*end_angle)])
y = np.array([np.sin(np.pi-np.pi/180*end_angle)*(180*center_v/np.pi/angle_v)+180+ofset_start+start_iti, np.sin(np.pi-np.pi/180*end_angle)*(180*center_v/np.pi/angle_v)+180+ofset_start-ofset_end*np.cos(np.pi-np.pi/180*end_angle)+start_iti])
plt.plot(x, y, linewidth=3, color="green")



plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
ax.set_aspect('equal')
plt.show()



