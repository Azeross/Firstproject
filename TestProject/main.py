import random
bk = ['abaya', 'baitur','temer','moskva']
mak = ['abaya1', 'baitur1','temer1','moskva1']
kfc = ['abaya2', 'baitur2','temer2','moskva2']
lists = [kfc, bk, mak]
cafe = random.choice(lists)
for name, value in list(locals().items()):
    if cafe is value:
        print(name, random.choice(cafe))
        break