a=[[1,2],[10,20]]
b=[[2,3],[3,4]]
c=[]


for i in range(len(a)):
    line, sum1= [], 0
    for j in range(len(a[0])):
        #print i, j
       sum1 = a[i][j]+b[i][j]
       line.append(sum1)
    c.append(line)       
        
print c       
       
        