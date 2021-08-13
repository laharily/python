import sys
import pickle, shelve

def openfile(filename):
    try:
        thefile = open(filename,'r')
    except IOError as e:
        print("Unable to open the file", filename, "Ending program.\n", e)
        input("\nPress the enter key to exit.")
        sys.exit()
    else:
        return thefile

def nextline(thefile):
    # Return next line from the trivia file, formatted.
    line = thefile.readline()
    line = line.replace("/", "\n")
    return line

def nextblock(thefile):
    # Returns the next block of data from the trivia file.
    category = nextline(thefile)
    question = nextline(thefile)
    answers = []
    for i in range(4):
        answers.append(nextline(thefile))
    correct = nextline(thefile)
    if correct:
        correct = correct[0]
    explanation = nextline(thefile)
    score = nextline(thefile)
    return category, question, answers, correct, explanation, score

name = input("What is your name? ")

def welcome(title):
    # Welcomes the player
    print("\n\t\tWelcome to Trivia Challenge!\n")
    print("\t\t",title, "\n")

def main():
    triviafile = openfile("trivia.txt")
    title = nextline(triviafile)
    welcome(title)
    points = 0

    category, question, answers, correct, explanation, score = nextblock(triviafile)
    while category:
        # Asks question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # Gets answer
        answer = input("What's your answer? ")
        # Checks answer
        if answer == correct:
            print("\nRight!", end=" ")
            points += int(score)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score: ", points, "\n")
        # Gets next block
        category, question, answers, correct, explanation, score = nextblock(triviafile)
    triviafile.close()

    print("That was the last question!")
    print(name + "'s final score is: " + str(points))

    # Writing to and pickling a binary file
    highscores = name + ": " + str(points)
    file = open("highscores.txt", "ab")
    pickle.dump(highscores, file)
    file.close()
    # Reading the binary file
    file = open("highscores.txt", "rb")
    highscores = pickle.load(file)
    print(highscores)
    file.close()
    
main()
input("\nPress enter to exit.")
