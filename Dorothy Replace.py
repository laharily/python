def replace_word(filename,oldWord,newWord):
    '''replace_word(filename,word) -> None
    Prints text in filename, replaces oldWord with newWord'''
    inputFile = open(filename,"r")
    for line in inputFile:
        line = line.replace(oldWord,newWord)
        print(line, end='')
    inputFile.close()

# test
replace_word('dorothy.txt','Dorothy','your face')
'''Should print:
It was Gizmo that made Dorothy laugh, and saved her from growing as gray as 
her other surroundings. Gizmo was not gray; he was a little black dog, with 
long silky hair and small black eyes that twinkled merrily on either side 
of his funny, wee nose. Gizmo played all day long, and Dorothy played with 
him, and loved him dearly. '''
