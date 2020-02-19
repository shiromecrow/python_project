import sys
import numpy as np
import matplotlib.pyplot as plt
import csv

#input##################################
delta_Re=1.5#積の分解能
frist_Re=3.0*10**3#最初のレイノルズ数
last_Re=1.0*10**7#最後のレイノルズ数
mode=0#関数選択用フラグ
limit_ratio=1.0*10**-4#収束判定値
frist_lamda=8#lamdaの最初の予測値(大きすぎると負になってしまう)
frist_lamda2=1.1
#input##################################
Rein=frist_Re
Re=[]
lamda=[frist_lamda]
lamdain=lamda[0]
A=[0]
error_mode=0

Rein=Rein*delta_Re
mode=4
delta=0.01
delta_on=0
B3 = 1.89#2.975
bv = 0.3
Av =11.83881#24.42002442002442
siki=[0]

def f(RA,LAMDA,fmode):#関数f(x)好きな関数をどうぞ
    global error_mode
    global B3
    global bv
    if fmode == 0:
        Ans = 2 * np.log10(RA * np.sqrt(LAMDA)) - 0.8 - 1 / np.sqrt(LAMDA)
    if fmode == 1:
        Ans = 1.903 * np.log10(RA * np.sqrt(LAMDA)) - 0.537 - 1 / np.sqrt(LAMDA)
    if fmode == 2:
        Ans = 2.116 * np.log10(RA * np.sqrt(LAMDA)) - 1.305 - 1 / np.sqrt(LAMDA)
    if fmode == 3:
        Ans = 2.092 * np.log10(RA * np.sqrt(LAMDA)) - 1.176 - 1 / np.sqrt(LAMDA)
    if fmode == 4:
        if LAMDA <= 0 or LAMDA<=B3/2:
            error_mode=1
            Ans=1
        else:
            Ans = -RA + LAMDA ** 2 * (np.pi - np.arcsin(B3 / 2 / LAMDA)) + B3 / 2 * (LAMDA ** 2 - (B3 / 2) ** 2) ** (1 / 2) + bv * B3
    if fmode == 5:
        Ans = -RA + LAMDA ** 2 * (np.arcsin(B3 / 2 / LAMDA)) - B3 / 2 * (LAMDA ** 2 - (B3 / 2) ** 2) ** (
                    1 / 2) + bv * B3


    return Ans

def fdifferential(RA, LAMDA,fmode):#関数f(x)の微分のf'(x)
    global B3
    global bv
    global delta
    global error_mode
    if fmode == 0:
        Ans =1/LAMDA/np.log(10)+1/2*(LAMDA)**(-3/2)
    if fmode == 1:
        Ans = 1.903/2 / LAMDA / np.log(10) + 1 / 2 * (LAMDA) ** (-3 / 2)
    if fmode == 2:
        Ans =2.116/2/LAMDA/np.log(10)+1/2*(LAMDA)**(-3/2)
    if fmode == 3:
        Ans = 2.092/2 / LAMDA / np.log(10) + 1 / 2 * (LAMDA) ** (-3 / 2)
    if fmode == 4:
        R1 = LAMDA + 0.01
        R=LAMDA
        if LAMDA <= 0 or LAMDA <= B3 / 2:
            error_mode = 1
            Ans = 1
        else:
            Ans = ((-RA + R1 ** 2 * (np.pi - np.arcsin(B3 / 2 / R1)) + B3 / 2 * (R1 ** 2 - (B3 / 2) ** 2) ** (
                    1 / 2) + bv * B3) - (
                           -RA + R ** 2 * (np.pi - np.arcsin(B3 / 2 / R)) + B3 / 2 * (R ** 2 - (B3 / 2) ** 2) ** (
                               1 / 2) + bv * B3)) / 0.01
    if fmode == 5:
        R1 = LAMDA + 0.01
        R = LAMDA
        Ans = ((-RA + R1 ** 2 * (np.arcsin(B3 / 2 / R1)) - B3 / 2 * (R1 ** 2 - (B3 / 2) ** 2) ** (
                1 / 2) + bv * B3) - (
                       -RA + R ** 2 * (np.arcsin(B3 / 2 / R)) - B3 / 2 * (R ** 2 - (B3 / 2) ** 2) ** (
                       1 / 2) + bv * B3)) / 0.01

   # if delta_on==1:
   #     Ans=(f(RA,LAMDA+delta,fmode)-f(RA,LAMDA,fmode))/delta

    return Ans


#while Rein<=last_Re:#配列の挿入(指数的に等間隔)
    #Re.append(Rein)
  #  Rein=Rein*delta_Re
#Re=[3217,3447,3677,3907,4136,4366,4596,4596,5285,5975,6664,7353,8043,8732,9422]
#Re=[3.0525030525030523,6.105006105006105, 9.157509157509157, 12.21001221001221, 15.262515262515262,
# 18.315018315018314, 21.367521367521366, 24.42002442002442]
Hv=[0]
theta=[0]
#Re=[4.03,8.08,12.1,16.2,20.2,24.2,28.3,32.3]
#Re=[0,1.9,3.80,5.70,7.65,9.56,11.50,13.40,15.30]
#Re=[25.7388*1/8,25.7388*2/8,25.7388*3/8,25.7388*4/8,25.7388*5/8,25.7388*6/8,25.7388*7/8 ,25.7388]
#Re=[2.971,5.943,8.914,11.885,14.856,17.828,20.799,23.77]
#Re=[35.5*1/8,35.5*2/8,35.5*3/8,35.5*4/8,35.5*5/8,35.5*6/8,35.5*7/8 ,35.5]
#Re=[42.2*1/8,42.2*2/8,42.2*3/8,42.2*4/8,42.2*5/8,42.2*6/8,42.2*7/8 ,42.2]
#Re=[29.46*1/8,29.46*2/8,29.46*3/8,29.46*4/8,29.46*5/8,29.46*6/8,29.46*7/8 ,29.46]
o=1
while o<=8:#配列の挿入(指数的に等間隔)
    Re.append(o/8*Av)
    o=o+1


while abs(f(Re[0],lamda[0],mode)) >= limit_ratio:
    lamda[0]=lamda[0]-f(Re[0],lamda[0],mode)/fdifferential(Re[0],lamda[0],mode)
    if error_mode ==1:
        lamda[0] = frist_lamda2
        mode = 5
        error_mode=2
    print(lamda[0])

if error_mode==0:
    Hv[0]=lamda[0]+(lamda[0]**2-(B3/2)**2)**(1/2)+bv
    siki[0]=1

else:

    Hv[0]=lamda[0]-(lamda[0]**2-(B3/2)**2)**(1/2)+bv
    siki[0]=2
theta[0]=np.arcsin(B3/2/lamda[0])*180/np.pi
count=1;
while count<=len(Re)-1:
    if error_mode ==2 or error_mode ==1:
        lamdain=frist_lamda
        mode = 4
        error_mode=0
    else:
        lamdain=lamda[count-1]
    while abs(f(Re[count],lamdain,mode)) >= limit_ratio:
        lamdain = lamdain - f(Re[count],lamdain,mode) /fdifferential(Re[count],lamdain,mode)
        if error_mode == 1:
            lamdain = frist_lamda2
            mode=5
            error_mode=2
        print("a=",lamdain)

    lamda.append(lamdain)
    if error_mode==0:
        Hv.append(lamdain+(lamdain**2-(B3/2)**2)**(1/2)+bv)
        siki.append(1)
    else:
        Hv.append(lamdain-(lamdain ** 2 - (B3 / 2) ** 2) ** (1 / 2) + bv)
        siki.append(2)
    theta.append(np.arcsin(B3 / 2 / lamdain)*180/np.pi)
    count=count+1

print(lamda)#負の値をチェック
print(Hv)

with open('NewtonRaphsonhiru.csv', 'w', newline='') as p:
    writer = csv.writer(p)
    count=0;
    writer.writerow(["A[cm^2]", "R[cm]", "Hv[cm]", "theta[deg]"])
    while count<=len(Re)-1:
        writer.writerow([Re[count],lamda[count],Hv[count],theta[count],siki[count]])
        count=count+1


