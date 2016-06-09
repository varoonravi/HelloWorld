



print "Enter a String to find out if it is an anagram"
a=raw_input("Enter any String")
b=raw_input("Enter any String")
d1={}
d2={}
boolean = False

if len(a) != len(b):
    print "Not an anagram"

for char in a:
    if char in d1:
        d1[char] += 1
    else:
        d1[char] = 1
        
        
for char in b:
    if char in d2:
        d2[char] += 1
    else:
        d2[char] = 1
        
        
for key in d1:
    if d1[key] == d2[key]:
        continue
    else:
        print 'Not an Anagram'
        boolean = True
        break
    
if boolean ==False:
     print "Is an anagram"