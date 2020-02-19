
import sys
import numpy as np
import csv
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

##################################################input
H=10
Q=0.8
Q2=Q/60
Q3=Q2*1.05
f = 50

##################################################input
print("福田真悟")
print("4517111")
print("H =",H)
print("Q[m^3/min] =",Q)
print("Q[m^3/sec] =",Q2)
print("f =",f)
print("you use input? YES===1 NO===0")
inputmode=int(input())

kyoku=2
N=0.0
Ns=0.0
while (Ns<150 or Ns>300):
    N=60*f/(kyoku/2)
    Ns=N*Q**(1/2)*H**(-3/4)
    kyoku=kyoku+2

N=1450
Ns = N * Q ** (1 / 2) * H ** (-3 / 4)
print("N=",N)
print("Ns=",Ns)

print("電動機出力は？")
if inputmode == 0:
    LM =3.7
else:
    LM=float(input())
print("LM=",LM)

d=125*(LM/N)**(1/3)
print(pycolor.RED +"d=",d,pycolor.END)
print("JISB1301より幅×高さで軸径12～17は5×5みぞは3")
print("JISB1301より幅×高さで軸径17～22は6×6みぞは3.5")
print("JISB1301より幅×高さで軸径22～30は8×7みぞは4")
print("それ以外はP130で")
print("dは変える？")
if inputmode == 0:
    d =20
else:
    d=float(input())


if (d>12 and d<=17):
    b1=5
    h1=5
    t1_1=3
    t1_2=2.3
if (d>17 and d<=22):
    b1=6
    h1=6
    t1_1=3.5
    t1_2=2.8
if (d>22 and d<=30):
    b1=8
    h1=7
    t1_1=4
    t1_2=3.3

print("b=",b1,"h=",h1,"t1=",t1_1,"t2=",t1_2)

d=125*(LM/N)**(1/3)+t1_1*2
print(pycolor.RED +"New_d=",d,pycolor.END)

print("JISB0901 20,22,25,28,30,32,35")
print("d0は？")
if inputmode == 0:
    d0 =25
else:
    d0=float(input())

if (d0>12 and d0<=17):
    b1=5
    h1=5
    t1_1=3
    t1_2=2.3
if (d0>17 and d0<=22):
    b1=6
    h1=6
    t1_1=3.5
    t1_2=2.8
if (d0>22 and d0<=30):
    b1=8
    h1=7
    t1_1=4
    t1_2=3.3
print("b=",b1,"h=",h1,"t1=",t1_1,"t2=",t1_2)
d=125*(LM/N)**(1/3)
E1=1-0.2*b1/d-1.1*t1_1/d
print(E1)
d02=d/(E1**(1/3))
print(pycolor.RED +"d0'=",d02,pycolor.END)
print("d0'は？")
if inputmode == 0:
    d02 =20
else:
    d02=float(input())
print(pycolor.BLUE +"d0'=",d02,pycolor.END)
if (d02>12 and d02<=17):
    b1=5
    h1=5
    t1_1=3
    t1_2=2.3
if (d02>17 and d02<=22):
    b1=6
    h1=6
    t1_1=3.5
    t1_2=2.8
if (d02>22 and d02<=30):
    b1=8
    h1=7
    t1_1=4
    t1_2=3.3
print(pycolor.BLUE +"b=",b1,"h=",h1,"t1=",t1_1,"t2=",t1_2,pycolor.END)

sigmay_0=343
sigmau_0=569
sigmau_bass=62.5
if sigmay_0*2/3>=sigmau_0/4:
    sigmaa=sigmau_0/4
else:
    sigmaa = sigmay_0 *2/3
toua=sigmaa/2
T=LM*10**3/2/np.pi*60/N
Fk=T*2/d02*10**3
lkmin=Fk/toua/b1
lbmin=Fk/sigmau_bass/(t1_2-0.3)
print("sigmaa=",sigmaa,"toua=",toua,"T=",T,"Fk=",Fk,"lkmin=",lkmin,"lbmin=",lbmin)
if lkmin <= lbmin:
    l1=lbmin
else:
    l1=lkmin

print("l=",l1)
lk=l1+b1
print("l=",lk)
print("JISB1301 6×6　14,16,18,20,22,25,28,32")
if inputmode == 0:
    lk =22
else:
    lk=float(input())
lb=lk+8
print(pycolor.BLUE+"lk=",lk,"lb=",lb,pycolor.END)
rk=((b1/2)**2+(d02/2+t1_2)**2)**(1/2)
print("rk=",rk)
Db=(rk+3)*2
print(pycolor.RED +"Db=",Db,pycolor.END)
Dr=(rk+5.5)*2
print(pycolor.RED +"Dr=",Dr,pycolor.END)
print("Dbは？？")
if inputmode == 0:
    Db =34
else:
    Db=float(input())
print(pycolor.BLUE +"Db=",Db,pycolor.END)
print("Drは？？")
if inputmode == 0:
    Dr =38
else:
    Dr=float(input())
print(pycolor.BLUE +"Dr=",Dr)

print(d02+2,"<=S<=",d02+6,"だからS_0＝24 e_0=27.7のM16を使うよ")
S_0=24
e_0=27.7
DM=16
#dh=2/3*(S_0**3-DM**3)/(S_0**2-DM**2)
dh=(S_0+e_0)/2
print(pycolor.RED +"dh=",dh,pycolor.END)
print("dhは？?")
if inputmode == 0:
    dh =25
else:
    dh=float(input())
print(pycolor.BLUE +"dh=",dh,pycolor.END)



normal_v=(2*9.8*H)**(1/2)
print(pycolor.BLUE +"基本の流速normal_v√2gH=",normal_v,pycolor.END)
print("Kuは？？")
if inputmode == 0:
    Ku =0.97
else:
    Ku=float(input())
print("Km1は？？")
if inputmode == 0:
    Km1 =0.175
else:
    Km1=float(input())
print("Km2は？？")
if inputmode == 0:
    Km2 =0.12
else:
    Km2=float(input())
print("Kvは？？")
if inputmode == 0:
    Kv =0.39
else:
    Kv=float(input())
print(pycolor.BLUE +"周速係数Ku=",Ku)
print("入口流速係数Km1=",Km1)
print("出口流速係数Km2=",Km2)
print("速度係数Kv=",Kv,pycolor.END)
u2=Ku*normal_v
print(pycolor.BLUE +"u2=",u2,pycolor.END)
D2=60*u2/np.pi/N*1000
print(pycolor.RED +"D2=",D2,pycolor.END)
print("D2は？")
if inputmode == 0:
    D2 =178
else:
    D2=float(input())
print(pycolor.BLUE +"D2=",D2,pycolor.END)
vm2=Km2*normal_v
print(pycolor.BLUE +"vm2=",vm2,pycolor.END)
print(pycolor.BLUE +"Q'=",Q3,pycolor.END)


print("羽数？")
if inputmode == 0:
    Z =7
else:
    Z=float(input())
S2=4#float(input())
beta2=22.5*np.pi/180#float(input())
print(pycolor.RED +"Z=",Z,"S2=",S2,"beta=",beta2*180/np.pi,"と仮定するよ～",pycolor.END)
print("理由は小型の吐き出しで")
t2_2=np.pi*D2/Z
print(pycolor.BLUE +"t2(t2_2)=",t2_2)
sigma2=S2/np.sin(beta2)
print("sigma2=",sigma2,pycolor.END)
print(t2_2/(t2_2-sigma2))
B2=Q3/(np.pi*D2*10**-3*vm2)*t2_2/(t2_2-sigma2)*10**3
print(pycolor.RED+"B2=",B2,pycolor.END)
print("B2は？？")
if inputmode == 0:
    B2 =17
else:
    B2=float(input())
print(pycolor.BLUE+"B2=",B2,pycolor.END)
vm1=Km1*normal_v
print(pycolor.BLUE +"vm1=",vm1,pycolor.END)
ve=vm1/1.2
print(pycolor.BLUE +"目玉流速ってなんや死ねve=",ve,pycolor.END)
De=(4/np.pi*Q3/ve+(dh*10**(-3))**2)**(1/2)*10**3
print(pycolor.RED +"目玉径ってなんや死ねチェックあるでDe=",De,pycolor.END)
if 2.5*e_0 <= De:
    print("cheakOK")
else:
    print("cheakout================")

print("Deは？？")
if inputmode == 0:
    De =96
else:
    De=float(input())
print(pycolor.BLUE +"目玉流速ってなんや死ねDe=",De,pycolor.END)
print("DLは？？")
if inputmode == 0:
    DL =112
else:
    DL=float(input())
print(pycolor.BLUE +"DL=",DL)
kakunin=0
while (kakunin<0.05 or kakunin>0.08):
    print("D1は？")
    if inputmode == 0:
        D1 = 92
    else:
        D1 = float(input())
    kakunin=(De-D1)/(De-dh)

print("D1=",D1)
u1=np.pi*D1*N/60*10**(-3)
print("u1=",u1)
beta1=np.arctan(1.15*vm1/u1)
print("beta1=",beta1*180/np.pi)
t2_1=np.pi*D1/Z
print("t1(t2_1)=",t2_1)
S1=2#本当？
sigma1=S1/np.sin(beta1)
print("sigma1=",sigma1,pycolor.END)
print(t2_1/(t2_1-sigma1))
B1=Q3/(np.pi*D1*10**-3*vm1)*t2_1/(t2_1-sigma1)*10**3
print(pycolor.RED+"B1=",B1,pycolor.END)
print("B1は？？")
if inputmode == 0:
    B1 =22
else:
    B1=float(input())
print(pycolor.BLUE+"B1=",B1)
Z_cheak=6.5*(D2+D1)/(D2-D1)*np.sin((beta1+beta2)/2)
print("Z_cheak=",Z_cheak)
sigmamaxFC=1/4*(3+0.27+(1-0.27)*(D1/D2)**2)*7210*u2**2*10**-6
sigmamaxCAC=1/4*(3+0.33+(1-0.33)*(D1/D2)**2)*8740*u2**2*10**-6
print(pycolor.BLUE +"sigmamaxFC",sigmamaxFC,"sigmamaxCAC",sigmamaxCAC)
if sigmamaxFC <= 7.5:
    print("FC200で決定だよ")
else:
    print("CAC402かも")
    if sigmamaxCAC <=15:
        print("CAC402だね")
    else:
        print("all_out dayo===========")

vv=Kv*normal_v
print("vv=",vv)
Av=Q2/vv*10**6
print("Av=",Av)
dv=(4/np.pi*Av)**(1/2)
print("dv=",dv)
B3=1.75*B2
print("B3=",B3)
D3=D2+4
print("D3=",D3,pycolor.END)
print("bvはP54より4mmdayo")
bv=4
Dv1=D2*1.06
Dv2=D2*1.3
print(Dv1,"<=Dv<=",Dv2)
print("Dvは？")
if inputmode == 0:
    Dv =200
else:
    Dv=float(input())
print(pycolor.BLUE +"Dv=",Dv,pycolor.END)
Ns2=6.67*Ns
print("specific_speed=",Ns2)
print("avは？[deg]")
if inputmode == 0:
    av =10*np.pi/180
else:
    av=float(input())*np.pi/180
print(pycolor.BLUE +"av=",av*180/np.pi,pycolor.END)



print("Dsは？")
if inputmode == 0:
    Ds =100
else:
    Ds=float(input())

vs=Q2/((Ds/2*10**(-3))**2*np.pi)
print("Ddは？")
if inputmode == 0:
    Dd =80
else:
    Dd=float(input())

vd=Q2/((Dd/2*10**(-3))**2*np.pi)
case_cheak=vd*vd/2/9.8/H
print(pycolor.BLUE +"Ds=",Ds,"vs=",vs,"Dd=",Dd,"vd=",vd,"cheak=",case_cheak,pycolor.END)
if case_cheak>=0.02 and case_cheak<=0.05 and vs<=3 and vs<=vd and vd<=6.5:
    print("けーじんぐはOK")
else:
    print("けーじんぐやり直し")



A0=B3*bv
A=[]
g=0
while g<=8:
    A.append(g/8*Av/100)
    g=g+1

print("A=",A)



r1=0.8*(De-dh)/2
print("r1=",r1)
print("r1は？")
if inputmode == 0:
    r1 =28
else:
    r1=float(input())

print("r1=",r1)
r2=r1*2/3
print("r2<=",r2)
r2=r1/3
print("r2>=",r2)
print("r2は？")
if inputmode == 0:
    r2 =10
else:
    r2=float(input())

print("r2=",r2)




H25=H*1.2
BL=18


print("H25=",H25)
print("DL=",DL)
d1=20+5
print("d1=",d1)
AL=np.pi*((DL/2)**2-(d1/2)**2)
print("AL=",AL)

urw=DL/2*2*np.pi/60*N*10**-3
Ta=AL*9.8*1000*(H25*(1-Kv**2)-1/4*(u2**2-urw**2)/2/9.8)*10**-6

print("urw=",urw)
print("Ta=",Ta)

B2_2=B2+S2*2
print("B2_2=",B2_2)
Tr=0.34*1000*9.8*H25*D2*B2_2*10**-6

print("Tr=",Tr)

print("面積計算中CADでの入力値あり注意[mm^3]")
print("羽根車は＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
V1=(BL+bv+12.5)*(DL**2-De**2)/4*np.pi
print("V1=",V1)

V2=(S2)*(D2**2-De**2)/4*np.pi
print("V2=",V2)

V3=(S2)*(D2**2-Dr**2)/4*np.pi
print("V3=",V3)


V4=(BL+bv)*(DL**2-De**2)/4*np.pi
print("V4=",V4)

V5=(lb)*(Dr**2)/4*np.pi
print("V5=",V5)

V6=Z*S2*B2*94
print("V6=",V6)

Vall=V1+V2+V3+V4+V5+V6
print("Vall=",Vall)
rhoFC200=7210

Wi=rhoFC200*Vall*10**-9*9.8
print("Wi=",Wi)

xgi=(-V1*32-V2*10.5+V3*10.5+V4*23.5+V5*11)/Vall
print("xgi=",xgi)

print("カップリングは＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
Vc1=19.5*np.pi*(42.5/2)**2
print("Vc1=",Vc1)

Vc2=16*np.pi*(100/2)**2
print("Vc2=",Vc2)

Wc=rhoFC200*(Vc1+Vc2)*10**-9*9.8
print("Wc=",Wc)

xgc=(Vc1*-25.75+Vc2*-8)/(Vc1+Vc2)
print("xgc=",xgc)

lziku1=24
lziku2=29
lziku3=190
lziku4=94
lziku5=60
lziku6=50
phi1=16
phi2=20
phi3=25
phi4=30
phi5=25
phi6=24
print("軸は＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")

Vziku=np.pi*((phi1/2)**2*lziku1+(phi2/2)**2*lziku2+(phi3/2)**2*lziku3+(phi4/2)**2*lziku4+(phi5/2)**2*lziku5+(phi6/2)**2*lziku6)
print("Vziku=",Vziku)

Ws=Vziku*7870*10**-9*9.8
print("Ws=",Ws)
f1=8*4+20
f2=f1*1.5
print("f1=",f1,"f2=",f2)
overfang=208.5
print("overfangオーバハング長さは",overfang)
zikuukekan=109
print("zikuukekan軸受間距離は",zikuukekan)
zikutan=92.5
print("zikutan軸端から軸受までの距離は",zikutan)



ll=(lziku4)*10**-3
al=(lziku2+lziku3)*10**-3
bl=(lziku2)*10**-3


Ill=np.pi/64*(phi4*10**-3)**4
Ial=np.pi/64*(phi3*10**-3)**4
Ibl=np.pi/64*(phi2*10**-3)**4

print("l a b",ll,al,bl,Ill,Ial,Ibl)

W1=Wi

print("W1=",W1)

sigmac1=1/3/(2.09*10**10*9.8)*(ll*al**2/Ill+(al**3-bl**3)/Ial+(bl**3)/Ibl)*W1

print("sigmac1=",sigmac1)


lr=(lziku4)*10**-3
ar=(lziku5+lziku6)*10**-3
br=(lziku6)*10**-3


Ilr=np.pi/64*(phi4*10**-3)**4
Iar=np.pi/64*(phi5*10**-3)**4
Ibr=np.pi/64*(phi6*10**-3)**4

print("l a b",lr,ar,br,Ilr,Iar,Ibr)

W2=Wc

print("W2=",W2)

sigmac2=1/3/(2.09*10**10*9.8)*(lr*ar**2/Ilr+(ar**3-br**3)/Iar+(br**3)/Ibr)*W2

print("sigmac2=",sigmac2)

Nc=60/2/np.pi*(9.8/(sigmac1+sigmac2))**(1/2)

print("Nc=",Nc)

kikensokudo=N/Nc*100

print("危険速度は",kikensokudo)


print("軸受の選定**************************")


Fr1y=(Wi*(overfang+zikuukekan-xgi)-Wc*(zikutan+xgc))/zikuukekan
Fr1x=(Tr*(overfang+zikuukekan-xgi))/zikuukekan
Fr2y=(-Wi*(overfang-xgi)+Wc*(zikutan+xgc+zikuukekan))/zikuukekan
Fr2x=(Tr*(overfang-xgi))/zikuukekan

print("Fr1x=",Fr1x)
print("Fr1y=",Fr1y)
print("Fr2x=",Fr2x)
print("Fr2y=",Fr2y)

Fr1=(Fr1x**2+Fr1y**2)**0.5
Fr2=(Fr2x**2+Fr2y**2)**0.5
print("Fr1=",Fr1)
print("Fr2=",Fr2)
Fa1=Ta/10
Fa2=0
print("Fa1=",Fa1)

print("使用する軸受は6205ですね")
f0=13.9
Cr=14000
C0r=7850

print("f0Fa1/C0r cheak",f0*Fa1/C0r,"Fa1/Fr1=",Fa1/Fr1)

e=0.38+(0.40-0.38)/(0.357-0.178)*(f0*Fa1/C0r-0.178)

print("e=",e)

if Fa1/Fr1 < e:
    X=1
    Y=0
else:
    print("めんどいから自分で線形補間よろ")
    X=0.44
    Y=1.48

P1=X*Fr1+Y*Fa1
P2=Fr2

Lk1=500*(Cr/1.4/P1)**3*33.3/N
Lk2=500*(Cr/1.4/P2)**3*33.3/N

print("Lk1=",Lk1,"Lk2=",Lk2)

P=0.7
Di=286
tk=P*Di/(20*2-1.2*P)
print("tk(ケーシングの肉厚)",tk)

Rc=D3
rc=D3/10
WW=(3+(Rc/rc)**0.5)/4

tc=P*Rc*WW/(40-0.2*P)+1
print("tc(ケーシングカバーの肉厚)",tc)

print(D2,D3)