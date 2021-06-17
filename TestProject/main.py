import random
bk = ['abaya', 'baitur','temer','moskva']
mak = ['abaya1', 'baitur1','temer1','moskva1']
kfc = ['abaya2', 'baitur2','temer2','moskva2']
list = [kfc, bk, mak]
cafe = random.choice(list)

print(cafe, random.choice(bk))
