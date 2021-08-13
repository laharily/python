# Returns a string with the even numbered capitalized and odd numbered letters
# lower cased.
def myfunc(string):
    outstr = ""
    for i in range(0,len(string)):
        if i % 2 == 0:
            outstr = outstr + (string[i].upper())
        else:
            outstr = outstr + (string[i])
    return outstr

outstr = myfunc("supercalifragilisticexpialodocious")
print (outstr)

# Capitalizes the first and fourth letters of a name.
def myfunc1(old_macdonald):
    ostr = ""
    for o in range (0, len(old_macdonald)):
        if o == 0 or o == 3:
            ostr = ostr + (old_macdonald[o].upper())
        else:
            ostr = ostr + (old_macdonald[o])
    return ostr

ostr = myfunc1("oldmacdonald")
print (ostr)
    
        
