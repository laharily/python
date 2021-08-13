file = open("wordlist.txt" , "r")
values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
          'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
          'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
highestScore = 0 # initialize highest score
highestWord = ""

for word in file:
    score = 0 # initializes score for each word
    word = word.upper()
    word = word.strip("\n") # takes out the newline
    if len(word) == 7: # if the word is 7 letters long
        if word.find("Z") == -1: # if the word doesn't have a "Z" in it
            for x in word:
                score += values[x] # sums up the score for the word based on the letters
            # sets the new highest score and value
            if score > highestScore: # you can also do >= to get the other word
                highestScore = score
                highestWord = word

print(highestScore)
print(highestWord)
file.close

''' Another version for highest word instead of highest 7-letter word without z:

for word in file:
    score = 0 # initializes score for each word
    word = word.upper() 
    word = word.strip("\n") # takes out the newline
    for x in word:
        score += values[x] # sums up the score for each word
        # sets the new highest score and word
        if score > highestScore: # you can also do >= to get the other word
                highestScore = score
                highestWord = word
'''

            
            
