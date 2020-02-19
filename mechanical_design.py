
import sys
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
##################################################input
power = 18500
f = 50
n = 2
R =2.25
##################################################input
print("福田真悟")
print("4517111")
print("power =",power)
print("p =",n)
print("f =",f)
print("R =",R)

Nin = 120*f/n
Nout = Nin/R

print("Nin =",Nin,"Nout =",Nout)

Tin = power/(Nin*2*np.pi/60)
Tout = power/(Nout*2*np.pi/60)

print("Tin =",Tin,"Tout =",Tout)

Lh=16*300*12

print("Lh =",Lh)

doushin=180
print("180L\n",doushin)

dinF = ((16*Tin/np.pi/18/(10**(6)))**(1/3))*1000

doutF = ((16*Tout/np.pi/18/(10**(6)))**(1/3))*1000
print("dinF =",dinF,"doutF =",doutF)

if dinF <= 24:
    dinT =24
elif dinF <= 25 and dinF >= 24:
    dinT=25
elif dinF <= 28 and dinF >= 25:
    dinT=28
elif dinF <= 30 and dinF >= 28:
    dinT=30
elif dinF <= 32 and dinF >= 30:
    dinT=32
elif dinF <= 35 and dinF >= 32:
    dinT=35
elif dinF <= 38 and dinF >= 35:
    dinT=38
elif dinF <= 40 and dinF >= 38:
    dinT=40
elif dinF <= 42 and dinF >= 40:
    dinT=42
elif dinF <= 45 and dinF >= 43:
    dinT=45
elif dinF <= 48 and dinF >= 45:
    dinT=48
elif dinF <= 50 and dinF >= 48:
    dinT=50
elif dinF <= 55 and dinF >= 50:
    dinT=55
elif dinF <= 56 and dinF >= 55:
    dinT=56
elif dinF <= 60 and dinF >= 56:
    dinT=60
elif dinF <= 63 and dinF >= 60:
    dinT=63
elif dinF <= 65 and dinF >= 63:
    dinT=65
else:
    dinT=70

if doutF <= 24:
    doutT = 24
elif doutF <= 25 and doutF >= 24:
    doutT = 25
elif doutF <= 28 and doutF >= 25:
    doutT = 28
elif doutF <= 30 and doutF >= 28:
    doutT = 30
elif doutF <= 32 and doutF >= 30:
    doutT = 32
elif doutF <= 35 and doutF >= 32:
    doutT = 35
elif doutF <= 38 and doutF >= 35:
    doutT = 38
elif doutF <= 40 and doutF >= 38:
    doutT = 40
elif doutF <= 42 and doutF >= 40:
    doutT = 42
elif doutF <= 45 and doutF >= 43:
    doutT = 45
elif doutF <= 48 and doutF >= 45:
    doutT = 48
elif doutF <= 50 and doutF >= 48:
    doutT = 50
elif doutF <= 55 and doutF >= 50:
    doutT = 55
elif doutF <= 56 and doutF >= 55:
    doutT = 56
elif doutF <= 60 and doutF >= 56:
    doutT = 60
elif doutF <= 63 and doutF >= 60:
    doutT = 63
elif doutF <= 65 and doutF >= 63:
    doutT = 65
else:
    dinT = 70
####################################################################
##dinT doutTはあとから自分で選定
dinT = 40
douT = 60
print("JIS 25 28 30 32 35 38 40 42 45 48 50 55 56 60 63 65 70")
print("入力軸の直径は？")
dinT =float(input())
print("出力軸の直径は？")
doutT =float(input())
####################################################################
print("dinT =",dinT,"doutT =",doutT)


####################################################################
print("JISを見ろ！！")
print("自分は")
keyb1 = 10
keyh1 = 8
keyl1 = 50##入力キー
keyb2 = 16
keyh2 = 10
keyl2 = 70##出力キー
print("歯車キーは",keyb1,"x",keyh1,"x",keyl1)
print("歯車キーは",keyb2,"x",keyh2,"x",keyl2)
print("入力軸キーの幅は？")
keyb1 = float(input())
print("入力軸キーの高さは？")
keyh1 = float(input())
print("入力軸キーの長さは？")
keyl1 = float(input())
print("出力軸キーの幅は？")
keyb2 = float(input())
print("出力軸キーの高さは？")
keyh2 = float(input())
print("出力軸キーの長さは？")
keyl2 = float(input())

print("歯車キーは",keyb1,"x",keyh1,"x",keyl1)
print("歯車キーは",keyb2,"x",keyh2,"x",keyl2)
####################################################################
TAUA = 30
SGMA = 100
Fk1 = 1000*Tin/dinT*2
Fk2 = 1000*Tout/doutT*2
print("キー部の接線力は")
print("入力のFk1 =",Fk1,"出力Fk2 =",Fk2)

TAUk1 = Fk1/(keyb1*(keyl1-(keyb1/2)))
SGMk1 = Fk1/((keyh1/2)*(keyl1-(keyb1/2)))
print("入力部のキーにかかる応力まとめ")
print("せん断応力 =",TAUk1,"面圧強度 =",SGMk1)

if TAUk1 >= 30 or SGMk1 >= 100:
    print("キーの耐久力不足だ出なおしてこい")
    exit()

TAUk2 = Fk2/(keyb2*(keyl2-(keyb2/2)))
SGMk2 = Fk2/((keyh2/2)*(keyl2-(keyb2/2)))

print("出力部のキーにかかる応力まとめ")
print("せん断応力 =",TAUk2,"面圧強度 =",SGMk2)

if TAUk2 >= 30 or SGMk2 >= 100:
    print("キーの耐久力不足だ出なおしてこい")
    exit()
###########################################################################
###############内径３０以下は違うよ
ZI_d1 = 45
ZI_d2 = 65
ZI_D1 = ZI_d1*2 + 10
ZI_D2 = ZI_d2*2 + 10
print("僕の軸受は入力45で出力は65だよ")
print("入力軸の軸受の内径は？")
ZI_d1 = float(input())
print("出力軸の軸受の内径は？")
ZI_d2 = float(input())
ZI_D1 = ZI_d1*2 + 10
ZI_D2 = ZI_d2*2 + 10

if ZI_d1 <= 30:
    print("入力軸の軸受の外径は？")
    ZI_D1 = float(input())
if ZI_d2 <= 30:
    print("出力軸の軸受の外径は？")
    ZI_D2 = float(input())
print("軸受寸法について")
print("入力の内径は",ZI_d1,"外径は",ZI_D1)
print("出力の内径は",ZI_d2,"外径は",ZI_D2)
##########################################################################

GY_d2 =ZI_d2 +5
print("出力軸の歯車の内径は")
print(GY_d2)

#########################################
keyb3 = 20
keyh3 = 12##歯車
print("歯車のキー寸法自分は20×12だよー")
print("歯車キーの幅は？")
keyb3 = float(input())
print("歯車キーの高さは？")
keyh3 = float(input())
########################################

Fk3 = 1000*Tout/(GY_d2/2)
print("キーの接線力は",Fk3)

keyl3F1=Fk3/(30*keyb3)+keyb3

keyl3F2=Fk3/(100*(keyh3/2))+keyb3
print("入力部のキーにかかる応力まとめ")
print("せん断応力 =",keyl3F1,"面圧強度 =",keyl3F2)

#########################################################
keyl3 = 50
print("僕は50㎜だけど君は？歯車のキーの長さどーする？")
keyl3 = float(input())

#########################################################
print("歯車キーは",keyb3,"x",keyh3,"x",keyl3)
Z1=29
Z2T1=79
Z2T2=83
a = 20/180*np.pi
ZTT1 = []
ZTT2 = []
print("小歯車23のとき")
Z1 =23
Z2F =Z1*R
if Z2F <= 43:
    Z2T1 = 41
    Z2T2 = 43
elif Z2F >= 43 and Z2F <=47:
    Z2T1 = 43
    Z2T2 = 47
elif Z2F >= 47 and Z2F <= 53:
    Z2T1 = 47
    Z2T2 = 53
elif Z2F >= 53 and Z2F <=59:
    Z2T1 = 53
    Z2T2 = 59
elif Z2F >= 59 and Z2F <=61:
    Z2T1 = 59
    Z2T2 = 61
elif Z2F >= 61 and Z2F <=67:
    Z2T1 = 61
    Z2T2 = 67
elif Z2F >= 67 and Z2F <=71:
    Z2T1 = 67
    Z2T2 = 71
elif Z2F >= 71 and Z2F <=73:
    Z2T1 = 71
    Z2T2 = 73
elif Z2F >= 73 and Z2F <=79:
    Z2T1 = 73
    Z2T2 = 79
elif Z2F >= 79 and Z2F <=83:
    Z2T1 = 79
    Z2T2 = 83
elif Z2F >= 83 and Z2F <=89:
    Z2T1 = 83
    Z2T2 = 89
elif Z2F >= 89 and Z2F <=97:
    Z2T1 = 89
    Z2T2 = 97
elif Z2F >= 97 and Z2F <=101:
    Z2T1 = 97
    Z2T2 = 101
elif Z2F >= 101 and Z2F <=103:
    Z2T1 = 101
    Z2T2 = 103
elif Z2F >= 103 and Z2F <=109:
    Z2T1 = 103
    Z2T2 = 109
elif Z2F >= 109 and Z2F <=113:
    Z2T1 = 109
    Z2T2 = 113
else:
    Z2T1 = 113
    Z2T2 = 127
print("Z2T1 =",Z2T1,"Z2T2 =",Z2T2)
RT1 = Z2T1/Z1
RT2 = Z2T2/Z1
print("減速比1 =",RT1,"減速比2 =",RT2)
gosa1 = abs(RT1-R)/R*100
gosa2 = abs(RT2-R)/R*100
print("誤差1 =",gosa1,"誤差2 =",gosa2)
CAM1=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T1+2)**2)-((Z2T1*np.cos(a))**2))**(1/2))-Z2T1*np.sin(a))/(2*np.pi*np.cos(a))
CAM2=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T2+2)**2)-((Z2T2*np.cos(a))**2))**(1/2))-Z2T2*np.sin(a))/(2*np.pi*np.cos(a))
print("かみ合い率1 =",CAM1,"かみ合い率2 =",CAM2)
if gosa1 >= 3 or CAM1 <= 1.7:
    print("11111111111outoutoutoutout11111111111")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T1]
if gosa2 >= 3 or CAM2 <= 1.7:
    print("22222222222outoutoutoutout22222222222")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T2]
print("小歯車29のとき")
Z1 =29
Z2F =Z1*R
if Z2F <= 43:
    Z2T1 = 41
    Z2T2 = 43
elif Z2F >= 43 and Z2F <=47:
    Z2T1 = 43
    Z2T2 = 47
elif Z2F >= 47 and Z2F <= 53:
    Z2T1 = 47
    Z2T2 = 53
elif Z2F >= 53 and Z2F <=59:
    Z2T1 = 53
    Z2T2 = 59
elif Z2F >= 59 and Z2F <=61:
    Z2T1 = 59
    Z2T2 = 61
elif Z2F >= 61 and Z2F <=67:
    Z2T1 = 61
    Z2T2 = 67
elif Z2F >= 67 and Z2F <=71:
    Z2T1 = 67
    Z2T2 = 71
elif Z2F >= 71 and Z2F <=73:
    Z2T1 = 71
    Z2T2 = 73
elif Z2F >= 73 and Z2F <=79:
    Z2T1 = 73
    Z2T2 = 79
elif Z2F >= 79 and Z2F <=83:
    Z2T1 = 79
    Z2T2 = 83
elif Z2F >= 83 and Z2F <=89:
    Z2T1 = 83
    Z2T2 = 89
elif Z2F >= 89 and Z2F <=97:
    Z2T1 = 89
    Z2T2 = 97
elif Z2F >= 97 and Z2F <=101:
    Z2T1 = 97
    Z2T2 = 101
elif Z2F >= 101 and Z2F <=103:
    Z2T1 = 101
    Z2T2 = 103
elif Z2F >= 103 and Z2F <=109:
    Z2T1 = 103
    Z2T2 = 109
elif Z2F >= 109 and Z2F <=113:
    Z2T1 = 109
    Z2T2 = 113
else:
    Z2T1 = 113
    Z2T2 = 127

print("Z2T1 =",Z2T1,"Z2T2 =",Z2T2)

RT1 = Z2T1/Z1
RT2 = Z2T2/Z1
print("減速比1 =",RT1,"減速比2 =",RT2)
gosa1 = abs(RT1-R)/R*100
gosa2 = abs(RT2-R)/R*100
print("誤差1 =",gosa1,"誤差2 =",gosa2)
CAM1=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T1+2)**2)-((Z2T1*np.cos(a))**2))**(1/2))-Z2T1*np.sin(a))/(2*np.pi*np.cos(a))
CAM2=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T2+2)**2)-((Z2T2*np.cos(a))**2))**(1/2))-Z2T2*np.sin(a))/(2*np.pi*np.cos(a))
print("かみ合い率1 =",CAM1,"かみ合い率2 =",CAM2)
if gosa1 >= 3 or CAM1 <= 1.7:
    print("11111111111outoutoutoutout11111111111")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T1]
if gosa2 >= 3 or CAM2 <= 1.7:
    print("22222222222outoutoutoutout22222222222")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T2]
print("小歯車31のとき")
Z1 =31
Z2F =Z1*R
if Z2F <= 43:
    Z2T1 = 41
    Z2T2 = 43
elif Z2F >= 43 and Z2F <=47:
    Z2T1 = 43
    Z2T2 = 47
elif Z2F >= 47 and Z2F <= 53:
    Z2T1 = 47
    Z2T2 = 53
elif Z2F >= 53 and Z2F <=59:
    Z2T1 = 53
    Z2T2 = 59
elif Z2F >= 59 and Z2F <=61:
    Z2T1 = 59
    Z2T2 = 61
elif Z2F >= 61 and Z2F <=67:
    Z2T1 = 61
    Z2T2 = 67
elif Z2F >= 67 and Z2F <=71:
    Z2T1 = 67
    Z2T2 = 71
elif Z2F >= 71 and Z2F <=73:
    Z2T1 = 71
    Z2T2 = 73
elif Z2F >= 73 and Z2F <=79:
    Z2T1 = 73
    Z2T2 = 79
elif Z2F >= 79 and Z2F <=83:
    Z2T1 = 79
    Z2T2 = 83
elif Z2F >= 83 and Z2F <=89:
    Z2T1 = 83
    Z2T2 = 89
elif Z2F >= 89 and Z2F <=97:
    Z2T1 = 89
    Z2T2 = 97
elif Z2F >= 97 and Z2F <=101:
    Z2T1 = 97
    Z2T2 = 101
elif Z2F >= 101 and Z2F <=103:
    Z2T1 = 101
    Z2T2 = 103
elif Z2F >= 103 and Z2F <=109:
    Z2T1 = 103
    Z2T2 = 109
elif Z2F >= 109 and Z2F <=113:
    Z2T1 = 109
    Z2T2 = 113
else:
    Z2T1 = 113
    Z2T2 = 127

print("Z2T1 =",Z2T1,"Z2T2 =",Z2T2)

RT1 = Z2T1/Z1
RT2 = Z2T2/Z1
print("減速比1 =",RT1,"減速比2 =",RT2)
gosa1 = abs(RT1-R)/R*100
gosa2 = abs(RT2-R)/R*100
print("誤差1 =",gosa1,"誤差2 =",gosa2)
CAM1=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T1+2)**2)-((Z2T1*np.cos(a))**2))**(1/2))-Z2T1*np.sin(a))/(2*np.pi*np.cos(a))
CAM2=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T2+2)**2)-((Z2T2*np.cos(a))**2))**(1/2))-Z2T2*np.sin(a))/(2*np.pi*np.cos(a))
print("かみ合い率1 =",CAM1,"かみ合い率2 =",CAM2)
if gosa1 >= 3 or CAM1 <= 1.7:
    print("11111111111outoutoutoutout11111111111")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T1]
if gosa2 >= 3 or CAM2 <= 1.7:
    print("22222222222outoutoutoutout22222222222")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T2]
print("小歯車37のとき")
Z1 =37
Z2F =Z1*R
if Z2F <= 43:
    Z2T1 = 41
    Z2T2 = 43
elif Z2F >= 43 and Z2F <=47:
    Z2T1 = 43
    Z2T2 = 47
elif Z2F >= 47 and Z2F <= 53:
    Z2T1 = 47
    Z2T2 = 53
elif Z2F >= 53 and Z2F <=59:
    Z2T1 = 53
    Z2T2 = 59
elif Z2F >= 59 and Z2F <=61:
    Z2T1 = 59
    Z2T2 = 61
elif Z2F >= 61 and Z2F <=67:
    Z2T1 = 61
    Z2T2 = 67
elif Z2F >= 67 and Z2F <=71:
    Z2T1 = 67
    Z2T2 = 71
elif Z2F >= 71 and Z2F <=73:
    Z2T1 = 71
    Z2T2 = 73
elif Z2F >= 73 and Z2F <=79:
    Z2T1 = 73
    Z2T2 = 79
elif Z2F >= 79 and Z2F <=83:
    Z2T1 = 79
    Z2T2 = 83
elif Z2F >= 83 and Z2F <=89:
    Z2T1 = 83
    Z2T2 = 89
elif Z2F >= 89 and Z2F <=97:
    Z2T1 = 89
    Z2T2 = 97
elif Z2F >= 97 and Z2F <=101:
    Z2T1 = 97
    Z2T2 = 101
elif Z2F >= 101 and Z2F <=103:
    Z2T1 = 101
    Z2T2 = 103
elif Z2F >= 103 and Z2F <=109:
    Z2T1 = 103
    Z2T2 = 109
elif Z2F >= 109 and Z2F <=113:
    Z2T1 = 109
    Z2T2 = 113
else:
    Z2T1 = 113
    Z2T2 = 127

print("Z2T1 =",Z2T1,"Z2T2 =",Z2T2)

RT1 = Z2T1/Z1
RT2 = Z2T2/Z1
print("減速比1 =",RT1,"減速比2 =",RT2)
gosa1 = abs(RT1-R)/R*100
gosa2 = abs(RT2-R)/R*100
print("誤差1 =",gosa1,"誤差2 =",gosa2)
CAM1=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T1+2)**2)-((Z2T1*np.cos(a))**2))**(1/2))-Z2T1*np.sin(a))/(2*np.pi*np.cos(a))
CAM2=(((((Z1+2)**2)-((Z1*np.cos(a))**2))**(1/2))-Z1*np.sin(a)+((((Z2T2+2)**2)-((Z2T2*np.cos(a))**2))**(1/2))-Z2T2*np.sin(a))/(2*np.pi*np.cos(a))
print("かみ合い率1 =",CAM1,"かみ合い率2 =",CAM2)
if gosa1 >= 3 or CAM1 <= 1.7:
    print("11111111111outoutoutoutout11111111111")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T1]
if gosa2 >= 3 or CAM2 <= 1.7:
    print("22222222222outoutoutoutout22222222222")
else:
    ZTT1 = ZTT1 + [Z1]
    ZTT2 = ZTT2 + [Z2T2]

print(ZTT1)
print(ZTT2)

moj = []
Ztest1=[]
Ztest2=[]
Ztest1 = Ztest1+ZTT1
Ztest2 = Ztest2+ZTT2

count = 0

while count <= len(Ztest1)-1:
    ZTTT1 = Ztest1[count]
    ZTTT2 = Ztest2[count]
    print("歯車が",ZTTT1,":",ZTTT2,"のとき")
    gear3_d1 =3*ZTTT1
    gear3_d2 =3*ZTTT2
    gear3_dis = (gear3_d1+gear3_d2)/2
    gear3_ZK=gear3_dis-((ZI_D1+ZI_D2)/2)
    gear3_d1_in= gear3_d1-3*2.5
    gear4_d1 =4*ZTTT1
    gear4_d2 =4*ZTTT2
    gear4_dis = (gear4_d1+gear4_d2)/2
    gear4_ZK = gear4_dis - ((ZI_D1 + ZI_D2) / 2)
    gear4_d1_in = gear4_d1 - 4 * 2.5
    print("moj==3 d1 =",gear3_d1,"d2 =",gear3_d2,"distance =",gear3_dis,"軸受 =",gear3_ZK,"底 =",gear3_d1_in)
    print("moj==4 d1 =",gear4_d1,"d2 =",gear4_d2,"distance =",gear4_dis,"軸受 =",gear4_ZK,"底 =",gear4_d1_in)
    if gear3_dis >=150 and gear3_dis <= 210 and gear3_ZK >= 47:
        if gear4_dis >= 150 and gear4_dis <= 210 and gear4_ZK >= 47:
            moj = moj +[3,4]
            ZTT1.insert(count,ZTTT1)
            ZTT2.insert(count, ZTTT2)
        else:
            moj = moj +[3]
    else:
        if gear4_dis >= 150 and gear4_dis <= 210 and gear4_ZK >= 47:
            moj = moj +[4]
        else:
            ZTT1.pop(count)
    count=count+1

print("小歯車",ZTT1)
print("大歯車",ZTT2)
print("モジュール",moj)

ZTF1 =np.array(ZTT1)
ZTF2 =np.array(ZTT2)
uu = ZTF2/ZTF1
moju=np.array(moj)
hb = moju * 10
aaaa= ZTF1*moju
print("小基準円",aaaa)
Fsen =1000*Tin/(aaaa/2)
print("歯幅",hb)
print("接線力",Fsen)
print("UU",uu)
Yu =[1 if AAA<=24 else 0.89 for AAA in ZTF1]
print(Yu)
Kti=Fsen*1.1/(aaaa*hb*(uu/(uu+1)))
print("K値",Kti)

Uti = Fsen*1.2*Yu/(moju*hb*1)
print("U値",Uti)

Fn =Fsen/np.cos(a)
print("Fn =",Fn )
Fn2 = Fn/2
print("Fn/2 =",Fn2)
Fr = 1.2*Fn2
print("Fr =",Fr)
fn = (33.3/Nin)**(1/3)
print("fn =",fn)
fh = (Lh/500)**(1/3)
print("fh =",fh)
CCC = fh*Fr/fn
print("C =",CCC)

ZTTT1 = 31
ZTTT2 = 97

print("小歯車",ZTT1)
print("大歯車",ZTT2)
print("選べ良い歯車を！")
print("小歯車")
ZTTT1 =float(input())
print("大歯車")
ZTTT2 =float(input())

