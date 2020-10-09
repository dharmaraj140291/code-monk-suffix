suf=input().split()
al=str(suf[0])
k=int(suf[1])
l,i=[],0
while i<len(al):
     l.append(al[i:])
     i+=1
print(l[k])

