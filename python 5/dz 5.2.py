spicok=[1,3,6,8,7,5,7,11,4,4]
n=spicok.copy()
for i in range (0,10):
    for k in range (i+1,10):
        if spicok[i]==n[k]:
            print(spicok[i])
        else:
            k+=1
    i+=1