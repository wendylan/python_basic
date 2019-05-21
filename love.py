"""
心形函数:
    (x²+y²-1)³+x²y³ = 0 心形线
    x²z³+9y²z³/80=(x²+9y²/4+z²-1)³ 心形三维曲面
    x²+y² = (2x²+2y²-x)² 心形线 
"""
import time
sentence = "Dear, I love you forever!"
for char in sentence.split():
    allChar = []
    for y in range(12, -12, -1):
        lst = []
        lst_con = ''
        for x in range(-30, 30):
            formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
        lst.append(lst_con)
        allChar += lst
    print('\n'.join(allChar))
    time.sleep(1)