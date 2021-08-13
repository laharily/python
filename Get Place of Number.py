def strip_right_digit(num):
    """strip_right_digit(num) --> int
    Returns num with its right-most digit removed"""
    return num//10

def get_place(num, p):
    """get_place(num,p) -> int
    Returns the digit in the decimal place corresponding to
    pth position (from the right) in positive num."""
    for i in range(p):
        num = strip_right_digit(num) # strips right digit of num
    return num % 10 # reutrns the rightmost digit of num

print(get_place(27183,3))
