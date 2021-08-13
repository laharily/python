def translate():
    '''translate() -> None
    Prompts user to enter dictionary files and input and output files
    Changes words in input file according to the dictionary file
    Write translation in output file'''
    
    # input for file names
    dictFileName = input('Enter name of dictionary: ')
    textFileName = input('Enter name of text file to translate: ')
    outputFileName = input('Enter name of output file: ' )
    
    # open files
    meanings = open(dictFileName, 'r')
    inFile = open(textFileName, 'r')
    outFile = open(outputFileName, 'w')
    
    # turn the first file into a dictionary
    dictionary = {}
    for line in meanings:
        line = line.strip("\n")
        line = line.split("|")                 # split each line using the "|" sign
        dictionary[line[0]] = line[1] # add words before and after sign as key and value to dict
    meanings.close()                         # close the file meanings
    
    # translate the input file
    translated = " "    # create new string
    for line in inFile: # in each line
        line = line.lower()
        line = line.split()
        for word in line:               # for each word
            if word in dictionary: # if that word can be translated
                translated += dictionary[word] # find the value of that word in the dictionary and add to string
                translated += " "       # add space after each word
            else:                               # if word can't be translated
                translated += word  # just add word to string
                translated += " "
        translated += "\n"            # after each line add a new line
        
    outFile.write(translated) # write the string into the output file
    inFile.close()                       # close the input file

translate()       # call the function
outFile.close() # close the output file
