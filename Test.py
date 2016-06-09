tc = int(raw_input())

for t in range(tc):
    string1, string2 = raw_input().split()
    
    print string1, string2
    a, b = string1, string2
    
    dictionary={}
    anagram = True
    
    for char in a:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
            
    for char in b:
        if char in dictionary:
            dictionary[char] -= 1
        else:
            anagram = False
            break
        
    
    if anagram:    
        for value in dictionary.values():
            if value == 0:
                continue
            else:
                anagram = False
    
    if anagram:
        print 'Anagram'
    else:
        print 'Not an angram'
        