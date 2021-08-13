def c(num):
    '''num --> nonnegative int
    finds the catalan number of that num
    'def c' is supposed to be 'def get_catalan_number' '''
    if num == 0:
        return 1
    else:
        count1 = 0
        count2 = num - 1
        catalan = 0
        while count2 >= 0:
            catalan += c(count1)*c(count2)
            count1 += 1
            count2 -= 1
        return catalan

'''print(c(1))
print(c(2))
print(c(3))
print(c(4))'''
print(c(30))
