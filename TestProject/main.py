import random
bk = ['abaya', 'baitur','temer','moskva']
mak = ['abaya1', 'baitur1','temer1','moskva1']
kfc = ['abaya2', 'baitur2','temer2','moskva2']
list = [kfc, bk, mak]
cafe = random.choice(list)

if cafe == bk:
    print('bk', random.choice(bk))
elif cafe == mak:
    print('mak', random.choice(mak))
elif cafe == kfc:
    print('kfc', random.choice(kfc))
    else