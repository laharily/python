# Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together
# with the number of times each letter occurs. Case should be ignored. 
sentence = (input("Please enter a sentence: ")).lower()
alphabet = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
for table in sentence:
    if table == "a":
        alphabet["a"] = alphabet["a"] + 1
    elif table == "b":
        alphabet["b"] = alphabet["b"] + 1
    elif table == "c":
        alphabet["c"] = alphabet["c"] + 1
    elif table == "d":
        alphabet["d"] = alphabet["d"] + 1
    elif table == "e":
        alphabet["e"] = alphabet["e"] + 1
    elif table == "f":
        alphabet["f"] = alphabet["f"] + 1
    elif table == "g":
        alphabet["g"] = alphabet["g"] + 1
    elif table == "h":
        alphabet["h"] = alphabet["h"] + 1
    elif table == "i":
        alphabet["i"] = alphabet["i"] + 1
    elif table == "j":
        alphabet["j"] = alphabet["j"] + 1
    elif table == "k":
        alphabet["k"] = alphabet["k"] + 1
    elif table == "l":
        alphabet["l"] = alphabet["l"] + 1
    elif table == "m":
        alphabet["m"] = alphabet["m"] + 1
    elif table == "n":
        alphabet["n"] = alphabet["n"] + 1
    elif table == "o":
        alphabet["o"] = alphabet["o"] + 1
    elif table == "p":
        alphabet["p"] = alphabet["p"] + 1
    elif table == "q":
        alphabet["q"] = alphabet["q"] + 1
    elif table == "r":
        alphabet["r"] = alphabet["r"] + 1
    elif table == "s":
        alphabet["s"] = alphabet["s"] + 1
    elif table == "t":
        alphabet["t"] = alphabet["t"] + 1
    elif table == "u":
        alphabet["u"] = alphabet["u"] + 1
    elif table == "v":
        alphabet["v"] = alphabet["v"] + 1
    elif table == "w":
        alphabet["w"] = alphabet["w"] + 1
    elif table == "x":
        alphabet["x"] = alphabet["x"] + 1
    elif table == "y":
        alphabet["y"] = alphabet["y"] + 1
    elif table == "z":
        alphabet["z"] = alphabet["z"] + 1
print (alphabet)
for key in alphabet:
    if alphabet[key] != 0:
        print (key,": ", alphabet[key])
    
    
    
