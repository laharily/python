def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
result = is_even(12345678909876543212345673456454835762983567828)
print (result)

def is_greater(a,b):
    if a > b:
        return True
    else:
        return False
result = is_greater(203875946, 912837465)
print (result)

def myfunc(*args):
    evennums = [ ]
    for a in args:
        if a%2 == 0:
            evennums.append(a)
    return evennums
result = myfunc (2,3,56,7543,45432806,9)
print (result)
            
