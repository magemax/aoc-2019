res1=0
res2=0
with open("input.txt") as maf:
    for line in maf:
        l=line.strip().split(",")
        a=[int(k) for k in l]
            #print(z)
aa=[k for k in a]


#part 1 
a[1]=12
a[2]=2
ii=0
while a[ii]!=99:
    if a[ii]==1:
        a[a[ii+3]]=a[a[ii+1]]+a[a[ii+2]]
    if a[ii]==2:
        a[a[ii+3]]=a[a[ii+1]]*a[a[ii+2]]
    ii+=4
print("Part 1 :",a[0])

#part 2
for i in range(100):
    for j in range(100):
        ii=0
        a=[k for k in aa]
        a[1]=i
        a[2]=j
        while a[ii]!=99:
            if a[ii]==1:
                a[a[ii+3]]=a[a[ii+1]]+a[a[ii+2]]
            if a[ii]==2:
                a[a[ii+3]]=a[a[ii+1]]*a[a[ii+2]]
            ii+=4
        if a[0]==19690720:
            print("Part 2 :",i*100+j)