def make_acronym(string):
    '''string --> str
    returns an acronym of string'''
    acronym = ''
    string = string.split()
    for x in string:
        acronym += x[0]
    return acronym

print(make_acronym("Art of Problem Solving"))

