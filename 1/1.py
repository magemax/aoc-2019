res1=0
res2=0
with open("input.txt") as maf:
    for line in maf:
        l=line.strip().split(" ")
        z=int(l[0])
        z=z//3-2
        res1+=z
        while z>=0:
            res2+=z
            z=z//3-2
            #print(z)
print(res1)
print(res2)