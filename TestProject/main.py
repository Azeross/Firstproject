import random
bk = ['abaya', 'baitur','temer','moskva']
mak = ['abaya1', 'baitur1','temer1','moskva1']
kfc = ['abaya2', 'baitur2','temer2','moskva2']
lists = [kfc, bk, mak]
cafe = random.choice(lists)

for key,value in globals().iteritems():
    if type(value) == list and value == cafe:
        print(key, random.choice(cafe))
