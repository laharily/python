def letter_count(inString):
    '''letter_count(inputString) -> None
    prints alphabetized letter count of letters in inputString'''
    letterCount = {}
    abc = "abcdefghijklmnopqrstuvwxyz"
    inString = inString.lower()
    for char in inString:
        if char in abc:
            if char not in letterCount:
                letterCount[char] = 1
            else:
                currentCount = letterCount[char]
                currentCount += 1
                letterCount[char] = currentCount
    for letter in abc:
        if letter in inString:
            count = letterCount[letter]
            # count = inString.count(letter)
            print(letter + ": " + str(count))

# example
letter_count("I like learning Python at Art of Problem Solving!")
'''should print
a: 3
b: 1
e: 3
f: 1
g: 2
h: 1
i: 4
k: 1
l: 4
m: 1
n: 4
o: 4
p: 2
r: 3
s: 1
t: 3
v: 1
y: 1
'''
