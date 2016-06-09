#String Reversal

str_input=raw_input("Enter a String\n")
l=[]
string=""

for i in str_input:
    l.append(i)
    
res=reversed(l)

for i in res:
    string += i
    
    
print "The reverse of "+str_input+" is "+string
    