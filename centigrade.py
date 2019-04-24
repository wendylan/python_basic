#coding=utf-8
"""
    华氏温度换成摄氏度
"""
f = float(input('请输入华氏温度:'));
c = (f-32) / 1.8;
print('%.1f华氏度 = %.1f摄氏度' %(f, c));