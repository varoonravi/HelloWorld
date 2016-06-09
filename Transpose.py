a=[[1,2,5],[3,4,20],[5,6,16]]
l=[]
transpose=[]

for i in range(len(a[0])):
    transpose.append(l)
    l=[]
    for j in range(len(a)):
        l.append(a[j][i])
        
transpose.append(l)
        
        
        
for i in range(len(transpose)):
    print str(transpose[i])+"\n"
        