a = [[2,3],[1,2]]
b = [[1,0],[0,1]]
sum1 = 0
l = []
result = []

for i in range(len(a)):
    result.append(l)
    l=[]
    for j in range(len(b[0])):
        for k in range(len(a[0])):
            sum1 += a[i][k] * b[k][j]
        
        l.append(sum1)
        sum1 = 0

result.append(l)            
            
            
for i in result:
    print i
            
            
            