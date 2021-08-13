st = "Print only the words that start with s in this sentence."
wordlist = st.split(" ")
print (wordlist)
for w in wordlist:
    if w.startswith("s"):
        print (w)


for r in range(0,11,2):
    print (r)


string = "Print every word in this sentece that has an even number of letters."
wordlist = string.split(" ")
for o in wordlist:
    if len(o) %2 == 0:
        print (o)


for r in range(1,101):
    if r %3 == 0 and r %5 == 0:
        print ("FizzBuzz")
    elif r %5 == 0:
        print ("Buzz")
    elif r %3 == 0:
        print ("Fizz")
    else:
        print (r)


def myfunc (x, y, z):
    if z == True:
        return x
    else:
        return y
a = myfunc ("supercalifragilisticexpialodocious!", "Wwaa, wwaa, wwaaaaa!!!", True)
print (a)




