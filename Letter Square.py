def letterSquare(letter, size):
    """letter --> string, size --> int
    returns the letter multiplied by size, size times"""
    letter *= size
    string = ""
    for x in range(size):
        string += letter
        string += "\n"
    return string

print(letterSquare('y',10))
