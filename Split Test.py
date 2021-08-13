st = "Print only the words that start with s in this sentence."
wordlist = st.split(" ")
print (wordlist)
for w in wordlist:
    if w.startswith("s"):
        print (w)
