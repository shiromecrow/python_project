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
frist_lamda=18#lamdaの最初の予測値(大きすぎると負になってしまう)
#input##################################
Rein=frist_Re
Re=[frist_Re]
lamda=[frist_lamda]
lamdain=lamda[0]
error_mode=0

Rein=Rein*delta_Re
mode=4
delta=0.01
delta_on=0
B3 = 2.975
bv = 0.4


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

    return Ans

def fdifferential(RA, LAMDA,fmode):#関数f(x)の微分のf'(x)
    global B3
    global bv
    global delta
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
   # if delta_on==1:
   #     Ans=(f(RA,LAMDA+delta,fmode)-f(RA,LAMDA,fmode))/delta

    return Ans


#while Rein<=last_Re:#配列の挿入(指数的に等間隔)
    #Re.append(Rein)
  #  Rein=Rein*delta_Re
#Re=[3217,3447,3677,3907,4136,4366,4596,4596,5285,5975,6664,7353,8043,8732,9422]
Re=[0,3.0525030525030523,6.105006105006105, 9.157509157509157, 12.21001221001221, 15.262515262515262,
 18.315018315018314, 21.367521367521366, 24.42002442002442]
#Re=[0,4.03,8.08,12.1,16.2,20.2,24.2,28.3,32.3]
#Re=[0,1.9,3.80,5.70,7.65,9.56,11.50,13.40,15.30]


while abs(f(Re[0],lamda[0],mode)) >= limit_ratio:
    lamda[0]=lamda[0]-f(Re[0],lamda[0],mode)/fdifferential(Re[0],lamda[0],mode)
    if error_mode ==1:
        lamda[0]='error'
        print("a")
        break


count=1;
while count<=len(Re)-1:
    if error_mode ==1:
        lamdain=frist_lamda
        error_mode=0

    else:
        lamdain=lamda[count-1]
    while abs(f(Re[count],lamdain,mode)) >= limit_ratio:
        lamdain = lamdain - f(Re[count],lamdain,mode) /fdifferential(Re[count],lamdain,mode)
        if error_mode == 1:
            lamdain = 'error'
            break
    lamda.append(lamdain)
    count=count+1

print(lamda)#負の値をチェック

with open('NewtonRaphsonx.csv', 'w', newline='') as p:
    writer = csv.writer(p)
    count=0;

    while count<=len(Re)-1:
        writer.writerow([Re[count],lamda[count]])
        count=count+1




