import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import csv
import matplotlib.patches as patche


c=1#

dt=0.01##時間の格子数
dx=0.01##空間の格子数
nu=0.0025##拡散係数
T=6##気づく時間
u=0.09#0#移流速度
X=0
t=0
Xmax=1.0#xの# 最大値
f=[[0 for i in range((int)(T/dt+1))] for j in range((int)(Xmax/dx+1))]#濃度の位置，時間での2次配列

def update_anim(i):#アニメーション用の関数

    plt.cla()#初期化
    #壁や境界の線まとめ###########################################
    x = np.array([0, 0])
    y = np.array([0, 1])
    plt.plot(x, y, linewidth=1, color="blue")
    plt.bar(-0.15, 1, 0.3, hatch="xx")

    x = np.array([0, 1.2])
    y = np.array([0, 0])
    plt.plot(x, y, linewidth=1, color="blue")

    x = np.array([0.3, 0.3])
    y = np.array([0, 1.0])
    plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

    x = np.array([0.3, 0.4])
    y = np.array([1.0, 1.0])
    plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

    x = np.array([0.4, 0.4])
    y = np.array([0, 1.0])
    plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

    x = np.array([1.0, 1.0])
    y = np.array([0, 1])
    plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")
    if i*10>T/dt:#移流に変更
        plt.text(1.0, 0.7,"exhaust\n by\n pump" )
        plt.text(1.1, 0.55, "T=")
        plt.text(1.2, 0.55, T)
    #文字一覧
    plt.text(0.5, 0.8, 't=')
    plt.text(0.6,0.8,(int)(i*dt*10))
    plt.text(0.5, 0.75, 'dx=')
    plt.text(0.6, 0.75, dx)
    plt.text(0.5, 0.7, 'dt=')
    plt.text(0.6, 0.7, dt)
    plt.text(0.5, 0.65, 'nu=')
    plt.text(0.6, 0.65, nu)
    plt.text(0.5, 0.6, 'u=')
    plt.text(0.6, 0.6, u)
    x = np.array([0.49, 0.8])
    y = np.array([0.85,0.85 ])
    plt.plot(x, y, linewidth=1, color="black")
    x = np.array([0.8, 0.8])
    y = np.array([0.85, 0.59])
    plt.plot(x, y, linewidth=1, color="black")
    x = np.array([0.49, 0.8])
    y = np.array([0.59, 0.59])
    plt.plot(x, y, linewidth=1, color="black")
    x = np.array([0.49, 0.49])
    y = np.array([0.59, 0.85])
    plt.plot(x, y, linewidth=1, color="black")
    # 壁や境界の線まとめ###########################################
    frame_list=[]
    xl=[]
    yl=[]
    X=0

    while X<=(Xmax/dx):
        xl.append(X*dx)
        yl.append(f[X][10*i])

        X=X+1
    pe = plt.plot(xl, yl, marker='.', color="red")#アニメーションの線
    frame_list.append(pe)
    return frame_list



#初期条件まとめ##########################################

xstart=0.3
xend=0.4
fstart=1.0
while xstart<xend+dx:
    f[(int)(xstart/dx)][0]=fstart

    xstart=xstart+dx

#初期条件まとめ##########################################



fig = plt.figure()
ax = plt.axes()




a=0
t=0
#移流なしの微分方程式を解く#######################################
while t < (T/dt):
    X=1
    while X <=(Xmax/dx-1):
        f[X][t+1]=c**2*dt**2/dx**2*(f[X+1][t]-2*f[X][t]+f[X-1][t])+2*f[X][t]-f[X][t-1]
        #拡散方程式

        X=X+1

    f[0][t+1] = f[1][t+1]#境界条件
    f[(int)(Xmax/dx)][t+1]=f[(int)(Xmax/dx)-1][t+1]#境界条件
    t=t+1
#移流なしの微分方程式を解く#######################################


X=0
t=0


print('you select anime---0  csv---1  makegraph---2')
#0はアニメーション，1はcsvファイル出力，2は静止画の出力
mode = int(input())

if mode==0:
    animation = ani.FuncAnimation(fig,update_anim,interval=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('tight')
    ax.set_aspect('equal')
    plt.show()
    #ani.save('output.gif',writer='imagemagick')

if mode==1:
    with open('test.csv','w',newline='') as p:
        writer = csv.writer(p)
        writer.writerow([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
        tcount=0
        while tcount < (T):
            writer.writerow([f[(int)(0/dx)][(int)(tcount/dt)],f[(int)(0.1/dx)][(int)(tcount/dt)],f[(int)(0.2/dx)][(int)(tcount/dt)],f[(int)(0.3/dx)][(int)(tcount/dt)],f[(int)(0.4/dx)][(int)(tcount/dt)],f[(int)(0.5/dx)][(int)(tcount/dt)],f[(int)(0.6/dx)][(int)(tcount/dt)],f[(int)(0.7/dx)][(int)(tcount/dt)],f[(int)(0.8/dx)][(int)(tcount/dt)],f[(int)(0.9/dx)][(int)(tcount/dt)],f[(int)(1.0/dx)][(int)(tcount/dt)]])
            tcount=tcount+1

if mode==2:
    q=0
    while q < (T):

        x = np.array([0, 0])
        y = np.array([0, 1])
        plt.plot(x, y, linewidth=1, color="blue")
        plt.bar(-0.15, 1, 0.3, hatch="xx")

        x = np.array([0, 1.2])
        y = np.array([0, 0])
        plt.plot(x, y, linewidth=1, color="blue")

        x = np.array([0.3, 0.3])
        y = np.array([0, 1.0])
        plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

        x = np.array([0.3, 0.4])
        y = np.array([1.0, 1.0])
        plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

        x = np.array([0.4, 0.4])
        y = np.array([0, 1.0])
        plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")

        x = np.array([1.0, 1.0])
        y = np.array([0, 1])
        plt.plot(x, y, linewidth=1, color="blue", linestyle="dashed")


        xl = []
        yl = []
        X = 0

        while X <= (Xmax / dx):
            xl.append(X * dx)
            yl.append(f[X][(int)(q/dt)])

            X = X + 1
        plt.plot(xl, yl, marker='.',label="t="+str(q),)
        plt.legend()
        q=q+1

    plt.xlabel('x')
    plt.ylabel('f')
    plt.axis('tight')
    ax.set_aspect('equal')
    plt.show()