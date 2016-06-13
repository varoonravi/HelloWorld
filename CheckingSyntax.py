
def main():
    print "hello, this is a test main"


   
def something():
    print "dont know what is happening"
    
    

if __name__ == "__main__":
    main()
    something()
    
    


d = {}
l = ['list','of','words','so','just','checking','it','out','it','out']

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
for k,v in d.items():
    print k+' has occurred ' + str(v) + ' times'
    
    

f = open('E:\Python Programs\WisdomBucketList.txt', 'r')
for line in f:
    print line