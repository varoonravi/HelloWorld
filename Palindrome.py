string=raw_input("Enter a string to check if it is a palindrome\n")
rstring=string[::-1] 
if string == rstring:
    print "Palindrome"
else:
    print "Not a palindrome"
    
    
#any_string[starting_position:ending_position:skipping how many positions from starting to ending]
    #it is equivalent to substring yo.